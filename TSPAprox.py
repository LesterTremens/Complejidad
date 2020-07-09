import Vertice
import Grafo
from random import randint


grafica = Grafo.Grafo()


def creaGraficas(g,tamanio):
    for i in range(tamanio):
        g.agregarVertice(i)
    for i in range(tamanio):
        for x in range(tamanio):
            if i != x:
                g.agregarArista(i,x,randint(1,20))


    for v in g:
        for w in v.obtenerConexiones():
            print("( %s , %s , %s, %s )" % (v.obtenerId(), w.obtenerId(), w.obtenerPonderacion(v), v.obtenerPonderacion(w) ))

creaGraficas(grafica,4)
