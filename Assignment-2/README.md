# Assignment 2: Advanced SQL 

**This assignment is to be done by yourself, but you are welcome to discuss the assignment with others.**

## Setup 
You can use the same setup as for Assignment 1 for this assignment. The only additional thing we will use here is Java, which was already installed.

## SQL Advanced Constructs (0.5 each -- total 4 points)
Here we use some of the more advanced constructs that are available in SQL, including ranking, functions, procedures, partitioning, triggers, 
and recursion. Not all of these will be covered in depth in class, and you are expected to read the PostgreSQL manual to understand how some of 
these constructs should be used. We have provided links to the appropriate PostgreSQL documentation and/or examples.

See `queries.py` for the details.

## SQL and Java (1.5 point)
One of more prominent ways to use a database system is using an external client, using APIs such as ODBC and JDBC, or proprietary protocols.
This allows you to run queries against the database and access the results from within say a Java or a Python program.

For this part, you have to write/complete a Java program that accesses the database using JDBC, does some computations that are better done in a
programming langauge, and writes back the result to the database.

Here are some useful links:
- [Wikipedia Article](http://en.wikipedia.org/wiki/Java_Database_Connectivity)
- [Another resource](http://www.mkyong.com/java/how-do-connect-to-postgresql-with-jdbc-driver-java/)
- [PostgreSQL JDBC](http://jdbc.postgresql.org/index.html)

The last link has detailed examples in the `documentation` section. The `Assignment-2` directory (in the git repository) also contains an example 
file (`JDBCExample.java`). To run the JDBCExample.java file, do: 
`javac JDBCExample.java` followed by `java -classpath .:./postgresql-42.2.10.jar JDBCExample` (the `jar` file is in the `Assignment-2` directory).

Your task is to compute the `local clustering coefficient` for each `user` using the `friends` table, and write it back to the `users` table (as a `real`).
Specifically:
- Create a new column in the `users` table, called `lcc` of type `real` (you can assume that it doesn't already exist).
- Read in the `friends` table in its entirety.
- For each userid `x`, compute the local clustering coefficient as follows:
    - Let `x1`, `x2`, .., `x_k` be the friends of `x` (from the `friends` table)
    - For each pair of those friends, find out if they are also friends (i.e., check if `x1` and `x2` are friends).
    - Let `N` denote the number of such pairs that are also friends themselves.
    - LCC = (2N)/(k(k-1))
- If a node does not have any friends, then the LCC = 0 by definition
- Write back the LCC for each `userid` into the `lcc` column created above.
- Make sure to `commit` after you are done.

Here are more details on LCC: https://www.centiserver.org/centrality/Local_Clustering_Coefficient/

First few rows of `select * from users` afterwards look like:
```
userid  |        name         | birthdate  |   joined   |     lcc
---------+---------------------+------------+------------+-------------
user0   | Anthony Roberts     | 1998-10-20 | 2007-02-04 |  0.21904762
user1   | Anthony Taylor      | 1967-02-09 | 2014-08-19 |  0.24242425
```

We have provided a skeleton code to get you started. As above, the code will be run using: `javac LCC.java` followed by `java -classpath
.:./postgresql-42.2.10.jar LCC`, and should result in a modified `users` table as described above.


## SQL and Python (1.5 point)
This project is similar to the above, in that you are being asked to write (complete) a Python program that accesses the database using `psycopg2` -- unlike
the above case, `psycopg2` uses a proprietary protocol, not JDBC or ODBC.

Specifically, we have provided a partial program that implements a Web API to execute update/delete/retrieval operations against our `socialnetwork` database. This API
is built using the Python `Flask` library, and couple of other packages built on top of it. 
- You will need to install three more Python modules using `pip3 install flask flask-restful flask_cors` (we have updated the Dockerfile and Vagrantfile to do this)
- If you are using Docker, when running docker, make sure to map the port 5000 (that's the default port for Flask).
- Ensure that PostgreSQL is running (in Docker, use `service postgresql start`)
- Now, in the Assignment-2 directory, you can start the Flask server by doing: `python3 rest.py`
- This should get the Flask server running, and listening on port 5000.
- In your web browser, go to: `http://127.0.0.1:5000/users/' -- you should see the JSON response from the web server with a list of all users in the database
    - If the web server is successfully up but this doesn't work, it's likely a problem with port mapping
- Your task is implement three other, user-specific endpoints:
    - `GET /user/<userid>/`: Given a specific userid, this should return a JSON with some more details about the user as listed in `rest.py`
        - Don't worry about the case where the user is not found in the database
    - `DELETE /user/<userid>`: Given a specific userid, this should delete the user from the backend database
        - You cannot run this from the Web browser easily, instead, the simplest way is to...
        - Use `curl`: Try `curl -X DELETE http://127.0.0.1:5000/user/user10sk3` -- it should return a default message
    - `POST /user/<userid>`: Given the information in the POST payload, this should create a new user with the specific userid
        - As above, you cannot easily run this from the web browser
        - Instead, try: `curl -X POST -d "birthdate=xyz" -d "joined=xyz" -d 'name=linuxize' -d 'userid=linuxize@example.com' 127.0.0.1:5000/user/user1`
        - We have already provided code for parsing the POST payload -- in the server output, you should see the parsed values to be inserted
- For more details, see the `rest.py` file -- it includes specific locations where you have to make the changes as well as discusses the error conditions that need to be
handled.



### Submission
Upload the three files `queries.py`, `LCC.java`, and `rest.py` as separate files to Gradescope (NOT as a Zip file as originally mentioned here).
