from flask import Flask, render_template, request, redirect
import requests
import pyshorteners
import requests as r

app = Flask(__name__)
@app.route('/')
def home():
    return "Working"
@app.route('/<query>')
def query(query):
    url = "https://url-shorten-api.vercel.app/?i="+query
    res = r.get(url).json()
    mainurl = res['main_link']
    return redirect(mainurl)
if __name__ == "__main__":
    app.run()