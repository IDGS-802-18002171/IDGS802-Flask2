from flask import Flask,render_template
from flask import request
import forms1

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def Home():
    num_form=forms1.UserForm(request.form)
    num=0
    if request.method=='POST' and (num_form.numero.data!=''):
        num=num_form.numero.data
        num=int(num)
    return render_template("home.html",form=num_form,num=num)
        

@app.route("/resultado",methods=["POST"])
def Resultado():
    num=request.form.get("txtCont")
    num=int(num)
    numMax=0
    numMin=int(request.form.get("numero{}".format(1)))
    numRange=0
    lista = []
    lista1 = []
    cont=0
    for i in range(num):
        numRange=int(request.form.get("numero{}".format((i+1))))
        lista.append(numRange)
        if numRange>numMax :
            numMax=numRange
        if numRange<numMin :
            numMin=numRange
    for i in range(num):
        numero_repetido = int(request.form.get("numero{}".format((i+1))))
        conteo = lista.count(numero_repetido)
        if(conteo>1) :
            lista1.append("El número {} aparece {} veces en la lista.".format(numero_repetido,conteo))
    lista2 = list(set(lista1))
    num=len(lista2)
    return render_template("resultado1.html",num=num,numMax=numMax,numMin=numMin,lista1=lista2)

if __name__ == "__main__":
    app.run(debug=True,port=3000)