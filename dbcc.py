import pymysql
from DBcn import UseDatebase

dbconfig = {'host':'127.0.0.1',
                'user':'root',
                'passwd':'liuhaozhe0253',
                'db':'vsearch1', }

with UseDatebase(dbconfig) as cur:

    _SQL = """insert into loga
            (pharse, letters, ip, browser_string, result)
            values
            ('hitch-hiker','aeiou','127.0.0.1','Firefox',"{'e','i'}")"""
    cur.execute(_SQL)

with UseDatebase(dbconfig) as cur:
    _SQL = """
        select * from loga
    """
    cur.execute(_SQL)
    res = cur.fetchall()
    for d in res:
        print(d)


