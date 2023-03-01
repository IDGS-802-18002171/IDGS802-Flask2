from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,FormField,SelectField,RadioField,EmailField
from wtforms.fields import EmailField,TextAreaField,PasswordField
from wtforms import validators

class UserForm(Form):
    ingles=StringField('Ingles',[validators.DataRequired(message='Palabra requerida')])
    español=StringField('Español',[validators.DataRequired(message='Palabra requerida')])
class UserForm1(Form):
    busqueda=StringField('Buscar...',[validators.DataRequired(message='Palabra requerida')])
    radio = RadioField('Idioma a traducir', choices=[('E', 'Ingles'), ('I', 'Español')])