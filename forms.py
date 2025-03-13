from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField,SubmitField, RadioField
from wtforms import validators

class UserForm(Form):

    mat = IntegerField("Matricula",[
        validators.DataRequired(message="El campo es requerido")
    ])
    nom = StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido")
    ])
    ap = StringField("Apellido",[
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo",[
        validators.DataRequired(message="El campo es requerido")
    ])

class ZodiacoForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido_paterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido_materno = StringField("Apellido Materno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    dia = IntegerField("Día", [
        validators.DataRequired(message="El campo es requerido"), validators.NumberRange(min=1, max=31, message="El día debe ser entre 1 y 31")
    ])
    mes = IntegerField("Mes", [
        validators.DataRequired(message="El campo es requerido"), validators.NumberRange(min=1, max=12, message="El mes debe ser entre 1 y 12")
    ])
    anio = IntegerField("Año", [
        validators.DataRequired(message="El campo es requerido")
    ])
    sexo = RadioField(
    "Sexo",
    choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")],
    validators=[validators.DataRequired()
    ])

