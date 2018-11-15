#Autor: Damián Iván García Ravelo
#Programa que contienen funciones para ejemplificar el uso de listas

def extraerPares(lista): #Función que elimina números que no sean pares

    nuevaLista=lista[:] #Copio la lista original a la nueva lista
    for x in nuevaLista: #Cda valor de la lista origina

        if nuevaLista== []: #Si la lista está vacía, la regresa igual
            return nuevaLista
        elif x%2 != 0: #Si la el valor % 2 no es 0
            nuevaLista.remove(x) #Elimina ese valor

    return nuevaLista #Regresa la nueva lista generada

def extraerMayoresPrevio(lista): #Función que inserta en una nueva lista el siguiente dato mayor
    nuevaLista=[]  #Comenzamos la nueva lista sin nada
    for x in range(len(lista)): #Visitamos la posición de cada dato
        if lista[x-1] < lista[x]: #Si el valor anterior es menor al siguiente valor
            nuevaLista.append(lista[x]) #En la nueva lista insertamos el "siguiente valor"
    return nuevaLista #Regresa la nueva lista generada

def intercambiarParejas(lista): #Función que intercambia las posiciones de los valores en una lista
    nuevaLista=[] #Comienza la nueva lista en 0
    if lista == []:
        return lista
    for x in range (len(lista)): #La x visita cada posición de la lista
        if x%2!=0: #Si posicióin del dato en la lista es impar
            nuevaLista.insert(x-1,lista[x]) #El valor anterior, lo pone una posición después
        else:
            nuevaLista.append(lista[x]) #Agrega el valor en las posiciones impares
    return nuevaLista #Regresa la lista

def intercambiarMM(lista):
    if lista==[]:
        return lista
    else:
        #Usamos las operaciones para obtener el valor máximo y el mínimo de la lista
        maximo = max(lista)
        minimo = min(lista)
        #Buscamos con las operaciones el índice de donde está ubicado cada valor
        posicionMaximo=lista.index(maximo)
        posicionMinimo=lista.index(minimo)
        #Intercambio de datos sin eliminar valores de la lista
        variableTemporal=lista[posicionMinimo] #Una variable va a recibir la posicion del mínimo
        lista[posicionMinimo]=lista[posicionMaximo] #La posición del mínimo estará en la posición del máximo
        lista[posicionMaximo]=variableTemporal #La posición del máximo estará en la posición de la variable que tiene la posición del mínimo

        return lista

def promediarCentro(lista): #Función que saca el promedio sin contar el valor máximo y mínimo
    if len(lista)==2 or len(lista)==1 or len(lista)==0: #Condición para que la lista sea mayor a 2 valores
        return 0
    else:
        #Buscamos los valores máximos
        maximo=max(lista)
        minimo=min(lista)

        dividendo= sum(lista) #Valor que se va a divir
        divisor=len(lista) #Valor que va a dividir
#promedio es igual a la suma total-los valores no deseados entre la longitud menos lca cantidad de datos no deseados
        promedio= (dividendo-maximo-minimo) // (divisor-2)
        return promedio #regresa el promedio

def calcularEstadistica(lista): #Función para calcular la desviación estandar de una lista
    media = sum(lista) / len(lista) #Primero se calcula la media

    if lista==[]: #Si la lista viene vacía
        return(0,0) #La dupla no puede contener nada
    else :
        diferenciaMedia=[] #De lo contrario generamos una nueva lista para obtener:
        for valor in lista:
            diferenciaMedia.append((valor-media)**2) #la sumatoria de cada valor-media al cuadrado
        desviacion=(sum(diferenciaMedia) / (len(lista)-1))**0.5 #la desviación es la  raíz de la suma total esas sumatorias entre la longitud de la lista
        return (media,desviacion) #me regersa la dupla




