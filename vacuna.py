import requests
import json
from flask import Flask, render_template, jsonify, request
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors

app = Flask(__name__)
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_DB"]  = "vacunas"

mysql = MySQL(app)
mysql.connect_args["autocommit"] = True
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor

