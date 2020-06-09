from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters

import pymysql

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {'host':'127.0.0.1',
                'user':'root',
                'passwd':'liuhaozhe0253',
                'db':'vsearch1', }
    conn = pymysql.connect(**dbconfig)
    cur = conn.cursor()
    _SQL = """insert into loga
                (phrase,letters,ip,browser_string,result)
                values
                (%s,%s,%s,%s,%s)
                """
    cur.execute(_SQL,(req.form['phrase'],
                      req.form['letters'],
                      req.remote_addr,
                      req.user_agent.browser,
                      res,))
    conn.commit()
    cur.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )

@app.route('/viewlog')
def view_the_log() ->'html':
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearchl',
                'passwd': 'vsearchpassword',
                'db': 'vsearchDB1', }
    conn = pymysql.connect(**dbconfig)
    cur = conn.cursor()
    _SQL = """select phrase,letters,ip,browser_string,result
              from loga
           """
    cur.execute(_SQL)
    contents = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    titles = ('Form Data','Remote_addr','User_agent','Results')

    return render_template('viewlog.html',
                            the_title = 'View log',
                            the_row_titles = titles,
                            the_data = contents)


# @app.route('/')
# def hello()->'302':
#     return redirect('/entry')

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry1.html',
                           the_title='Welcome to Python')


# get, post <form>

app.run()

if __name__ == '__main__':
    app.run(debug=True)
    # 查看测试信息
