from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,FormField,SelectField,RadioField,EmailField
from wtforms.fields import EmailField,TextAreaField,PasswordField
from wtforms import validators

class UserForm(Form):
    combo1 = SelectField('Banda 1',[validators.DataRequired(message='Banda1 requerida')], choices=[('0', 'NEGRO'), ('1', 'MARRON'), ('2', 'ROJO'), ('3', 'NARANJA'), ('4', 'AMARILLO'), ('5', 'VERDE'), ('6', 'AZUL'), ('7', 'VIOLETA'), ('8', 'GRIS'), ('9', 'BLANCO')])
    combo2 = SelectField('Banda 2',[validators.DataRequired(message='Banda2 requerida')], choices=[('0', 'NEGRO'), ('1', 'MARRON'), ('2', 'ROJO'), ('3', 'NARANJA'), ('4', 'AMARILLO'), ('5', 'VERDE'), ('6', 'AZUL'), ('7', 'VIOLETA'), ('8', 'GRIS'), ('9', 'BLANCO')])
    combo3 = SelectField('Banda 3',[validators.DataRequired(message='Banda3 requerida')], choices=[('0', 'NEGRO'), ('1', 'MARRON'), ('2', 'ROJO'), ('3', 'NARANJA'), ('4', 'AMARILLO'), ('5', 'VERDE'), ('6', 'AZUL'), ('7', 'VIOLETA'), ('8', 'GRIS'), ('9', 'BLANCO')])
    radio = RadioField('Banda 4', choices=[('10', 'ORO'), ('11', 'PLATA')])