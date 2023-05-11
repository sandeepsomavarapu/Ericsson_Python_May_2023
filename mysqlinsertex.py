
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="ericsson_virtual")

mycursor=mydb.cursor()

mycursor.execute("insert into ericsson_emps values(125,'suresh')");

mydb.commit();