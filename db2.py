import pymysql
try:
    conn = pymysql.connect(host='127.0.0.1', user="root", passwd="liuhaozhe0253", db="vsearch1", port=3306, charset="utf8")
    cur = conn.cursor()
    _SQL = 'show tables'
    cur.execute(_SQL)
    res = cur.fetchall()
    for d in res:
        print(d)
    cur.close()
    conn.cursor()
except Exception:
    print('出现异常')

