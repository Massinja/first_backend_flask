import random
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {"admin": generate_password_hash("admin")}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route('/protected')
@auth.login_required
def index():
    return "Welcome, authenticated user"


song_list = ["Accidents Will Happen", "Adeste Fideles", "An Affair to Remember", "After You've Gone", "Ain't She Sweet",
             "Air For English Horn", "All Alone", "All By Myself", "All I Do Is Dream of You", "All I Need is the Girl",
             "All My Tomorrows", "All of Me", "All of You", "All or Nothing at All", "All the Way", "All the Way Home",
             "Almost Like Being in Love", "America the Beautiful", "And Then You Kissed Me",
             "Are You Lonesome Tonight?",
             "Aren't You Glad You're You?", "Baby, Won't You Please Come Home?"]


@app.route('/')
def random_songname():
    return random.choice(song_list)


@app.route('/birth_date')
def birth_date():
    return "December 12, 1915"


@app.route('/birth_city')
def birth_city():
    return "Hoboken, NJ"


@app.route('/wives')
def wives():
    return "Nancy Barbato, Ava Gardner, Mia Farrow, Barbara Marx"


@app.route('/picture')
def frankie_picture():
    return '<img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Frank_Sinatra_%2757.jpg" width=200>'


@app.route('/public')
def public_page():
    return "Everybody can see this page"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
