from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name: ')
    age = StringField('Age: ')
    tsh = StringField('TSH: ')
    t3 = StringField('T3:   ')
    tt4 = StringField('TT4: ')
    t4u = StringField('T4U: ')
    fti = StringField('FTI: ')
    submit = SubmitField('Submit')

class DelForm(FlaskForm):
    
    id_ = IntegerField('ID Number:')
    submit = SubmitField('Remove data')
