from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,FormField,SelectField,RadioField,EmailField
from wtforms.fields import EmailField,TextAreaField,PasswordField
from wtforms import validators

class UserForm(Form):
    ingles=StringField('Ingles',[validators.DataRequired(message='Palabra requerida')])
    español=StringField('Español',[validators.DataRequired(message='Palabra requerida')])
    busqueda=StringField('Buscar...',[validators.DataRequired(message='Palabra requerida')])
    