from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class StoryForm(FlaskForm):
    # add invalid input messages
    title       = StringField('Post Title', [validators.Length(min=5, max=40), validators.InputRequired()])
    description = StringField('Post Description', [validators.Length(min=5, max=300), validators.InputRequired()])
    image       = StringField('Post Image', [validators.URL, validators.InputRequired()])
    author      = StringField('Story Author', [validators.Length(min=2, max=30)])
