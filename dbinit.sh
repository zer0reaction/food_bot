#!/bin/bash

touch db/users.db
touch db/database.db

sqlite3 db/users.db \
"CREATE TABLE state(
    user_id int NOT NULL PRIMARY KEY, 
    user_state text
)"

sqlite3 db/database.db \
"CREATE TABLE food(
    label int, 
    food_type int, 
    location int
)"

sqlite3 db/database.db \
"CREATE TABLE food_types(
    label text
)"

sqlite3 db/database.db \
"CREATE TABLE food_locations(
    label text
)"

sqlite3 db/database.db \
"CREATE TABLE food_labels(
    label text, 
    food_type int
)"
