import sqlite3

# Connect to sqlite3
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table, retrieve

cursor = connection.cursor()

#create the table

table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

# Insert some more record

cursor.execute('''Insert Into STUDENT values('Saurav' , 'Data Science' , 'A' , '90') ''')
cursor.execute('''Insert Into STUDENT values('Ashish' , 'Machine Learning' , 'B' , '70') ''')
cursor.execute('''Insert Into STUDENT values('Piyush' , 'Generative AI' , 'A' , '99') ''')
cursor.execute('''Insert Into STUDENT values('Sanjay' , 'SAP ABAP' , 'B' , '79') ''')
cursor.execute('''Insert Into STUDENT values('Suresh' , 'SAP Fiori' , 'C' , '60') ''')
cursor.execute('''Insert Into STUDENT values('Rajat' , 'SAP HANA' , 'D' , '80') ''')

#Display all the records

print("The inserted records are")

data= cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)
    
#close the connection

connection.commit()
connection.close()