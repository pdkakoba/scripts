#!/usr/bin/env perl

use Mojolicious::Lite;
# expanded upon from Joel Berger's excellent blog entry:
# http://blogs.perl.org/users/joel_berger/2012/10/a-simple-mojoliciousdbi-example.html
# connect to database
use DBI;
my $dbh = DBI->connect("dbi:SQLite:database.db","","") or die "Could not connect";

# add helper methods for interacting with database
helper db => sub { $dbh };

helper create_table => sub {
  my $self = shift;
  warn "Creating table 'posts'\n";
  $self->db->do('CREATE TABLE posts ( id integer primary key autoincrement,
  title text,
  body  text);');
};

helper select => sub {
  my $self = shift;
  my $sth = eval { $self->db->prepare('SELECT * FROM posts') } || return undef;
  $sth->execute;
  return $sth->fetchall_arrayref;
};

helper insert => sub {
  my $self = shift;
  my ($title, $body) = @_;
  my $sth = eval { $self->db->prepare('INSERT INTO posts (title, body) VALUES (?,?)') } || return undef;
  $sth->execute( $title, $body);
  return 1;
};

helper delete => sub {
  my $self = shift;
  my ($id) = @_;
  my $sth = $self->db->prepare('DELETE FROM posts WHERE id=?');
  $sth->execute($id);
  return 1;
};

helper edit => sub {
  my $self = shift;
  my ($id) = @_;
  my $sth = $self->db->prepare('SELECT title, body FROM posts WHERE id=?');
  $sth->execute($id);
  return $sth->fetchrow_hashref;
};

helper update => sub {
  my $self = shift;
  my ($id, $title, $body) = @_;  # order of parameter linked to form,
  my $sth = eval { $self->db->prepare("UPDATE posts SET title = ?, body = ?  WHERE id = ?")} || return undef;
  $sth->execute($title, $body, $id);
  return 1;
};
# if statement didn't prepare, assume its because the table doesn't exist
app->select || app->create_table;

# setup base route
any '/' => sub {
  my $self = shift;
  my $rows = $self->select;
  $self->stash( rows => $rows );
  $self->render('index');
};

# setup route which receives data and returns to /
any '/insert' => sub {
  my $self = shift;
  my $title = $self->param('title');
  my $body = $self->param('body');
  my $insert = $self->insert($title, $body);
  $self->redirect_to('/');
};

post '/delete' => sub {
  my $self = shift;
  my $id = $self->param('id');
  my $del = $self->delete($id);
  $self->redirect_to('/');
};

get '/edit' => sub {
  my $self = shift;
  my $id = $self->param('id');
  my $row = $self->edit($id);
  $self->stash( row => $row );
  $self->render('edit');
};

put '/update' => sub {
  my $self = shift;
  my $id = $self->param('id');
  my $title = $self->param('title');
  my $body = $self->param('body');
  my $update = $self->update($id, $title, $body);
  $self->redirect_to('/');
 };

app->start;

__DATA__

@@ index.html.ep

<!DOCTYPE html>
<html>
<head><title>Posts</title></head>
<body>
  <form action="<%=url_for('insert')->to_abs%>" method="post">
    Title: <input type="text" name="title"> 
    Body: <input type="text" name="body"> 
    <input type="submit" value="Add">
  </form>
  <br>
    <form action="<%=url_for('delete')->to_abs%>" method="post">
    Id: <input type="text" name="id">  
    <input type="submit" value="Delete">
  </form>
      <form action="<%=url_for('edit')->to_abs%>">
    Id: <input type="text" name="id">  
    <input type="submit" value="Edit">
  </form>
  
  <br>
  Data: <br>
  <table border="1">
    <tr>
	  <th>Id</th>
      <th>Title</th>
      <th>Body</th>
    </tr>
    % foreach my $row (@$rows) {
      <tr>
        % foreach my $text (@$row) {
          <td><%= $text %></td>
        % }
      </tr>
    % }
  </table>
</body>
</html>

@@edit.html.ep
<head><title>Edit-Post</title></head>
<body>
  %= form_for 'update' => begin
  %= text_field id => $row->{id}
  %= label_for title => 'Title'
  <br>
  %= text_field title => $row->{title}
  <br>
  %= label_for body => 'Body'
  <br>
  %= text_area body => $row->{body}
  <br>
  %= submit_button 'Update'
% end
</body>
</html>