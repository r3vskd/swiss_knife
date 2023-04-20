import subprocess                                                                                                        
print('\x1b[33;92m'"                          _                    _          "'\x1b[0m')                                
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
menu_options = {                                                                                                           
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

def print_menu():                                                                                                             
    for key in menu_options.keys():                                                                                            
        print ([key], '\x1b[33;92m' '=>' '\x1b[0m', menu_options[key] )                                                       
                                                                                                                              
def option1():                                                                                                                 
     print('creando archivos y directorios......')                                                                            
     subprocess.run(["mkdir", "d1"])                                                                                          
     subprocess.run(["mkdir", "d2"])
     subprocess.run(["touch", "fi1", "fi2", "fi3", "fi4", "fi5"])
     subprocess.run(["cp", "fi1", "fi2", "fi3", "fi4", "fi5", "/home/re3v0x/Documents/files/d1"])
     subprocess.run(["cp", "fi1", "fi2", "fi3", "fi4", "fi5", "/home/re3v0x/Documents/files/d2"])
     print('tarea terminada... ')

def option2():                                                                                                                
      print('buscando el archivo mas pesado de d2 y el mas ligero de d1...')                                                  
      bash= "du -a d2 | sort -r -n | head -n 2"                                                                              
      open=subprocess.Popen(bash, shell=True)                                                                                 
      bash2= "du -a d1 | sort -r| head -n 2"                                                                                 
      open2=subprocess.Popen(bash2, shell=True)                                                                               
      open.wait()                                                                                                            
      open2.wait()                                                                                                           
      print('tarea terminada... ')                                                                                         
                                                                                                                             
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

if __name__=='__main__':    
    while(True):            
        print('\x1b[33;92m' '  ﮾ menu ﮾  ''\x1b[0m') # Estilo que le di para que sira como separador y le de estetica '\x1b[0m' eso solo le da color
        print("\t")     
        print_menu()    
        option = ''      los datos con ''
        try:
            option = int(input('[''\x1b[33;92m'' N.S''\x1b[0m'']' '==== ')) 
        except:
            print('')   
        if option == 1:   
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
