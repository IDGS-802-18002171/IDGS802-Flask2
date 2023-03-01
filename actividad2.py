from flask import Flask,render_template
from flask import request
from flask import make_response
from flask import flash
import forms2

app=Flask(__name__)
app.config['SECRET_KEY']="Esta es una clave encriptada"

@app.route("/",methods=["GET","POST"])
def Home():
    num_form=forms2.UserForm(request.form)
    num_form1=forms2.UserForm1(request.form)
    ingles=''
    español=''
    if request.method=='POST' and num_form.validate():
        ingles=num_form.ingles.data
        ingles=ingles.upper()
        español=num_form.español.data
        español=español.upper()
        f=open('diccionario.txt','r')
        contenido = f.read()
        lista={}
        lista2 = contenido.split('\n')
        for item in lista2:
            items=item.split(':')
            lista['{}'.format(items[0])]=items[1]
        if español in lista:
            success_message='Error ya se encontraba guardada esa palabra o clave'
            flash(success_message,category='error')
        else:
            f1=open('diccionario.txt','a')
            try:
                f1.write('\n'+'{}:{}'.format(español,ingles))
                success_message='Agregado de forma exitosa'
                flash(success_message,category='success')
            except:
                success_message='Error al agregar'
                flash(success_message,category='error')
            f1.close()
        f.close()
    return render_template("home1.html",form=num_form,form1=num_form1)
        

@app.route("/resultado",methods=["POST"])
def Resultado():
    num_form=forms2.UserForm(request.form)
    num_form1=forms2.UserForm1(request.form)
    if request.method=='POST' and num_form1.validate():
        idioma=num_form1.radio.data
        busqueda=num_form1.busqueda.data
        busqueda=busqueda.upper()
        f=open('diccionario.txt','r')
        contenido = f.read()
        lista={}
        lista1={}
        lista2 = contenido.split('\n')
        for item in lista2:
            items=item.split(':')
            lista['{}'.format(items[0])]=items[1]
        for item in lista2:
            items=item.split(':')
            lista1['{}'.format(items[1])]=items[0]
        f.close()
        if idioma=='E':
            try:
                traduccion=lista[busqueda]
            except:
                traduccion='No encontrada'
        elif idioma=='I':
            try:
                traduccion=lista1[busqueda]
            except:
                traduccion='No encontrada'
        if traduccion=='No encontrada':
            success_message=traduccion
            flash(success_message,category='error')
        else :
            success_message='El significado es: {}'.format(traduccion)
            flash(success_message,category='success')
    return render_template("home1.html",form=num_form,form1=num_form1)

if __name__ == "__main__":
    app.run(debug=True,port=3000)