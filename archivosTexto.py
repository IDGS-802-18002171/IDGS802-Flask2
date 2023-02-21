f=open('alumnos3.txt','r')
'''nombres=f.read()
print(nombres)'''

#nombres2=f.readlines()
contenido = f.read()
lista = contenido.split('\n')
print(lista)
f.close()
'''for items in nombres2:
    print(items,end='')'''

'''f=open('alumnos.txt','w')
f.write('Hola mundo!!!!')
f.close()'''

'''alumno={'Matricula':12345,'Nombre': 'Mario','Apellidos':'Lopez','Correo':'charlyxbox360nuevo@gmail.com'}
lista=[]
cont=0
f=open('alumnos3.txt','a')
for i in alumno :
    lista.append(i)
    f.write('\n'+i)
    f.write('\n'+'{}'.format(alumno[i]))
f.close()'''