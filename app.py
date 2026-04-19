from flask import Flask, request, render_template, make_response, session

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/')
def index():
    user_language = request.cookies.get('user_language')
    return render_template('index.html', user_language=user_language)

@app.route('/set_language/<language>')
def set_language(language):
    resp = make_response(render_template('set_language.html'))
    resp.set_cookie('user_language', language)   # FIXED INDENTATION
    return resp

@app.route('/session')
def index_session():
    session['visit_count'] = session.get('visit_count', 0) + 1
    return render_template('index_session.html',
                           visit_count=session['visit_count'])

if __name__ == '__main__':
    app.run(debug=True)
