from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():

    return 'Hello, World'
    
@app.route('/tentang')

def tentang():

    return 'Hai,adalah halaman tentang saya alfi sahrul'

if __name__ == '__main__':

    app.run(debug=True)