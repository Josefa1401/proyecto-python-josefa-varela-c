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

@app.route('/')
def paciente():
	cursor = mysql.get_db().cursor()
	sql = "SELECT * FROM paciente"
	cursor.execute(sql)

	pacientes_ = cursor.fetchall()
	return render_template("pacientes.html",paciente = pacientes_)

@app.route('/vacunas')
def vacunas():
	cursor = mysql.get_db().cursor()
	sql = "SELECT * FROM vacuna"
	cursor.execute(sql)

	vacuna_ = cursor.fetchall()
	return render_template("vacunas.html",vacuna = vacuna_)

@app.route('/recibe')
def recibe():
	cursor = mysql.get_db().cursor()
	cursor.execute("SELECT * FROM recibe")
	return jsonify(cursor.fetchall())

@app.route('/pacientes_ver',methods=["GET","POST"])
def paciente_vacuna():
	cursor = mysql.get_db().cursor()

	if request.method == "GET":
		rut_p = request.args.get('rut', default = "", type = str)

	sql = "SELECT * FROM recibe WHERE rut=%s"
	cursor.execute(sql,(rut_p))
	pavacuna_ = cursor.fetchall()
	return render_template("vacunas_paciente.html",vacunas = pavacuna_)

@app.route('/vacunas_ver',methods=["GET","POST"])
def listar():
	cursor = mysql.get_db().cursor()

	if request.method == "GET":
		nombre_e = request.args.get('nombre', default = "", type = str)

	sql = "SELECT * FROM recibe WHERE nombre_enfermedad=%s"
	cursor.execute(sql,(nombre_e))
	lavacuna_ = cursor.fetchall()
	return render_template("lista_vacuna_pacientes.html",vacunados = lavacuna_)

@app.route('/pacientes_agregar',methods=["GET","POST"])
def agregar_su_vacuna():
	cursor = mysql.get_db().cursor()

	if request.method == "POST":
		rut = request.form["rut"]
		nombre = request.form["vacuna"]
		sql = "INSERT INTO recibe VALUES(%s,%s,current_date)"
		cursor.execute(sql,(rut,nombre))

	if request.method == "GET":
		rut_p = request.args.get('rut', default = "", type = str)

	sql = "SELECT * FROM vacuna,paciente WHERE rut=%s"
	cursor.execute(sql,(rut_p))
	pavacuna_ = cursor.fetchall()
	return render_template("agregar_vacuna_paciente.html",datos = pavacuna_)

@app.route('/agregar_paciente',methods=["GET","POST"])
def agregar_p():
	cursor = mysql.get_db().cursor()

	if request.method == "POST":
		nombre = request.form["nombre"]
		rut = request.form["rut"]
		fecha = request.form["date"]
		sql = "INSERT INTO paciente VALUES(%s,%s,%s)"
		cursor.execute(sql,(rut,nombre,fecha))

	return render_template("agregar_paciente.html")

@app.route('/agregar_vacunas',methods=["GET","POST"])
def agregar_v():
	cursor = mysql.get_db().cursor()

	if request.method == "POST":
		enfermedad = request.form["enfermedad"]
		sql = "INSERT INTO vacuna VALUES(%s,current_date)"
		cursor.execute(sql,(enfermedad))

	return render_template("agregar_vacuna.html")


if __name__ == "__main__":
	app.run(debug=True)