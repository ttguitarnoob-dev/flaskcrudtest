from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

#Flask app initialize
app = Flask(__name__)

#Set configs
app.config['SQLALCHEMY_DATABASE_URI'] = "SQLITE:/// database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize dadabase object
db = SQLAlchemy(app)

#Create Marshmallow Object
ma = Marshmallow(app)

#Database Create
class TodoList(db.Model):
    id = db.Columns(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(400), nullable = False)
    completed = db.Column(db.Boolean, nullable = False, default = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return self.id
    
#Schema
class TodoListSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'completed', 'date_created')

# Create instance of Schema
todolist_schema = TodoListSchema(many = False)
todolists_schema = TodoListSchema(many = True)

#Routes
@app.route("/todolist", methods = ["POST"])
def add_todo():
    try:
        name = request.json['name']
        description = request.json['description']

        new_todo = TodoList(name = name, description = description)

        db.session.add(new_todo)
        db.session.commit()
        
        return todolist_schema.jsonify(new_todo)
    
    except Exception as e:
        return jsonify({"Error" : "Something Broked"})


if __name__ == "__main__":
    app.run(debug = True)