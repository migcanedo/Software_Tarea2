'''
Created on 2 oct. 2017

@author: Miguel Canedo 13-10214
@author: Carlos Perez 13-11089
'''
from datetime import date, time
from tarifa import Tarifa
from _datetime import timedelta

'''
Funcion que calcula el precio de un servicio de acuerdo a las horas de trabajo.
Si la tarifa es negativa, saltara un error y si el tiempoDeServicio es menor a 15
minutos o mayor a las horas equivalentes a siete dias de trabajo la funcion retornara
el valor None.

@param tarifa es un Obtejo Tarifa que representa el precio segun los dias en que se 
                trabajo (Dias de Semana o Fin de Semana).
@param tiempoDeServicio es una lista de listas que representa el dia y hora de inicio 
                y fin del servicio.
                
@result precio que tendra el servicio prestado.
'''
def calcularPrecio(tarifa, tiempoDeServicio):
    # Si los dias son iguales.
    if tiempoDeServicio[0][0] == tiempoDeServicio[1][0]:  
        # Se escoge la traifa segun el dia en que se trabajo.
        if tiempoDeServicio[0][0].weekday() < 5: 
            montoHora = tarifa.habiles
        else: 
            montoHora = tarifa.finde
        
        # Se calculan las horas trabajadas.
        trabajado = tiempoDeServicio[1][1].hour - tiempoDeServicio[0][1].hour 
        
        if trabajado == 0 and (tiempoDeServicio[1][1].minute - tiempoDeServicio[0][1].minute < 15):
            return None 
        
        # Se suma como 1 hora de trabajo mas si se paso por al menos un segundo.
        if tiempoDeServicio[1][1].minute > tiempoDeServicio[0][1].minute \
                or tiempoDeServicio[1][1].second > tiempoDeServicio[0][1].second: 
            trabajado += 1
            
        return trabajado*montoHora # Total a pagar
    
    # Cuando los dias son diferentes.
    else:
        # Se cuentan los dias de trabajo durante la semana y los dias de
        # trabajo durante el fin de semana.
        contador = tiempoDeServicio[0][0] + timedelta(1)
        diasSemana = 0
        diasFin = 0
        while contador != tiempoDeServicio[1][0]:
            if contador.weekday() < 5: 
                diasSemana += 1
            else:
                diasFin += 1
            contador += timedelta(1)
        
            
        # Elegimos la tarifa correspondiente al primer dia del servicio.
        if tiempoDeServicio[0][0].weekday() < 5:
            montoHoraDiaInicial = tarifa.habiles
        else:
            montoHoraDiaInicial = tarifa.finde
        
        # Elegimos la tarifa correspondiente al ultimo dia del servicio.
        if tiempoDeServicio[1][0].weekday() < 5:   
            montoHoraDiaFinal = tarifa.habiles
        else:
            montoHoraDiaFinal = tarifa.finde
        
        precioPrimerDia = (24 - tiempoDeServicio[0][1].hour)*montoHoraDiaInicial # Total a pagar por horas de servicio del primer dia.
        
        # Sumamos como 1 hora de trabajo mas si se paso por al menos un segundo.
        horasDiaFinal = tiempoDeServicio[1][1].hour 
        
    
        if tiempoDeServicio[0][1].hour == tiempoDeServicio[1][1].hour and \
                (tiempoDeServicio[1][1].minute > tiempoDeServicio[0][1].minute \
                    or tiempoDeServicio[1][1].second > tiempoDeServicio[0][1].second): 
            horasDiaFinal += 1
            
        precioUltimoDia = horasDiaFinal*montoHoraDiaFinal  ##Total a pagar por horas de sercios del ultimo dia.
        
        precioSemana = diasSemana*24*tarifa.habiles   # Total a pagar por las horas trabajadas durante la semana.
        precioFin = diasFin*24*tarifa.finde           # Total a pagar pir las horas trabajadas durante los fin de semana.
        
        if (diasFin + diasSemana + 1) >= 7 \
                and (diasSemana*24 + diasFin*24 + horasDiaFinal + (24 - tiempoDeServicio[0][1].hour)) > 168:
            return None
        
        
        return precioPrimerDia + precioSemana + precioFin + precioUltimoDia       # Total a pagar.

