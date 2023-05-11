
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="ericsson_virtual")

mycursor=mydb.cursor()

mycursor.execute("update ericsson_emps set ename='sandeep' where empid=125");

mydb.commit();