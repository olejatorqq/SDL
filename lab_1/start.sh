#!/bin/bash

docker-compose down --rmi all

gpg --decrypt postgres-data/students.sql.gpg > postgres-data/students.sql

docker-compose build

docker-compose up -d
