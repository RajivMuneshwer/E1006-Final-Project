# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def homePage():
    return render_template('index.html')

@app.route("/1006")
def Second_page():
    return render_template('secPage.html')

@app.route("/420")
def Third_page():
    return render_template('thirdPage.html')

#start the server
if __name__ == "__main__":
    app.run()