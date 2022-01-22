import subprocess                                                                                                        # importamos esta libreria que es la que hace que python pueda interpretar comandos nativos de bash (linux)
print('\x1b[33;92m'"                          _                    _          "'\x1b[0m')                                # esto \x1b[33;92m'"  "'\x1b[0m' es para darle color a las letras
print('\x1b[33;92m'"  _ __   __ ___   ____ _ (_) __ _    ___ _   _(_)______ _ "'\x1b[0m')                                
print('\x1b[33;92m'" | '_ \ / _` \ \ / / _` || |/ _` |  / __| | | | |_  / _` |"'\x1b[0m')
print('\x1b[33;92m'" | | | | (_| |\ V / (_| || | (_| |  \__ \ |_| | |/ / (_| |"'\x1b[0m')
print('\x1b[33;92m'" |_| |_|\__,_| \_/ \__,_|/ |\__,_|  |___/\__,_|_/___\__,_|"'\x1b[0m')
print('\x1b[33;92m'" |__/ "'\x1b[0m')
print('\x1b[33;92m'"               .:^                    .:^  "'\x1b[0m')
print('\x1b[33;92m'"              / / Credo por:         /   : "'\x1b[0m')
print('\x1b[33;92m'"  '`.        /;/  Miguel Edrick     /    / "'\x1b[0m')
print('\x1b[33;92m'"  \  \      /;/   Gener Ana Yahir  /    /  "'\x1b[0m')
print('\x1b[33;92m'"   \\ \    /;/                     /  ///   "'\x1b[0m')
print('\x1b[33;92m'"    \\ \  /;/                     /  ///    "'\x1b[0m')
print('\x1b[33;92m'"     \  \/_/____________________/    /     "'\x1b[0m')
print('\x1b[33;92m'"      `/                         \  /      "'\x1b[0m')
print('\x1b[33;92m'"      {  o              o  }'      /       "'\x1b[0m')
print('\x1b[33;92m'"       \_________________________/         "'\x1b[0m')
print('\x1b[33;92m'"  SELECCIONA UNA OPCION "'\x1b[0m')
print('                                                                     ')
menu_options = {                                                                                                           # creamos el objeto menu_options para que capture cada opcion
    1:' Crear 5 archivos y copiarlos a 2 directorios (D1 y D2)',
    2:' Buscar el archivo mas grande de d2 y el mas chico de d1',
    3:' Comparar los archivos de los 2 directorios d1 y d2' '\n' '\t' '(mostrar el mas actual de d1 y el mas antiguo de d2)',
    4:' Copiar el contenido de d1/fi1/ a d1/fi5/'  '\n' '\t' 'conservando el contenido de d1/fi1/',
    5:' Contar el numero de ocurrencias de las letras B o b ' '\n' '\t' 'dentro de d1/fi1/',
    6:' Cambiar los permisos de d1/fi1 a unicamente ejecucion',
    7:' Cambiar de propietario al archivo d2/fi2',
    8:' Cambiar de grupo al archivo d2/fi3',
    9:' Crear un script para cambiar el nombre del archivo d2/fi4',
    10:' Encriptar el archivo d2/fi5/',
    11:' Desencriptar el archivo d2/fi5',
    12:' Salir',
}

def print_menu():                                                                                                             # "def" es para crear funciones en python, en este caso nuestra funcion
    for key in menu_options.keys():                                                                                           # hace un ciclo "for" para que cada vez que metamos una opcion se muestre 
        print ([key], '\x1b[33;92m' '=>' '\x1b[0m', menu_options[key] )                                                       # esto: [ N.S]=> en la terminal, lo que dice [key]  es el iconito este
                                                                                                                              # [ N.S]
def option1():                                                                                                                # Aqui empezamos a simplemente crear las funciones que son las que 
     print('creando archivos y directorios......')                                                                            # hacen la instruccion en bash para modificar los archivos
     subprocess.run(["mkdir", "d1"])                                                                                          # esta cosa "subprocess.run" es para decirle: ejecuta este comando en bash.
     subprocess.run(["mkdir", "d2"])
     subprocess.run(["touch", "fi1", "fi2", "fi3", "fi4", "fi5"])
     subprocess.run(["cp", "fi1", "fi2", "fi3", "fi4", "fi5", "/home/re3v0x/Documents/files/d1"])
     subprocess.run(["cp", "fi1", "fi2", "fi3", "fi4", "fi5", "/home/re3v0x/Documents/files/d2"])
     print('tarea terminada... ')

def option2():                                                                                                               # a partir de aqui descubri que habia una forma mas facil de decirle 
      print('buscando el archivo mas pesado de d2 y el mas ligero de d1...')                                                 # que ejecute el comando en bash "bash" es el numbre que le puse a la 
      bash= "du -a d2 | sort -r -n | head -n 2"                                                                              # para que cargue el script, el script el lo que va adentro de las comillas
      open=subprocess.Popen(bash, shell=True)                                                                                # lo que dice "open y open 2" es para que inicie "bash" y 
      bash2= "du -a d1 | sort -r| head -n 2"                                                                                 # lo que dice "shell=True" es para que identifique que estoy trabjando con bash
      open2=subprocess.Popen(bash2, shell=True)                                                                              # el open.wait() es para decirle que para y pueda inciar la siguiente 
      open.wait()                                                                                                            # lo mismo con todas las demas, lo que va adentro de las comillas no
      open2.wait()                                                                                                           # se espanten, solo son los comandos de linux mkdir, para hacer carpetas
      print('tarea terminada... ')                                                                                          # find para buscar, sort, ordenar, head decirle que solo muestre la primera
                                                                                                                             # linea y asi, eso es lo de menos, son literal significados nada mas
def option3():
     print('buscando el archivo mas actual de d1 y el mas antiguo de d2...')
     bash= "find d1 -type f -printf '%T+ %p\n' | sort -r | head -n 1"
     open=subprocess.Popen(bash, shell=True)
     bash2= "find d2 -type f -printf '%T+ %p\n' | sort | head -n 1"
     open2=subprocess.Popen(bash2, shell=True)
     open.wait()
     open2.wait()
     print('tarea terminada... ')

def option4():
     print('pasando contenido de fi1 a fi5...')
     #bash= "cd /home/re3v0x/Documents/files/d1"
     #open=subprocess.Popen(bash, shell=True)
     bash2= "cat /home/re3v0x/Documents/files/d1/fi1 >> /home/re3v0x/Documents/files/d1/fi5"
     open2=subprocess.Popen(bash2, shell=True)
     #open.wait
     open2.wait()
     print('tarea terminada... ')

def option5():
     print('contando b y B......')
     bash= "grep B -o /home/re3v0x/Documents/files/d1/fi1 | wc -l "
     open=subprocess.Popen(bash, shell=True)
     bash2= "grep b -o /home/re3v0x/Documents/files/d1/fi1 | wc -l "
     open2=subprocess.Popen(bash2, shell=True)
     open.wait()
     open2.wait()
     print('tarea terminada... ')

def option6():
     print('asignando unicamente permisos de ejecucion......')
     bash= "sudo chmod -r-w+x fi1"
     open=subprocess.Popen(bash, shell=True)
     open.wait()
     print('tarea terminada... ')

def option7():
     print('cambiando de porpietario.......')
     bash= "sudo chown prueba /home/re3v0x/Documents/files/d2/fi2"
     open=subprocess.Popen(bash, shell=True)
     open.wait()
     print('tarea terminada... ')

def option8():
     print('cambiando de grupo...')
     bash= "sudo chgrp prueba2 /home/re3v0x/Documents/files/d2/fi3 "
     open=subprocess.Popen(bash, shell=True)
     open.wait()
     print('tarea terminada... ')

def option9():
     print('renombrando...')
     bash= "mv d2/fi4 d2/renombrado"
     open=subprocess.Popen(bash, shell=True)
     open.wait()
     print('tarea terminada... ')

def option10():
     print('enriptando.....')
     bash= "gpg -c d2/fi5 && rm -rfv d2/fi5"
     open=subprocess.Popen(bash, shell=True)
     #bash2= "rm -rfv d2/fi5.txt"
     #open2=subprocess.Popen(bash2, shell=True)
     open.wait()
     #open2.wait()
     print('tarea terminada... ')

def option11():
     print('desencriptando.......')
     bash= "gpg d2/fi5.gpg && rm -rfv d2/fi5.gpg"
     open=subprocess.Popen(bash, shell=True)
     open.wait()
     print('tarea terminada... ')

def option12():
     print('tarea terminada... ')

if __name__=='__main__':    # aqui creamos una condicion con if para que siempre sea verdadera por lo tanto siempre se ejecuta el codigo
    while(True):             # el while para que mientras sea real el la condicion del if se ejecute lo siguiente
        print('\x1b[33;92m' '  ﮾ menu ﮾  ''\x1b[0m') # Estilo que le di para que sira como separador y le de estetica '\x1b[0m' eso solo le da color
        print("\t")     # \t es una linea de espacio
        print_menu()    # se incia la funcion del menu
        option = ''     #se comienzan a capturar los datos con ''
        try:
            option = int(input('[''\x1b[33;92m'' N.S''\x1b[0m'']' '==== ')) # swk de swiss knife             #se le dice que la entrada de datos estara posterior al simbolito [ N.S] que le puse
        except:
            print('')   # si no ocurre ningun error, except se omite y try simplemente termina, pero si ocurre captura el error y lo muestra en pantalla
        if option == 1:    # si es ingresa 1 el usuario pos incia la funcion 1 y asi con el resto, si pone 2, la 2, etc...
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 8:
            option8()
        elif option == 9:
            option9()
        elif option == 10:
            option10()
        elif option == 11:
            option11()
        elif option == 12:
            print('Finalizando script... ')
            exit()
        else:
            print('Ingresa una opcion valida del 1 al 12')
