'''
Created on 2 oct. 2017

@author: Carlos Perez
@author: Miguel Canedo
'''

import unittest

from datetime import date, time
from calcularPrecio import calcularPrecio
from tarifa import Tarifa

'''

La clase ServiciosTest es utilizada para los casos de prueba unitarios, usando
el pluging PyUnit.

'''
class ServiciosTest(unittest.TestCase):
    def setUp(self):
        self.tarifa = Tarifa(1, 2)
        self.tarifa0 = Tarifa(0, 0)
        self.tarifaFlotante = Tarifa(0.5, 0.75)
            
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
        
    def testTarifaFlotanteConDosDecimales(self):
        fechaInicio = date(2017, 8, 8) # Domingo
        fechaFin = date(2017, 8, 9)    # Domingo
        tiempoInicio = time(12, 45)
        tiempoFin = time(11)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEqual(11.5, calcularPrecio(self.tarifaFlotante, tiempoDeServicio))
    
    def testErrorUnMinutoMasDeSieteDiasDeTrabajo(self):
        fechaInicio = date(2017, 8, 6) # Domingo
        fechaFin = date(2017, 8, 13)    # Domingo
        tiempoInicio = time(12, 45)
        tiempoFin = time(12, 46)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEqual(None, calcularPrecio(self.tarifa, tiempoDeServicio))

    def testErrorMenosDeQuinceMinutos(self):
        fechaInicio = date(2017, 8, 6) # Domingo
        fechaFin = date(2017, 8, 6)    # Domingo
        tiempoInicio = time(12)
        tiempoFin = time(12, 1)
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
        tiempoInicio = time(12, 59, 59)
        tiempoFin = time(12, 59, 59)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEqual(216, calcularPrecio(self.tarifa, tiempoDeServicio))
        
    def testLimitesDiasDeSemanaConFinDeSemanaEnMedio(self):
        fechaInicio = date(2017, 8, 6) # Domingo
        fechaFin = date(2017, 8, 12)    # Sabado
        tiempoInicio = time(12)
        tiempoFin = time(12)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEqual(168, calcularPrecio(self.tarifa, tiempoDeServicio))
        
    def testLimitesFinDeSemanaConDiasDeSemanaEnMedio(self):
        fechaInicio = date(2017, 8, 3) # Jueves
        fechaFin = date(2017, 8, 8)    # Martes
        tiempoInicio = time(12)
        tiempoFin = time(12)
        inicio = [fechaInicio, tiempoInicio]
        fin = [fechaFin, tiempoFin]
        tiempoDeServicio = [inicio, fin]
        
        self.assertEqual(168, calcularPrecio(self.tarifa, tiempoDeServicio))
    