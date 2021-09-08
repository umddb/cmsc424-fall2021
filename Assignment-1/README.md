## Assignment 1: SQL Assignment - Part 1, CMSC424, Fall 2021

*The assignment is to be done by yourself.*

The following assumes you have gone through PostgreSQL instructions and have ran some queries on the `university` database. 
It also assumes you have cloned the git repository, and have done a `git pull` to download the directory `Assignment-1`. The files are:

1. README.md: This file
1. populate-sn.sql: The SQL script for creating the data.
1. queries.py: The file where to enter your answer
1. SQLTesting.py: File to be used for running the queries (in `queries.py`) against the database, and generate the file to be submitted.
1. Vagrantfile: A Vagrantfile that creates the `socialnetwork` database and populates it using `populate-sn.sql` file.

### Getting started
Start the VM with `vagrant up` in the main GitHub directory (i.e., the directory that contains `Assignment-1`). The database should already be set up, but if not: 
- Create a new database called `socialnetwork` and switch to it (see the PostgreSQL setup instructions).
- Run `\i /vagrant/Assignment-1/populate-sn.sql` to create and populate the tables. 

If you are using Docker, you can build an image in the main directory using:
`docker build -t "cmsc424" .`
And then run it using:
`docker run --rm -ti -p 8888:8888 -v /Users/amol/git/cmsc424-fall2021:/data cmsc424:latest`
(Make sure to change the directory name appropriately).

The above command will land you in a shell, and you can do `psql` or run Jupyter Notebook there (you may have to start the PostgreSQL server first: `/etc/init.d/postgresql start`)

### Schema 
The dataset contains a synthetic social network dataset (inspired by Facebook etc.). Specifically it contains the following tables:
- Users(userid, name, birthdate, joined)
- Groups(groupid, name)
- Friends(userid1, userid2): This is a symmetric table. For every entry (X, Y), there is a symmetric entry (Y, X).
- Follows(userid1, userid2): This is an asymmetric table. For an entry (X, Y), the reverse entry (Y, X) is NOT required to be present.
- Members(userid, groupid): Membership of users in groups.
- Status(statusid, userid, status_time, text): A status update posted by a user.
- Liked(statusid, userid, liked_time): A user may like someone else's "status update".

The dataset was generated synthetically: the user names, birthdates etc., were randomly generated, and the group names were chosen from a list of universities around the world. The status text is generated as "Status update 1/2/3 by User XYZ", and are not properly ordered -- no queries should involve looking inside the status update.  Only status updates from a period of about 10 days are included in the dataset, with many users having no status updates during that period.

In many cases (especially for complex queries or queries involving `max` or `min`), you will find it easier to create temporary tables using the `with` construct. This also allows you to break down the full query and makes it easier to debug.

You don't have to use the "hints" if you don't want to; there might be simpler ways to solve the questions.

### Testing and submitting using SQLTesting.py
Your answers (i.e., SQL queries) should be added to the `queries.py` file. A simple query is provided for the first answer to show you how it works.
You are also provided with a Python file `SQLTesting.py` for testing your answers.

- We recommend that you use `psql` to design your queries, and then paste the queries to the `queries.py` file, and confirm it works.

- SQLTesting takes quite a few options: use `python3 SQLTesting.py -h` to see the options.

- To get started with SQLTesting, do: `python3 SQLTesting.py -v -i` -- that will run each of the queries and show you your answer.

- If you want to run your query for Question 1, use: `python3 SQLTesting.py -q 1`. 

- `-i` flag to SQLTesting will run all the queries, one at a time (waiting for you to press Enter after each query).

- **Note**: We will essentially run a modified version of `SQLTesting.py` that compares the returned answers against correct answers. So it imperative that `python3 SQLTesting.py` runs without errors.

### Submission Instructions
Submit the `queries.py` file on Gradescope under Assignment 1. 
      
### Assignment Questions
See `queries.py` file.
