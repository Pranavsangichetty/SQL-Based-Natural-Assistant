# pip install db-sqlite3
# pip install sqlite3
import sqlite3

#Connectt to SQlite
#Our database name: Naresh_it_student
connection=sqlite3.connect("ipl_csk_players.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

cursor.execute("DROP TABLE IF EXISTS ipl_csk_players")

#create the table
#Our table name student
#Columns names are: name, course
table_inf="""
CREATE TABLE ipl_csk_players(players_name varchar(30),
                    players_role varchar(30),
                    players_age int,
                    players_salary float);
"""
cursor.execute(table_inf)

#Insert the records

cursor.execute('''Insert Into ipl_csk_players values('Ruturaj Gaikwad','Batsmen',29,1500000)''')
cursor.execute('''Insert Into ipl_csk_players values('Ayush Matre','Batsmen',17,100000)''')
cursor.execute('''Insert Into ipl_csk_players values('Urvil Patel','Batsmen',31,200000)''')
cursor.execute('''Insert Into ipl_csk_players values('Ravindra Jedeja','Allrounder',37,500000)''')
cursor.execute('''Insert Into ipl_csk_players values('Dewald Brevis','Batsmen',23,200000)''')
cursor.execute('''Insert Into ipl_csk_players values('Khaleel Ahmed','Bowler',33,1100000)''')
cursor.execute('''Insert into ipl_csk_players values('Mateesha Patirana','Bowler','23',1200000)''')
cursor.execute('''Insert into ipl_csk_players values('Sam Curran','Allrounder','25',250000)''')
cursor.execute('''Insert into ipl_csk_players values('MS Dhoni','WK-Batsmen','42',1150000)''')
cursor.execute('''Insert into ipl_csk_players values('Noor Ahmed','Bowler','22',400000)''')
cursor.execute('''Insert into ipl_csk_players values('Shivam Dube','Allrounder','33',800000)''')

#Dispaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from ipl_csk_players''')
for row in data:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()