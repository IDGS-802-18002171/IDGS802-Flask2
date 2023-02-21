from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,FormField,SelectField,RadioField,EmailField
from wtforms.fields import EmailField,TextAreaField,PasswordField
from wtforms import validators

class UserForm(Form):
    matricula=StringField('Matricula',[validators.DataRequired(message='La Matricula es requerida')])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=5,max=15,message='Ingresa un valor maximo')])
    apaterno=StringField('Apaterno')
    amaterno=StringField('Amaterno')
    email=EmailField('Correo')
