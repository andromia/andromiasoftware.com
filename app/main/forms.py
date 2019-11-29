from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length

class PostForm(FlaskForm):
    is_dev = BooleanField('Dev Post')
    text = TextAreaField('Type here', validators=[DataRequired()])
    # SelectField does not allow None
    project = SelectField(
        'Project',
        choices=[('None', 'No Project'), ('MDS', 'Model Design Studio'), ('TDR', 'The Duel Reloaded')],
        validators=[DataRequired()])
    submit = SubmitField('Submit')
