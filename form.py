from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    map_url = StringField('Cafe Location(Map URL)', validators=[DataRequired()])
    location = StringField('Cafe Location(City Name)', validators=[DataRequired()])
    toilet = StringField('Toilet Provided(True/False)', validators=[DataRequired()])
    wifi = StringField('WiFi Provided(True/False)', validators=[DataRequired()])
    socket = StringField('Socket Provided(True/False)', validators=[DataRequired()])
    submit = SubmitField('Submit')

