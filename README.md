# Overview

This is the database and the start of connectors for a slack bot I'm writing for my workplace, which does a weird version of telesales. The database stores info about sales and the bot will frequently and automatically query the databse for various bits of motivational info. The database should also be queriable by other software for data analysis and management. Thus I am using a mySQL server and connector, rather than a SQLite database.

The connector class is written as a static, because it is a simple too that the remainder of the bot will use to query.



[Software Demo Video](https://youtu.be/P_28ok1ShSo)

# Relational Database

And EER built in MySQL workbench is included.

# Development Environment

- Python
- MySQL
- 

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [MySQL Documetntation](https://dev.mysql.com/doc/)
* [Query Syntax refreshers](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)

# Future Work

* settings.py or other untracked file to contain connector info (I've been lazy with my .gitignore, just removing the private data before commiting. This is obviously very bad practice.)
* SQL exception handling.
* More static methods, more queries. I have a whole list of use cases and their edges to write methods for. 