from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, EqualTo, Length




class TextForm(Form):
    method1 = TextField(
        'choice',
    )
    method2 = TextField(
        'choice',
    )