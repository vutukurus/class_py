import sqlite3 #mulitple users
#import MySQLdb
a='''
10000s
'''

b = 90
print b+ 90
asdfsafsafsad
#db=MySQLdb.connect("localhost","username","password","dbname")
test_con = sqlite3.connect("test_db.db")

#Table creation
#test_con.execute("create table dummy_7(name TEXT, sal INT)")

test_con.execute("delete from dummy_7 where sal > 7000")

'''
#drop table table_name --> it will remove totoal table
#describe table_name
test_con.execute('insert into dummy_7(name,sal) values ("test_3",19000)')
test_con.commit()
a = test_con.execute("select * from dummy_7")
print a.fetchall()
'''
test_con.commit()
test_con.close()


'''

#How to view..
#select * from test Class1

create --> create table table_name(colum1 datatype, colum2 datatype)
selection/fetching --> select * from table_name where name="test_2"
insertion/saving --> insert into table_name(column1,column2) values (1,"test")


data=test_con.execute('select * from Class1 where name = "test_2"')
#fetchone -- > fetches only ine record
#fetchall --> fetches all records
process = data.fetchone()
print process

'''

'''
a=[1,conect,2,txtclea]
for  i in a:
  q=insert into dummy_7(name,sal) values (%s,%s)' %(a[j],a[j+1])
  test_con.execute(q)
  j=j+2 #j=2

'''