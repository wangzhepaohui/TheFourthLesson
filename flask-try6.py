from flask import Flask, render_template, request,escape

from werkzeug.utils import redirect
from vsearch import search4letters

#对文件操作
#todo = open('a.txt','a')

app = Flask(__name__)

def log_request(req:'flask_request',res:str) -> None:
    with open('vsearch.log','a')as log:
        #print(str(dir(req)),res,file=log)
        print(req.form,file=log,end='|')
        print(req.remote_addr,file=log,end='|')
        print(req.user_agent,file=log,end='|')
        print(req.form,file=log,end='|')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request,results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log() ->str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)




#判断如何运行（是否被引用）
if __name__ == '__main__':
    app.run(debug=True)
