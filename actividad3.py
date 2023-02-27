from flask import Flask,render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash
import forms3

app=Flask(__name__)
app.config['SECRET_KEY']="Esta es una clave encriptada"
csrf=CSRFProtect()

@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'),404

@app.route("/",methods=["GET","POST"])
def Home():
    num_form=forms3.UserForm(request.form)
    datos=''
    if request.method=='POST' and num_form.validate():
        combo1=num_form.combo1.data
        combo2=num_form.combo2.data
        combo3=num_form.combo3.data
        radio=num_form.radio.data
        lista=['{}'.format(combo1),'{}'.format(combo2),'{}'.format(combo3),'{}'.format(radio)]
        valor='{}{}'.format(combo1,combo2)
        valor = valor.ljust((int(combo3)+2),'0')  # Agrega ceros a la derecha hasta que tenga 5 caracteres
        valor=int(valor)
        maximo=0
        minimo=0
        porcentaje=0
        if radio==10:
            porcentaje=.05
        else :
            porcentaje=.1
        cambiable=valor*porcentaje
        minimo=valor-cambiable
        maximo=valor+cambiable
        datos='{}@{}@{}@{}@{}@{}@{}'.format(combo1,combo2,combo3,radio,valor,minimo,maximo)
        success_message='Valor Final : {}'.format(valor)
        flash(success_message)
        response=make_response(render_template("home2.html",form=num_form,lista=lista,valor=valor,maximo=maximo,minimo=minimo))
    else :
        response=make_response(render_template("home2.html",form=num_form))
    response.set_cookie('datos_user',datos)
    return response
    
if __name__ == "__main__":
    app.run(debug=True,port=3000)