from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime



#initialize app
app = Flask(__name__)

#Set configs
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initiate database object
db = SQLAlchemy(app)

#Create Marshmallow object
ma = Marshmallow(app)

#Create Database
class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(400), nullable = False)
    completed = db.Column(db.Boolean, nullable = False, default = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return self.id

#Create Schema
class TodoListSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'completed', 'date_created')

#Create instance of Schema
todolist_schema = TodoListSchema(many = False)
todolists_schema = TodoListSchema(many = True)

#Routes

@app.route('/todolist', methods = ["POST"])
def add_todo():
    try:
        name = request.json['name']
        description = request.json['description']

        new_todo = TodoList(name = name, description = description)

        db.session.add(new_todo)
        db.session.commit()
        return todolist_schema.jsonify(new_todo)
    
    except Exception as e:
        return jsonify({"Error" : "Wow that didn't work"}, e)
    

@app.route('/', methods = ["GET"])
def get_things():
    return jsonify({"msg" : "Hello from the get route"})

if __name__ == "__main__":
    app.run(debug = True)

