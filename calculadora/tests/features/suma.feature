Feature: Suma de dos números.
  Yo como usuario de la app calculadora
  quiero realizar una suma de dos números
  para poder tener un resultado confiable.

  Scenario: Sumar 2 más 2.
    Dado que tengo el número "2" y "2"
    cuando realizo la suma
    entonces el resultado que obtengo es "4"

  Scenario: Sumar 3 más 4.
    Dado que tengo el número "3" y "4"
    cuando realizo la suma
    entonces el resultado que obtengo es "7"

  Scenario: Sumar  un error.
    Dado que tengo el número "tres" y "cuatro"
    cuando realizo la suma
    entonces el resultado que obtengo es "Error"
