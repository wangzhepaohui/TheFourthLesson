import pymysql

conn = pymysql.connect(host='127.0.0.1', user="root", passwd="liuhaozhe0253", db="vsearch1", port=3306, charset="utf8")
cur = conn.cursor()
_SQL = """insert into loga
        (pharse, letters, ip, browser_string, result)
        values
        ('hitch-hiker','aeiou','127.0.0.1','Firefox',"{'e','i'}")"""
cur.execute(_SQL)
conn.commit()

_SQL = """
    select * from loga
"""
cur.execute(_SQL)
res = cur.fetchall()
for d in res:
    print(d)
cur.close()
conn.cursor()

