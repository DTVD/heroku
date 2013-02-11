drop table if exists users;
create table users(
  id integer primary key autoincrement,
  name string not null,
  age int not null
);
