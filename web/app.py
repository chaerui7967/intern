from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/hi')
def hello():    return 'Hello'

@app.route('/')
def hihtml():   return render_template("login.html")

@app.route('/me', methods = ['GET', 'POST'])
def me():
    if request.method == 'GET':
        num = request.args['num']
        return 'get 전달 {}'.format(num)
    else:
        num = request.form['num']
        return 'post 전달 {}'.format(num)

@app.route('/naver')
def naver():    return render_template('naver.html')

@app.route('/daum')
def daum():    return redirect('https://daum.net/')

@app.route('/urltest')
def url_test():    return redirect(url_for('daum'))

@app.route('/move/<url>')
def input(url):
    if url == 'naver':
        return redirect('https://naver.com')
    elif url == 'daum':
        return redirect('https://daum.net')
    else:
        pass





# except
@app.errorhandler(404)
def page_not_found(error):  return 'no page, check url', 404


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=True)