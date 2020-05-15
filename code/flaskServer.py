#!/usr/bin/python
#THis script creates a Flask server, and serves the index.html out of the templates folder.#It also creates an app route to be called via ajax from javascript in the index.html to query
#the database that is being written to by tempReader.py, and return the data as a json object.

#This was written for Joshua Simons's Embedded Linux Class at SUNY New Paltz 2020
#And is licenses under the MIT Software License

#Import libraries as needed
from flask import Flask, render_template, jsonify, Response
import sqlite3 as sql
import json
import os

#Globals
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('/index.html')

@app.route("/sqlData")
def chartData():
	con = sql.connect('log/sensorLog.db')
	cur = con.cursor()
	con.row_factory = sql.Row
	cur.execute("SELECT * FROM sensorLog")
	dataset = cur.fetchall()
	chartData = []
	for row in dataset:
		chartData.append({"Date": row[0], "Arm": row[1], "Trigger": row[2]})
	return Response(json.dumps(chartData), mimetype='application/json')

@app.route("/arm")
def arm():
	try:
		os.system('python3 sensor.py')
	except:
		print('error has occurred')

@app.route("/disarm")
def disarm():
	try:
		os.system('pkill -9 -f sensor.py')
		os.system('pkill -9 -f security.py')
	except:
		print('error has occurred')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=2020, debug=True)

