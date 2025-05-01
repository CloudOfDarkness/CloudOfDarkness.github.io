from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <body>
            <h1>Moi!</h1>
            <a href="/cookies">Super normal cookies</a>
        </body>
    </html>
    '''

@app.route('/cookies')
def cookies():
    return '''
    <html>
        <body>
            <h1>Cookies!</h1>
            <a href="/">Back</a>
            <a href="oak.hackstree.io/android/webview/pwn.html">Not back</a>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
