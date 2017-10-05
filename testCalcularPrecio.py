'''
Created on 4 oct. 2017

@author: Mike
'''

import unittest

from datetime import date, time
from calcularPrecio import calcularPrecio
from tarifa import Tarifa

class ServiciosTest(unittest.TestCase):
    def setUp(self):
        self.tarifa = Tarifa(1, 2)
        self.tarifa0 = Tarifa(0, 0)
            
    def testMinTiempoDeTrabajoDiaDeSemana(self):
        fechaInicio = date(2017, 8, 8)
        fechaFin = date(2017, 8, 8)
        tiempoInicio = time(8)
        tiempoFin = time(8, 15, 0)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEquals(1, calcularPrecio(self.tarifa, tiempoDeServicio))
        
    def testMinTiempoDeTrabajoFinDeSemana(self):
        fechaInicio = date(2017, 8, 6)
        fechaFin = date(2017, 8, 6)
        tiempoInicio = time(8)
        tiempoFin = time(8, 15, 0)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEquals(2, calcularPrecio(self.tarifa, tiempoDeServicio))
                  
    def testTransicionDeFinDeSemanaADiaSemana(self):
        fechaInicio = date(2017, 8, 6) # Domingo
        fechaFin = date(2017, 8, 7)    # Lunes
        tiempoInicio = time(23, 45)
        tiempoFin = time(0)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEquals(2, calcularPrecio(self.tarifa, tiempoDeServicio))
        
    def testTransicionDeDiaSemanaAFinDeSemana(self):
        fechaInicio = date(2017, 8, 4) # Viernes
        fechaFin = date(2017, 8, 5)    # Sabado
        tiempoInicio = time(23, 45)
        tiempoFin = time(0)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEquals(1, calcularPrecio(self.tarifa, tiempoDeServicio))
        
    def testTarifaCero(self):
        fechaInicio = date(2017, 8, 6) # Domingo
        fechaFin = date(2017, 8, 8)    # Martes
        tiempoInicio = time(12, 45)
        tiempoFin = time(16)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEqual(0, calcularPrecio(self.tarifa0, tiempoDeServicio))
        
    def testErrorUnMinutoMasDeSieteDiasDeTrabajo(self):
        fechaInicio = date(2017, 8, 6) # Domingo
        fechaFin = date(2017, 8, 13)    # Domingo
        tiempoInicio = time(12, 45)
        tiempoFin = time(12, 46)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEqual(None, calcularPrecio(self.tarifa, tiempoDeServicio))

    def testErrorMasDeSieteDiasDeTrabajo(self):
        fechaInicio = date(2017, 8, 6) # Domingo
        fechaFin = date(2017, 8, 19)    # Sabado
        tiempoInicio = time(12, 45)
        tiempoFin = time(16)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEqual(None, calcularPrecio(self.tarifa, tiempoDeServicio))
    
    def testMaxCantidadHorasDeTrabajo(self):
        fechaInicio = date(2017, 8, 6) # Domingo
        fechaFin = date(2017, 8, 13)    # Domingo
        tiempoInicio = time(12, 45)
        tiempoFin = time(12, 45)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEqual(216, calcularPrecio(self.tarifa, tiempoDeServicio))