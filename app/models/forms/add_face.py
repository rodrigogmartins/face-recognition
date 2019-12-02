from flask_wtf import Form
from wtforms import StringField, FileField
from wtforms.validators import DataRequired, Email, Length

class AddFaceForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    image = FileField('Face Image', validators=[DataRequired()])
    submit = SubmitField('Add')
