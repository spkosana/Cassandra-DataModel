
# Project Name: Data Modeling with Postgres

###### <strong> Project Overview: <strong>
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.The analytics team is particularly interested in understanding  what songs users are listening to. All the activity of the users and the metadata of the songs available in the app are listed in csv files at location with directory name as "event_data". 

###### <strong> Project Aim: <strong>
Sparkify like a data engineer to create a Casandra database with tables designed to optimize queries on song play analysis. The role of a data engineer is mainly to determine how the data model need to be created for different use cases. As saprkify has given three use cases for the project, tables should be created per use case. 

###### <strong> Project Description
After thoroughly reading through the requirement and understanding the data and needs of sparkify, for analysis team to understand the user activity on the app they need necessary statistics of the activities and the results that are retrieved should be fast and accurate. The primary reason dimensional modeling is its ability to allow data to be stored in a way that is optimized for information retrieval once it has been stored in a database.Dimensional models are specifically designed for optimized for the delivery of reports and analytics.It also provides a more simplified structure so that it is more intuitive for business users to write queries. Tables are de-normalized and are few tables which will have few joins to get the results with high performance. 
    

###### <strong> Database creation Approach: 
<b>cassandra_module.py : </b>
Implemented all the database necessary functions for extracting the files, database creation and creating tables and executing sql in cassandra_module.py
 
###### <strong> Database Design scripts : 
<b>etl.py : </b>This is the script that need to be executed. The script grabs the necessary functions from cassandra_modules.py 
    
# Gist of the etl.py script
    

* Declare filepath variable and point out the directory which append the path.
* Declare cols where it takes the list of the columns that are need in the resultant dataframe. 
* create a session variable and call the function(get_cassandra(dbname)) which creates database and sets the session for given db name
* Declare a variable to store the dataframe and call function(get_dataframe(filepath,cols)) which takes filename and cols variables as input and spits out the dataframe.
* As per the project there are three scenarios that sparkify is looking for. Data modeling will different for every scenario. 
* Tables are created as per the scenario along with the positioning of the columns. 
* Created variable called create query and assigned the create statement based on each scenario 
* created variable called Insert query and assigned the insert statement based on each scenario. 
* created variable called select query and assigned the select statement based on each scenario. 
* created try catch block which takes the above parameters to get the results into variables and loops through it and prints each row. 
    
    
    
# Queries for Scenarios 
###### <strong> Database Modelling Approach:     
I have created the tables with the order of information that is asked for. As per the data modelling concepts of cassandra, the querying conditions are sessionid and inteminsession. Here the partition key is sessionid which brings a group of records. iteminsession would be the clustering key. Primary key is the combination of partition key and clustering key to fetch the unique record.


###### <strong> Scenario 1 : <strong>

<strong> Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4. </strong>
    
As the query is based on sessionid and iteminsession , i have choosed to create the table as below. Data is partitioned by Sessionid and the sorted by clustering column iteminsession
    
* Table name : music_app_history
* Columns:
    * sessionid
    * iteminsession
    * artist
    * song
    * length  
    
<strong> Create Statement:
* CREATE TABLE IF NOT EXISTS music_app_history (sessionid int,  iteminsession int, artist text, song text, length decimal, PRIMARY KEY(sessionid,iteminsession)) 

   
* Primary keys : Combination of below columns to get the unique record. 
    * Partition Key: Sessionid 
    * Clustering Key: iteminsession
    
<strong> Select Statement: Pulling artist, song and length as requested
    * Select artist,song, length from music_app_history where sessionid = 338 and itemInSession = 4

###### <strong> Scenario 2 : <strong>
<strong> Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182 </strong>   
    
As the query is based on userid and sessionid , i have choosed to create the table as below. Data will be stored based on partition key as userid and sessionid. data is ordered by clustering column iteminsession
    
* Table name : music_app_history_user
* Columns: 
    * userid
    * sessionId
    * iteminsession
    * artist
    * song
    * firstname
    * lastname
    
<strong> Create Statement:
    * CREATE TABLE IF NOT EXISTS music_app_history_user (userid int, sessionId int, iteminsession int, artist text, song text, firstname text, lastname text, PRIMARY KEY ((userId,sessionid),itemInSession))

* Primary keys : Combination of below columns to get the unique record.  
    * Partition key : userId, sessionid
    * clustering keys : itemInsession

<strong> Select Statement: Pulling artist, song, firstName and lastName as requested
    * Select artist,song, firstName, lastName from music_app_history_user where userId = 10 and sessionId = 182
    
    
###### <strong> Scenario 3 : <strong>
<strong> Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own' </strong>  

As the query is based on song and userId , i have choosed to create the table as below. The data will be stored based on the partition key as song. here the clustering key would be the user id. 
    


* Table name : music_app_history_song
* Columns:
    * song
    * userId
    * firstName
    * lastName   
    
<strong> Create Statement:
    * CREATE TABLE IF NOT EXISTS music_app_history_song (song text, userid int, firstname text, lastname text, PRIMARY KEY(song,userid))

* Primary keys : Combination of below columns to get the unique record. 
    * Partition keys : song
    * clustering keys : userid   
    
<strong> Select Statement: Pulling firstName and lastName as requested
    * Select firstname,lastname from music_app_history_song where song='All Hands Against His Own
    
<strong> Below is the screenshot of the all the queries execution run using python etl.py
    
<img src="images/Project_1B_Output.JPG">