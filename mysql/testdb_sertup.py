drop database if exists testdb;
create database testdb CHARACTER SET utf8 COLLATE utf8_general_ci;
grant all on testdb.* to 'testuser'@'localhost' identified by 'test623';
