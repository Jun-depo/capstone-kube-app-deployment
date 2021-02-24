import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate ### Uncomment when migrate db
from hypothyroid import hypothyroid_pred
import logging
from flask.logging import create_logger

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

##### SQL DATABASE AND MODELS #####

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Migrate(app,db) ### Uncomment when migrate db

class Hypothyroid(db.Model):
    """ Input Params: 'name', 'age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI' """ 
    __tablename__ = 'data_table'
    id_ = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Text)
    tsh = db.Column(db.Text)
    t3 = db.Column(db.Text)
    tt4 = db.Column(db.Text)
    t4u = db.Column(db.Text)
    fti = db.Column(db.Text)

    def __init__(self,name, age, tsh, t3, tt4, t4u, fti):
        self.name = name
        self.age = agee
        self.tsh = tsh
        self.t3 = t3
        self.tt4 = tt4
        self.t4u = t4u
        self.fti = fti


    def input_data(self):
        
        input_values = {"Name": self.name, "Age": float(self.age), "TSH": float(self.tsh),
        "T3": float(self.t3), "TT4": float(self.tt4), "T4U": float(self.t4u), "FTI": float(self.fti)}
        return input_values

    def data_array(self):
        return [float(self.age), float(self.tsh), float(self.t3), float(self.tt4), float(self.t4u), float(self.fti)]


##### VIEWS WITH FORMS #####

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_data():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        tsh = form.tsh.data
        t3 = form.t3.data
        tt4 = form.tt4.data
        t4u = form.t4u.data
        fti = form.fti.data

        if name=="" or age=="" or tsh=="" or t3=="" or tt4=="" or t4u=="" or fti=="":  
            return render_template('add.html', form=form)

        else:
            new_data = Hypothyroid(name, age, tsh, t3, tt4, t4u, fti)
            db.session.add(new_data)
            db.session.commit()
            input_values = new_data.input_data()
            data_arr = new_data.data_array()
            predictions = hypothyroid_pred(data_arr)
            
            return render_template('result.html',input_values=input_values, \
                data_arr=data_arr, predictions=predictions)
    else:
        return render_template('add.html',form=form)

@app.route('/list')
def list_data():
    
    all_data = Hypothyroid.query.all()
    return render_template('list.html', all_data=all_data)

@app.route('/delete', methods=['GET', 'POST'])
def del_data():

    form = DelForm()
    if form.validate_on_submit():
        id_ = form.id_.data
        data_point = Hypothyroid.query.get(id_)

        db.session.delete(data_point)
        db.session.commit()

        return redirect(url_for('list_data'))
    return render_template('delete.html',form=form)


if __name__ == '__main__':
    LOG.info("Running http://127.0.0.1:8000 when use Docker")
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
    LOG.info("Running http://127.0.0.1:8000 when use Docker")