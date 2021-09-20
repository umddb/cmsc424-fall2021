# Assignment 5: Advanced SQL 

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
- Write back the LCC for each `userid` into the `lcc` column created above.
- Make sure to `commit` after you are done.

Here are more details on LCC: https://www.centiserver.org/centrality/Local_Clustering_Coefficient/

We have provided a skeleton code to get you started. As above, the code will be run using: `javac LCC.java` followed by `java -classpath
.:./postgresql-42.2.10.jar LCC`, and should result in a modified `users` table as described above.


## SQL and Python (1.5 point)
This project is similar to the above, in that you are being asked to write (complete) a Python program that accesses the database using `psycopg2` -- unlike
the above case, `psycopg2` uses a proprietary protocol, not JDBC or ODBC.


More details to be posted shortly.



### Submission
Zip the `queries.py`, `LCC.java`, and `rest.py` files into a single file, and upload it to Gradescope.
