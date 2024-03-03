from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired



class PokemonForm(FlaskForm):
    name_or_id = StringField('Name_or_id: ', validators=[DataRequired()])
    submit_btn = SubmitField('Search')

class BattleForm(FlaskForm):
    username = StringField('Name_or_id: ', validators=[DataRequired()])
    submit_btn = SubmitField('find opponent')