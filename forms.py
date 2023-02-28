from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, BooleanField
 

class AddPetForm(FlaskForm):

    name = StringField('Add Pet Name', validators=[validators.InputRequired()])
    species = StringField('Add Pet Species', validators=[validators.InputRequired(), validators.AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField('Add Pet Photo', validators=[validators.Optional(), validators.URL()])
    age = IntegerField('Enter Age', validators=[validators.Optional(), validators.NumberRange(min=0, max=30)])
    notes = StringField('Enter Notes')

class EditPetForm(FlaskForm):

    photo_url = StringField('Add Pet Photo', validators=[validators.Optional(), validators.URL()])
    notes = StringField('Enter Notes')
    available = BooleanField()