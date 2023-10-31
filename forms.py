from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, DateField  
from wtforms.validators import DataRequired

class InfoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])
    sexo = RadioField('Sexo', choices=[('M','Masculino'),('F','Femenino')], validators=[DataRequired()])
    submit = SubmitField('Enviar')
