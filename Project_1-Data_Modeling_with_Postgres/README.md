### Project Introduction
A new startup company named Sparkify has been collecting data on songs and user activity on their music streaming app.  
They want to analyze this data to try to understand what the trends in what the users are listening to.    
However, there currently is no easy way to query these logs because they exist in several JSON files.  

### Project Files

- data directory - this folder contains the .json files that are to be used to generate the database tables
- log_data - these files contain the log files detailing user activity and are used to populate the following tables:
    - songplays  
    - users  
    - time  

- song_data - these files contain song and artist information used to generate the following tables:
    - songs
    - songplays
    - artists

- create_tables.py - this file contains the functions that create the tables in the database, utilizing the drop and create statements within sql_queries.py
- etl.py - this file contains the functions that are used to generate the tables in the database and utilizes the insert and select statements within sql_queries.py
- sql_queries.py - this file contains the sql queries that create and manage the tables in the database


### Database Design
The database is created using a star schema. This was chosen because of its ability to simplify queries, denormalize data, and perform fast aggregations.  
The fact table, which is the songplays table, is populated with data from the following tables:  
- users
- songs
- artists


### Creating and Populating the Database

1. Run the create_tables.py file to create the database tables
2.  Run the etl.py file to populate the datafiles with the .json files within the data folder
3. Verify the database tables have been created and populated by running test queries:
- SELECT * FROM songplays LIMIT 5  
- SELECT * FROM songs LIMIT 5  
- SELECT * FROM artists LIMIT 5  
- SELECT * FROM users LIMIT 5  
- SELECT * FROM time LIMIT 5 