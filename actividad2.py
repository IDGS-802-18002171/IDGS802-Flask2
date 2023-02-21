from flask import Flask,render_template
from flask import request
import forms2

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def Home():
    num_form=forms2.UserForm(request.form)
    ingles=''
    español=''
    if request.method=='POST':
        ingles=num_form.ingles.data
        ingles=ingles.upper()
        español=num_form.español.data
        español=español.upper()
        f=open('diccionarioIngles.txt','a')
        f1=open('diccionarioEspañol.txt','a')
        f.write('\n'+'{} : {}'.format(ingles,español))
        f1.write('\n'+'{} : {}'.format(español,ingles))
        f1.close()
        f.close()
    return render_template("home1.html",form=num_form)
        

@app.route("/resultado",methods=["POST"])
def Resultado():
    num=request.form.get("txtCont")
    num=int(num)
    numMax=0
    numMin=int(request.form.get("numero{}".format(1)))
    numRange=0
    suma=0
    promedio=0
    lista = []
    lista1 = []
    cont=0
    for i in range(num):
        numRange=int(request.form.get("numero{}".format((i+1))))
        suma=suma+numRange
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
    promedio=(suma/num)
    num=len(lista2)
    return render_template("resultado1.html",num=num,numMax=numMax,numMin=numMin,lista1=lista2,suma=suma,promedio=promedio)

if __name__ == "__main__":
    app.run(debug=True,port=3000)