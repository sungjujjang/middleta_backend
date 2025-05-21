from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_cors import CORS
import sqlite3, os, random, string, time, json, re, datetime, jwt
import settings.setting as setting
import utils.db.db as db
from utils.db.db import start_db
from utils.jwt import *

app = Flask(__name__)
app.config['SECRET_KEY'] = setting.SECRET_KEY

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)