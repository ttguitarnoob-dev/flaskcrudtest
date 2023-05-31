from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



#initialize app
app = Flask(__name__)

#Set configs
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:/// database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initiate database object
db = SQLAlchemy(app)

#Create Database
class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(400), nullable = False)




if __name__ == "__main__":
    app.run(debug = True)

