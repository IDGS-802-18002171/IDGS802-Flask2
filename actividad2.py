from flask import Flask,render_template
from flask import request
import forms2

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def Home():
    num_form=forms2.UserForm(request.form)
    ingles=''
    español=''
    if request.method=='POST' :
        ingles=num_form.ingles.data
        ingles=ingles.upper()
        español=num_form.español.data
        español=español.upper()
        f=open('diccionarioIngles.txt','a')
        f1=open('diccionarioEspañol.txt','a')
        f.write('\n'+'{}'.format(ingles))
        f1.write('\n'+'{}'.format(español))
        f1.close()
        f.close()
    return render_template("home1.html",form=num_form)
        

@app.route("/resultado",methods=["POST"])
def Resultado():
    num_form=forms2.UserForm(request.form)
    idioma=request.form.get("rdb")
    busqueda=num_form.busqueda.data
    busqueda=busqueda.upper()
    traduccion='No encontrada'
    cont=0
    f=open('diccionarioEspañol.txt','r')
    f1=open('diccionarioIngles.txt','r')
    contenido1 = f1.read()
    lista1 = contenido1.split('\n')
    contenido = f.read()
    lista = contenido.split('\n')
    f.close()
    f1.close()
    if idioma=='E':
        for item in lista :
            if busqueda==item :
                traduccion=lista1[cont]
            cont=cont+1
    cont=0
    if idioma=='I':
        for item in lista1 :
            if busqueda==item :
                traduccion=lista[cont]
            cont=cont+1
    return render_template("home1.html",form=num_form,traduccion=traduccion)

if __name__ == "__main__":
    app.run(debug=True,port=3000)