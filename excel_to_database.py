import pymysql

f = open(r"attendees1.csv","r")
fstring = f.read()

flist = []
for line in fstring.split('\n'):
    flist.append(line.split(','))
    
db = pymysql.connect("localhost","root","","test")

cursor = db.cursor()

#cursor.execute("DROP TABLE IF EXISTS EMP")

#FIRST_NAME = flist[0][0], LAST_NAME = flist[0][1], EMAIL = flist[0][2]

#queryCreateTable = """ CREATE TABLR EMP(
#                        {} VARCHAR(50) NOT NULL,
#                        {} VARCHAR(50) NOT NULL,
#                        {} EMAIL VARCHAR(100)
#                        )""".format(FIRST_NAME, LAST_NAME, EMAIL)
#cursor.execute(queryCreateTable)
#del flist[0]

rows = ""
for i in range(len(flist)-1):
    rows += "('{}','{}','{}')".format(flist[i][0], flist[i][1], flist[i][2])
    if i != len(flist) - 2:
        rows += ','
        
queryInsert = "INSERT INTO EMP VALUES"+ rows

try:
    cursor.execute(queryInsert)
    db.commit()
except:
    db.rollback()

print("All Done :) ")

db.close()