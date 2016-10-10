# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora

@step(u'Dado que tengo el número "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_group1_y_group1(step, num1, num2):
    cal = Calculadora()
    world.resultado = str(cal.suma((num1),(num2)))

@step(u'cuando realizo la suma')
def cuando_realizo_la_suma(step):
    pass

@step(u'entonces el resultado que obtengo es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_group1(step, esperado):
    assert esperado==world.resultado, 'El resultado '+esperado+' no es el esperado.'
