
''' Documentation is in the read me file along with docstrings in the script'''

import cassandra_module as cm


# getting all file names from events_data 
filepath = cm.os.getcwd() + '/event_data'   


# cols that are needed for the final dataframe which gets from the get dataframe function when below varible is passed
cols = ['artist','firstName','gender','itemInSession','lastName','length', 'level','location','sessionId','song','userId']


# getting cassandra session with the database name that is passed in the function. 
session = cm.get_cassandra('udacity')


# getting the dataframe which extracts all the files from the event_data folder. 
data_df = cm.get_dataframe(filepath,cols)



# Scenario 1 
## TO-DO: Query 1:  Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4


'''Create statement for the scenario 1'''
create_query = "CREATE TABLE IF NOT EXISTS music_app_history (sessionid int,  iteminsession int, artist text, song text, length decimal, PRIMARY KEY(sessionid,iteminsession))"


'''Insert statement for scenario 1 '''
insert_query = "INSERT INTO  music_app_history (sessionid, iteminsession, artist, song, length)"
insert_query = insert_query + "VALUES (%s, %s, %s, %s, %s)"


'''Select statement for scenario 1 '''
select_query = "Select artist,song, length from music_app_history where sessionid = 338 and itemInSession = 4"
     
    
try:
    session.execute(create_query)
    for index, row in data_df.iterrows():
        session.execute(insert_query, (row.sessionId,row.itemInSession,row.artist,row.song,row.length) )
    print("All Rows Inserted Sucessfully for Query 1: \n")
    rows1 = session.execute(select_query)
except Exception as e:
        print(e)

        
''' Results are looped to print out each row in the results set'''
for row in rows1:
    print(row)
    print('\n')


    
# # Scenario 2 
## TO-DO: Query 2: Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name)\
## for userid = 10, sessionid = 182

'''Create statement for the scenario 2'''
create_query2 = "CREATE TABLE IF NOT EXISTS music_app_history_user (userid int, sessionId int, iteminsession int, artist text, song text, firstname text, lastname text, PRIMARY KEY ((userId,sessionid),itemInSession))"


'''Insert statement for scenario 2 '''
insert_query2 = "INSERT INTO  music_app_history_user (userId, sessionId, iteminsession, artist, song, firstName, lastName)"
insert_query2 = insert_query2 + "VALUES (%s, %s, %s, %s, %s, %s, %s)"


'''Select statement for scenario 2 '''
select_query2 = "Select artist,song, firstName, lastName from music_app_history_user where userId = 10 and sessionId = 182"


'''Below is where the table is created and records from the dataframe are inserted and query is executed to get the results'''
try:
    session.execute(create_query2)
    for index, row in data_df.iterrows():
        session.execute(insert_query2, (int(row.userId),row.sessionId,row.itemInSession,row.artist,row.song,row.firstName,row.lastName) )
    print("All Rows Inserted Sucessfully for Query 2: \n")
    rows2 = session.execute(select_query2)
except Exception as e:
        print(e)

        
''' Results are looped to print out each row in the results set'''
for row in rows2:
    print(row)
    print('\n')
    

# # Scenario 3
## TO-DO: Query 3: Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
# select_query3  = "Select firstname,lastname from music_app_history_song where song='All Hands Against His Own'"


'''Create statement for the scenario 3'''
create_query3 = "CREATE TABLE IF NOT EXISTS music_app_history_song (song text, userid int, firstname text, lastname text, PRIMARY KEY(song,userid))"


'''Insert statement for scenario 3 '''
insert_query3 = "INSERT INTO  music_app_history_song (song, userId, firstName, lastName)"
insert_query3 = insert_query3 + "VALUES (%s, %s, %s, %s)"


'''Select statement for scenario 3 '''
select_query3 = "Select firstname,lastname from music_app_history_song where song='All Hands Against His Own'"



'''Below is where the table is created and records from the dataframe are inserted and query is executed to get the results'''
try:
    session.execute(create_query3)
    for index, row in data_df.iterrows():
        session.execute(insert_query3, (row.song,int(row.userId),row.firstName,row.lastName) )
    print("All Rows Inserted Sucessfully for Query 3: \n")
    rows3 = session.execute(select_query3)
except Exception as e:
        print(e)

        
''' Results are looped to print out each row in the results set'''
for row in rows3:
    print(row)
    print('\n')
    

'''Shutting the session'''
session.shutdown()
