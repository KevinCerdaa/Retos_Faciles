'''
Reto #1: FIZZ BUZZ
 -- FÁCIL --
Crea un código que imprima los números del 1 al 100 (incluyendolos), pero si el programa encuentra número con las siguientes caracerísticas:
El número es multiplo de 3, imprime "fizz".
El número es multiplo de 5, imprime "buzz".
El número es multiplo de ambos, imprime "fizzbuzz".

      Ejemplo de salida:
      1
      2
      fizz
      4
      buzz
      [...]
      14
      fizzbuzz
'''

i = 1
while i < 101:
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz\n")
    elif i % 5 == 0:
        print("buzz\n")
    elif i % 3 == 0:
        print("fizz\n")
    else:
        print("{}\n".format(i))
    i += 1
