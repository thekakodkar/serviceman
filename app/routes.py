from app import app

@app.route('/')
@app.route('/index')
def index():
        user = {'username': 'Niraj'}
        return '''
    <html>
        <head>
            <title>ServiceMan</title>
        </head>
        <body>
            <h1>Moi, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''