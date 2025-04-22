from flask import Flask
from flask import render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("panelhab.html")



if __name__ == '__main__':

    app.run("localhost","8000")