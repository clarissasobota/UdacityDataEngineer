# Project - Create a Data Warehouse
A music streaming app wants to move their processes and data into the cloud.  Currently, the data resides in multiple S3 and includes JSON logs of user activity on the app as well as JSON metadata of the songs.  The task is to build an ETL pipeline that extracts the data from S3, stages it in Redshift, and transforms the data into tables for the analytics team to utilize.  

### Project Files
| File | Description|
| --- | ------------|
| create_tables.py | Scripts to drop and create tables on Redshift |
| dwh.cfg | Configuration variables to connect to Redshift cluster|
| sql_queries.py | Queries to drop, create, and insert into tables |
| etl.py | Scripts to load and transform the data from S3 to Redshift |
| README.md | Project information  |

### Project Setup
- **Create a Redshift cluster with the following configurations**
    1. IAM Role that grants Redshift readonly access to S3
    2. Security group that allows traffic on port 5439
    3. Cluster Group that allows all of the subnets in the VPC
- **Create the database structure and tables by executing create_tables.py**
- **Import S3 data into staging tables and transform the data to conform to the proposed database schema by executing etl.py**

### Project Data 
The Star Database Schema, using fact and dimension tables, is going to be used for modeling the data.  The fact table, songplays, contains information such as user_id, song_id, start_time, location, and artist_id.  This model makes it easier to obtain data while minimizing the number of joins needed, which make makes the read queries faster.  
Data is extracted from S3 and imported into two staging tables.  The data is then transformed to populate the tables within the star schema.  
##### staging_events (Staging Table) - Events that have been imported from S3 logs
    artist VARCHAR
    auth VARCHAR
    firstName VARCHAR
    gender CHAR(1)
    itemInSessions INT
    lastName VARCHAR
    length FLOAT
    level VARCHAR
    location VARCHAR
    method VARCHAR
    page VARCHAR
    registration FLOAT
    sessionId INT
    song VARCHAR
    status INT
    ts BIGINT
    userAgent VARCHAR
    userId INT

##### staging_songs (Staging Table) - Song data that has been imported from S3
    num_songs INT
    artist_id VARCHAR
    artist_latitude FLOAT
    artist_longitude FLOAT
    artist_location VARCHAR
    artist_name VARCHAR
    song_id VARCHAR
    title VARCHAR
    duration FLOAT
    year INT

##### songplays (Fact Table) - Song data that has been imported from S3
    songplay_id INT IDENTITY(0,1) PRIMARY KEY
    start_time TIMESTAMP
    user_id INT
    level VARCHAR
    song_id VARCHAR
    artist_id VARCHAR
    session_id INT
    location VARCHAR
    user_agent VARCHAR
    
##### users (Dimension Table) - Users in the application
    user_id INT PRIMARY KEY
    first_name VARCHAR
    last_name VARCHAR
    gender CHAR(1)
    level VARCHAR
    
##### songs (Dimension Table) - Songs in the music database
    song_id VARCHAR PRIMARY KEY
    title VARCHAR
    artist_id VARCHAR
    year INT
    duration FLOAT
    
##### artists (Dimension Table) - Artists in the music database
    artist_id VARCHAR PRIMARY KEY
    name VARCHAR
    location VARCHAR
    latitude FLOAT
    longitude FLOAT
    
##### time (Dimension Table) - Timestamps of records in songplays
    start_time TIMESTAMP PRIMARY KEY
    hour INT
    day INT
    week INT
    month INT
    year INT
    weekday VARCHAR
