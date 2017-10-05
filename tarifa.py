'''
Created on 2 oct. 2017

@author: Carlos Perez 13-11089
@author: Miguel Canedo 13-10214
'''

'''

La clase Tarifa es utilizada para guardar que costo tendra la hora
de hora de servicio segun si es dia de semana o fin de semana.

Esta clase trabaja principalmente en Bolivares, redondea toda cifra a 
2 decimales y revelara un error si los precios son negativos.

'''
class Tarifa:
    def __init__(self, habiles, finde):
        #Precondicion
        assert(habiles >= 0 and finde >= 0)
        
        self.habiles = round(habiles, 2)
        self.finde = round(finde, 2)