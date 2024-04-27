# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:13:16 2022

@author: usuario
"""
import random

def CodigosEncuestas():
    tupla=("Escriba CSAT para realizar una encuesta de Satisfaccion","Escriba BAWR para realizar una encuesta de Reconocimiento de Marca","Escriba PSUR para realizar una encuesta de Precios")
    print(tupla[0])
    print(tupla[1])
    print(tupla[2])
    
def Salto():
    tupla=("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(tupla)


def CodigosEncuestas2():
    tupla=("Escriba CSAT para visaulizar una encuesta de Satisfaccion","Escriba BAWR para visualizar una encuesta de Reconocimiento de Marca","Escriba PSUR para visualizar una encuesta de Precios")
    print(tupla[0])
    print(tupla[1])
    print(tupla[2])



def Decision():
    tupla=("Escriba BUSQUEDA para realizar una busqueda de una encuesta ya realizada con un CODIGO IDENTIFICADOR","Escriba VISUALIZAR para vizualizar TODAS las encuesta ya realizadas de un cliente en especifico","Escriba TERMINAR Para Finalizar el Programa")
    print(tupla[0])
    print(tupla[1])
    print(tupla[2])


      
def Quicksort(lista):
    if len(lista)<=1:
        return lista
    else:
        ListaMa=[]
        ListaMe=[]
        ListaIg=[]
        pivot=lista[0]
        for i in range(len(lista)):
            if lista[i] > pivot:
                ListaMa.append(lista[i])
            elif lista[i] < pivot:
                ListaMe.append(lista[i])
            else:
                ListaIg.append(lista[i])
        ListaMa= Quicksort(ListaMa)
        ListaMe= Quicksort(ListaMe)
        return ListaMa + ListaIg + ListaMe



def BusquedaCodigoCliente(ListaCodigoCliente):#BUSQUEDA BINARIA VISUALIZAR TODAS
    ResultadosBN= open("ResultadosSatisfaccionBN.txt","r")
    ResultadosBN=ResultadosBN.read()
    CodigoCliente=int(input("Ingrese el codigo de cliente que desea buscar: "))
    indice=-1   
    izq=0
    der=len(ListaCodigoCliente)-1
    while izq<=der:
        med=(izq+der)//2
        if ListaCodigoCliente[med]==CodigoCliente:
            indice=med
            break
        else:
            if CodigoCliente>ListaCodigoCliente[med]:
                izq=med+1
            else:
                der=med-1
    if indice==-1:
        print("No se encontro")
    else:
        print("Se encontraron las encuestas")
        print(ResultadosBN)
    
    """ResultadosBN.close() POR ALGUNA RAZON ESTE .CLOSE ME MANDA ERROR """
   
    

   
def BusquedaIdentificador(CodigoIdentificador):#BUSQUEDA SECUENCIAL VISUALIZAR 1 ENCUESTA EN ESPECIFICO
    indice=-1
    ResultadosBS= open("ResultadosSatisfaccionBS.txt","r")
    ResultadosBS=ResultadosBS.read()
    CodigoEncuesta=str(input("Escriba el codigo de encuesta: "))
    CodigoEncuesta=CodigoEncuesta.upper()
    CodigoCliente=int(input("Escriba el codigo de cliente: "))
    Random=int(input("Escriba el numero que aparecia al final de su codigo: "))
    n=str(CodigoEncuesta) +"-"+ str(CodigoCliente) +"-"+ str(Random)
    for i in range(0,len(CodigoIdentificador)):
        if CodigoIdentificador[i]==n:
            indice=i
            break
    if indice==-1:
        print("No se encontro")
    else:
        print("Se encontro en la encuesta")
        print(ResultadosBS)
        
    """ResultadosBS.close() POR ALGUNA RAZON ESTE .CLOSE ME MANDA ERROR"""
        



def EncuestaSatisfaccion(cantidad_encuestas,nombre_cliente,cod,codigo,CODIGOIDENTICADOR):
    RutaPreguntas=str(input("Escriba la ruta del archivo de las preguntas: ")) #Se escribe solo el nombre del archivo, el .txt se agrega automaticamente
    RutaPreguntas=str(RutaPreguntas)+".txt"
    preguntas= open(RutaPreguntas,"r")
    respuestas= open("Respuestas.txt","r")
    ResultadosBS= open("ResultadosSatisfaccionBS.txt","a")
    ResultadosBN= open("ResultadosSatisfaccionBN.txt","a")
    lista=[]
    lista2=[]
    Fechas=[]
    ResultadosBS.write(CODIGOIDENTICADOR+"\n")
    ResultadosBN.write(str(codigo)+"\n")
    respuesta=respuestas.read()
    for linea in preguntas:
        linea=linea.strip()
        lista.append(linea)
    lista.insert(5,"5(DIFICULTAD) ¿Como calificarias tu experiencia general con el producto?") 
    for i in range(0,cantidad_encuestas):
        for i in range(0,len(lista)-1):
            print(Quicksort(lista)[i])
            print(respuesta)
            n=str(input("Ingrese la opcion correspondiente: "))
            lista2.append(n)
    respuestas.close()    
    preguntas.close()
    lista=list(map(lambda line: line + "\n",lista))    #Esto agrega el \n al final de cada elemento de la lista
    lista2=list(map(lambda line: line + "\n",lista2))  #Esto agrega el \n al final de cada elemento de la lista
    for i in range(0,len(lista)-1):
        ResultadosBS.writelines((Quicksort(lista)[i]))
        ResultadosBS.writelines(lista2[i])
        ResultadosBN.writelines(Quicksort(lista)[i])
        ResultadosBN.writelines(lista2[i])
    dia=int(input("Ingrese el dia en el que se realizo esta encuesta: "))
    mes=int(input("Ingrese el mes en el que se realizo esta encuesta: "))
    año=int(input("Ingrese el año en el que se realizo esta encuesta: "))
    Fechas.append(nombre_cliente+"|"+str(dia)+"/"+str(mes)+"/"+str(año)+"\n")
    ResultadosBS.writelines(Fechas)
    ResultadosBN.writelines(Fechas)
    ResultadosBS.close()
    ResultadosBN.close()
    print("GUARDE ESTE CODIGO IDENTICADOR PARA BUSCAR SU ENCUESTA MAS ADELANTE",CODIGOIDENTICADOR)
    
    
    
        
def ReconocimientoMarca(cantidad_encuestas,nombre_cliente,cod,codigo,CODIGOIDENTICADOR):
    RutaPreguntas=str(input("Escriba la ruta del archivo de las preguntas: ")) #Se escribe solo el nombre del archivo, el .txt se agrega automaticamente
    RutaPreguntas=str(RutaPreguntas)+".txt"
    preguntas= open(RutaPreguntas,"r")
    respuestas= open("Respuestas.txt","r")
    ResultadosBS= open("ResultadosSatisfaccionBS.txt","a")
    ResultadosBN= open("ResultadosSatisfaccionBN.txt","a")
    lista=[]
    lista2=[]
    Fechas=[]
    ResultadosBS.write(CODIGOIDENTICADOR+"\n")
    ResultadosBN.write(str(codigo)+"\n")
    respuesta=respuestas.read()
    for linea in preguntas:
        linea=linea.strip()
        lista.append(linea)
    lista.insert(5,"5(DIFICULTAD) ¿Como calificarias tu experiencia general con el producto?") 
    for i in range(0,cantidad_encuestas):
        for i in range(0,len(lista)-1):
            print(Quicksort(lista)[i])
            print(respuesta)
            n=str(input("Ingrese la opcion correspondiente: "))
            lista2.append(n)
    respuestas.close()    
    preguntas.close()
    lista=list(map(lambda line: line + "\n",lista))    #Esto agrega el \n al final de cada elemento de la lista
    lista2=list(map(lambda line: line + "\n",lista2))  #Esto agrega el \n al final de cada elemento de la lista
    for i in range(0,len(lista)-1):
        ResultadosBS.writelines((Quicksort(lista)[i]))
        ResultadosBS.writelines(lista2[i])
        ResultadosBN.writelines(Quicksort(lista)[i])
        ResultadosBN.writelines(lista2[i])
    dia=int(input("Ingrese el dia en el que se realizo esta encuesta: "))
    mes=int(input("Ingrese el mes en el que se realizo esta encuesta: "))
    año=int(input("Ingrese el año en el que se realizo esta encuesta: "))
    Fechas.append(nombre_cliente+"|"+str(dia)+"/"+str(mes)+"/"+str(año)+"\n")
    ResultadosBS.writelines(Fechas)
    ResultadosBN.writelines(Fechas)
    ResultadosBS.close()
    ResultadosBN.close()
    print("GUARDE ESTE CODIGO IDENTICADOR PARA BUSCAR SU ENCUESTA MAS ADELANTE",CODIGOIDENTICADOR)
    
  
   
        
def EncuestaPrecios(cantidad_encuestas,nombre_cliente,cod,codigo,CODIGOIDENTICADOR):
    RutaPreguntas=str(input("Escriba la ruta del archivo de las preguntas: ")) #Se escribe solo el nombre del archivo, el .txt se agrega automaticamente
    RutaPreguntas=str(RutaPreguntas)+".txt"
    preguntas= open(RutaPreguntas,"r")
    respuestas= open("Respuestas.txt","r")
    ResultadosBS= open("ResultadosSatisfaccionBS.txt","a")
    ResultadosBN= open("ResultadosSatisfaccionBN.txt","a")
    lista=[]
    lista2=[]
    Fechas=[]
    ResultadosBS.write(CODIGOIDENTICADOR+"\n")
    ResultadosBN.write(str(codigo)+"\n")
    respuesta=respuestas.read()
    for linea in preguntas:
        linea=linea.strip()
        lista.append(linea)
    lista.insert(5,"5(DIFICULTAD) ¿Como calificarias tu experiencia general con el producto?") 
    for i in range(0,cantidad_encuestas):
        for i in range(0,len(lista)-1):
            print(Quicksort(lista)[i])
            print(respuesta)
            n=str(input("Ingrese la opcion correspondiente: "))
            lista2.append(n)
    respuestas.close()    
    preguntas.close()
    lista=list(map(lambda line: line + "\n",lista))    #Esto agrega el \n al final de cada elemento de la lista
    lista2=list(map(lambda line: line + "\n",lista2))  #Esto agrega el \n al final de cada elemento de la lista
    for i in range(0,len(lista)-1):
        ResultadosBS.writelines((Quicksort(lista)[i]))
        ResultadosBS.writelines(lista2[i])
        ResultadosBN.writelines(Quicksort(lista)[i])
        ResultadosBN.writelines(lista2[i])
    dia=int(input("Ingrese el dia en el que se realizo esta encuesta: "))
    mes=int(input("Ingrese el mes en el que se realizo esta encuesta: "))
    año=int(input("Ingrese el año en el que se realizo esta encuesta: "))
    Fechas.append(nombre_cliente+"|"+str(dia)+"/"+str(mes)+"/"+str(año)+"\n")
    ResultadosBS.writelines(Fechas)
    ResultadosBN.writelines(Fechas)
    ResultadosBS.close()
    ResultadosBN.close()
    print("GUARDE ESTE CODIGO IDENTICADOR PARA BUSCAR SU ENCUESTA MAS ADELANTE",CODIGOIDENTICADOR)
    
  
    
      
def main():
    ListaCodigoCliente=[]
    CodigoIdentificador=[]
    codigo=int(input("Ingrese el codigo de cliente: "))
    ListaCodigoCliente.append(codigo)
    nombre_cliente=str(input("Ingrese el nombre del cliente: "))
    CodigosEncuestas()
    cod=str(input("Ingrese el tipo de encuesta: "))
    cod=cod.upper()
    while cod!="NO":
        cantidad_encuestas=int(input("Ingrese la canitdad de encuestas: "))
        if cod=="CSAT":
            CODIGOIDENTICADOR=str(cod) +"-"+ str(codigo) +"-"+ str(random.randint(10000 , 20000))#el generador de codigo para realizar la busqueda secuencial
            CodigoIdentificador.append(CODIGOIDENTICADOR)
            EncuestaSatisfaccion(cantidad_encuestas,nombre_cliente,cod,codigo,CODIGOIDENTICADOR)
            Salto()
            print("Si desea realizar otra encuesta escriba el codigo correspondiente")
            CodigosEncuestas()
            print("Caso contrario escriba NO")
            cod=str(input("Escriba su respuesta: "))
            cod=cod.upper()  
            
        elif cod=="BAWR":
            CODIGOIDENTICADOR=str(cod) +"-"+ str(codigo) +"-"+ str(random.randint(10000 , 20000))#el generador de codigo para realizar la busqueda secuencial
            CodigoIdentificador.append(CODIGOIDENTICADOR)
            ReconocimientoMarca(cantidad_encuestas,nombre_cliente,cod,codigo,CODIGOIDENTICADOR)
            Salto()
            print("Si desea realizar otra encuesta escriba el codigo correspondiente")
            CodigosEncuestas()
            print("Caso contrario escriba NO")
            cod=str(input("Escriba su respuesta: "))
            cod=cod.upper()
               
        elif cod=="PSUR":
            CODIGOIDENTICADOR=str(cod) +"-"+ str(codigo) +"-"+ str(random.randint(10000 , 20000))#el generador de codigo para realizar la busqueda secuencial
            CodigoIdentificador.append(CODIGOIDENTICADOR)
            EncuestaPrecios(cantidad_encuestas,nombre_cliente,cod,codigo,CODIGOIDENTICADOR)
            Salto()
            print("Si desea realizar otra encuesta escriba el codigo correspondiente")
            CodigosEncuestas()
            print("Caso contrario escriba NO")
            cod=str(input("Escriba su respuesta: "))
            cod=cod.upper()
              
        else:
            print("Ha escrito un codigo incorrecto")
            CodigosEncuestas()
            cod=str(input("Escriba nuevamente su respuesta: "))
            cod=cod.upper()
    
    Salto()      
    print("¿Que desea realizar ahora?")
    Decision()
    decision=str(input("Ingrese la opcion que usted decida: "))
    decision=decision.upper()
    while decision!="TERMINAR":
        if decision=="VISUALIZAR":
            BusquedaCodigoCliente(ListaCodigoCliente)
            print("¿Desea realizar alguna operacion mas?")
            Decision()
            decision=str(input("Ingrese la opcion que usted decida: "))
            decision=decision.upper()
        
        elif decision=="BUSQUEDA":
            pass
            BusquedaIdentificador(CodigoIdentificador)
            print("¿Desea realizar alguna operacion mas?")
            Decision()
            decision=str(input("Ingrese la opcion que usted decida: "))
            decision=decision.upper()
        
        else:
            print("Ha selecciona una opcion erronea")
            Decision()
            decision=str(input("Ingrese nuevamente la opcion que usted decida: "))
            decision=decision.upper()
            
    print("Se ha finalizado el programa, Muchas gracias por usarlo")
    
    
main()