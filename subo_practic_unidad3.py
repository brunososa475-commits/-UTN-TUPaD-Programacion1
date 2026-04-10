''' TP integrador - Repetitivas- Condicionales y Secuenciales.  '''

#---------------------------------------#
'''Ejercicio 1— “Caja del Kiosco” '''
#---------------------------------------#
while True:
    nombre = input("Escriba su nombre: ")
    if nombre != "" and nombre.isalpha():
        break
    print("Error, escriba su nombre, sin espacios ni numeros")

while True:
    producto = input("Coloque la cantidad de productos a llevar: ")
    if producto.isdigit() and int (producto) >0:
        producto = int(producto)
        break
    print("Error, ingrese solo numeros enteros.")


total_sin_descuento = 0
total_con_descuento = 0
ahorro_total = 0

for i in range (producto):
    print(f"\nproducto {i+1}")
    
    while True:
        precio = input("Precio: ") #ingresas el precio del producto 
        if precio.isdigit(): # se validad que sea (.isdigit)
            precio = int(precio) # se pasa la variable precio a entero
            break
        print("Error, Ingrese numeros enteros")
    
    while True:
        descuento = input("Ingrese el descuento N/S: ").lower()
        if descuento == "s" or descuento == "n":
            break
        print("Error, ingrese solo las iniciales N/S")
        
        
        
    total_sin_descuento += precio #acumulaciones 
        
    if descuento == "s": #si el descuento es  s , se aplica en descuento del 10% 
        precio_final = precio * 0.9 
        ahorro = precio - precio_final
        ahorro_total += ahorro
            
    else: # sino el precio queda igual 
        precio_final = precio 
            
    total_con_descuento += precio_final 
        
promedio = total_con_descuento / producto
 
print(f"\nCliente: {nombre}")
print(f"total sin descuento: $  {total_sin_descuento}")
print(f"total con descuento: $ {total_con_descuento}")
print(f"ahorro total : $ {ahorro_total}")
print(f"Promedio por producto: $ {promedio}")

#---------------------------------------------------------#
'''Ejercicio 2  — “Acceso al Campus y Menú Seguro” '''
#---------------------------------------------------------#

intentos = 1

usuario = "alumno"

clave = "python123"

while intentos <4:
    print (f"Intentos: {intentos} /3")
    
    usuario_1 = input("Ingrese su usario: ")
    clave_1 = input("Ingrese su clave: ")
    
    if usuario_1 == usuario and clave_1 ==clave:
            print("Acceso concedido")
            opcion = 0
            while opcion !=4:
                print ("1 - Estado ") 
                print ("2 - Cambiar clave ")
                print ("3 - Mensaje ")
                print ("4 - Salir ")
                
                opcion = input ("Eliga una Opcion: ") 
                
                if not opcion.isdigit():
                    print("Error, Ingrese un numero valido")
                    continue
                opcion = int(opcion)
                
                if opcion < 1 or opcion > 4:
                    print("Error: opción fuera de rango.")
                
                elif opcion ==1:
                    print ("Inscripto.")
                    
                elif opcion == 2:
                    print("Cambiar clave.")
                    clave_2 = input("Ingrese su nueva clave: ")
                    if len(clave_2) > 5:
                        confirmar = input("Confirme la clave: ")
                        if clave_2 == confirmar:
                            clave = clave_2
                            print("Cambio su clave")
                        else:
                            print("Error: las claves no coinciden.")
                    else:
                        print("Error, tiene que tener minimo 6 caracteres.")
                            
                        
                elif opcion ==3:
                    print("Mensaje Motivacional ")
                    
                elif opcion ==4:
                    
                    print("Salir")
            break
    
      
    else:
        print("credenciales inválidas.")
        intentos +=1 
        if intentos ==4:
            print("Cuenta bloqueda")
            
#-----------------------------------------------------# 
'''Ejercicio 3 (Alta) — “Agenda de Turnos con 
Nombres (sin listas)” '''
#-----------------------------------------------------#        
       
lunes_4= ""
lunes_1= ""
lunes_2= ""
lunes_3= ""
martes_3= ""
martes_1= ""
martes_2= ""

opcion_1 = 0
while opcion_1 !=5:
    
    print ("1. Reservar turno ")
    print ("2. ancelar turno (por nombre) ")
    print ("3. Ver agenda del día ")
    print ("4. Ver resumen general ")
    print ("5. Cerrar sistema ")
    

    opcion_1 = input("Selecione una opcion: ")
    if not opcion_1.isdigit():
                    print("Error, Ingrese un numero valido")
                    continue
    opcion_1 = int(opcion_1)
    
    if opcion_1 < 1 or opcion_1 > 5:
        print("Error: opción fuera de rango.")
        
    if opcion_1 ==1:
        dia = input("Elegir dia de la reserva: 1 = lunes, 2= martes: ")
        if not dia.isdigit():
            print ("Error: ingrese un numero valido")
            continue
        dia = int(dia)
        
        if dia <1 or dia >2:
            print("Error: opción fuera de rango.")
            continue
        

        if dia == 1:
            print("Tu reserva es del dia lunes. ")
            
            while True: 
                nombre_paciente = input ("Ingrese su nombre: ")
                if nombre_paciente != "" and nombre_paciente.isalpha():
                    break
                else:
                    print ("Error, escriba el nombre sin espacios ni numeros. ")
            
            if (nombre_paciente != lunes_1 and nombre_paciente != lunes_2 and nombre_paciente != lunes_3 and nombre_paciente != lunes_4):
              
              if lunes_1 == "": 
                lunes_1 = nombre_paciente
                print(f"{nombre_paciente} Se agendo su turno el dia lunes 1")
                
              elif lunes_2 == "":
                lunes_2 = nombre_paciente
                print(f"{nombre_paciente} Se agendo su turno el dia lunes2")            
                
              elif lunes_3 == "":
                lunes_3 = nombre_paciente
                print(f"{nombre_paciente} Se agendo su turno el dia lunes 3")
                
              elif lunes_4 =="":
                lunes_4 = nombre_paciente
                print(f"{nombre_paciente} Se agendo su turno el dia lunes 4")
            
              else:
                print("Agenda del lunes llena. ")
            
            else:
                print ("Este paciente ya tiener turno el dia lunes. ")    
        
        else:
            while True:
                nombre_paciente = input("Ingrese su nombre: ")
                if nombre_paciente != "" and nombre_paciente.isalpha():
                    break
                else: 
                    print ("Error,  escriba el nombre sin espacios ni numeros. ")
            
            print("Tu reserva es el dia martes")
            
            
            if (nombre_paciente != martes_1 and nombre_paciente != martes_2 and nombre_paciente != martes_3):
                
              if martes_1 == "": 
                martes_1= nombre_paciente
                print(f"{nombre_paciente} Se agendo su turno el dia martes 1")
                
              elif martes_2 == "":
                martes_2= nombre_paciente
                print(f"{nombre_paciente} Se agendo su turno el dia martes 2")
                
             
              elif martes_3 == "":
                martes_3 = nombre_paciente
                print(f"{nombre_paciente} Se agendo su turno el dia martes 365")
            
              else: 
                print("Agenda del martes llena. ")
            
            else:
                print ("Este paciente ya tiener turno el dia martes. ")
    
    elif opcion_1 ==2:
        cancelar = input("Elige el dia del turno para cancelar: 1 lunes , 2 martes. ")
        if not cancelar.isdigit():
            print ("Error: ingrese un numero valido")
            continue
        cancelar = int(cancelar)
        
        if cancelar <1 or cancelar >2:
            print("Error: opción fuera de rango.")
            continue
        if cancelar ==1: 
            while True:
                nombre_paciente = input ("Ingrese su nombre: ")
                if nombre_paciente != "" and nombre_paciente.isalpha():
                    break
                else: 
                    print ("Error,  escriba el nombre sin espacios ni numeros. ")
                
            if nombre_paciente == lunes_1:
                lunes_1 = ""
                print (f"{nombre_paciente}Se cancelo su turno el dia, {lunes_1}")
            elif nombre_paciente == lunes_2:
                
                lunes_2 = ""
                print (f"{nombre_paciente}Se cancelo su turno el dia, {lunes_2}")
                
            elif nombre_paciente == lunes_3:
                lunes_3 = ""
                print (f"{nombre_paciente}Se cancelo su turno el dia, {lunes_3}")
                
            elif nombre_paciente == lunes_4:
                lunes_4 = ""
                print (f"{nombre_paciente}Se cancelo su turno el dia, {lunes_4}")
            
            else:
                print ("Usted no tiene turno agendado. ")

        else:
            while True:
                nombre_paciente = input("Ingrese su nombre: ")
                if nombre_paciente != "" and nombre_paciente.isalpha():
                    break
                else: 
                    print ("Error,  escriba el nombre sin espacios ni numeros. ")
            
            if nombre_paciente == martes_1:
                martes_1 = ""
                print (f"{nombre_paciente}Se cancelo su turno el dia, {martes_1}")
                
            elif nombre_paciente == martes_2:
                martes_2 = ""
                print (f"{nombre_paciente}Se cancelo su turno el dia, {martes_2}")
            elif nombre_paciente == martes_3:
                martes_3 = ""
                print (f"{nombre_paciente}Se cancelo su turno el dia, {martes_3}")
                
            else:
                print ("Usted no tiene turno agendado. ")
                
    elif opcion_1 ==3:
        print ("\nAgenda dia lunes")
        
        if lunes_1 == "" :
            print ("Turno 1 libre. ")
        else:
            print (f"Turno 1 {lunes_1} ")
    
        if lunes_2 =="":
            print ("Turno 2 libre. ")
        else:
            print (f"Turno 2 {lunes_2} ")
        
        if lunes_3 =="":
            print ("Turno 3 libre. ")
        else:
            print (f"Turno 3 {lunes_3} ")
        
        if lunes_4 =="":
            print ("Turno 4 libre. ")
        else:
            print (f"Turno 4 {lunes_4} ")


        print ("\nAgenda dia martes")
        
        
        if martes_1 == "" :
            print ("Turno 1 libre. ")
        else:
            print (f"Turno 1 {martes_1} ")
    
        if martes_2 =="":
            print ("Turno 2 libre. ")
        else:
            print (f"Turno 2 {martes_2} ")
        
        if martes_3 =="":
            print ("Turno 3 libre. ")
        else:
            print (f"Turno 3 {martes_3} ")

    elif opcion_1 ==4:
        lunes_turnos_libres = 0
        lunes_turnos_ocupados = 0
        martes_turno_libres = 0
        martes_turno_ocupados = 0
        
        if lunes_1 =="":
            lunes_turnos_libres +=1
        else:
            lunes_turnos_ocupados +=1
        
        if lunes_2 =="":
            lunes_turnos_libres +=1
        else:
            lunes_turnos_ocupados +=1
        
        if lunes_3 =="":
            lunes_turnos_libres +=1
        else:
            lunes_turnos_ocupados +=1
            
        if lunes_4 =="":
            lunes_turnos_libres +=1
        else:
            lunes_turnos_ocupados +=1
        
        if martes_1 == "":
            martes_turno_libres +=1 
        else:
            martes_turno_ocupados +=1
        
        if martes_2 == "":
            martes_turno_libres +=1 
        else:
            martes_turno_ocupados +=1
            
        if martes_3 == "":
            martes_turno_libres +=1 
        else:
            martes_turno_ocupados +=1    
        
       
        if lunes_turnos_ocupados < martes_turno_ocupados:
            print("Martes tiene mas turnos") 
            
        elif lunes_turnos_ocupados > martes_turno_ocupados:
            print ("Lunes tiene mas turnos")
        
        elif lunes_turnos_ocupados == martes_turno_ocupados:
                print ("Empate de turnos")    
            
            
        print (f"Lunes ocupado {lunes_turnos_ocupados}, libres {lunes_turnos_libres}")
        print (f"Martes ocupado {martes_turno_ocupados}, libres {martes_turno_libres} ")
    
# ---------------------------------------------- #
'''Ejercicio 4  — “Escape Room: La Bóveda” '''
# ---------------------------------------------- #

energia = 100 
tiempo = 12  
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 

while True:
    agente = input ("Ingresa su nombre: ")
    if agente != "" and agente.isalpha():
        break
    print ("Error,  escriba el nombre sin espacios ni numeros. ")  
              
forzar_cerradura = 0        
        
while tiempo >0 and energia >0 and cerraduras_abiertas <3:
    print ("Estado")
    print (f"energia {energia}")
    print (f"tiempo {tiempo}")
    print (f"candados abiertos {cerraduras_abiertas}")
    print (f"alarma {alarma}")
    print (f"codigo {codigo_parcial}")
    
    print ("----------------------------------")    
    print (" --MENU-- ")
    print ("Forzar cerradura")
    print ("Hackear panel")
    print ("Descansar")
    puntos = input("Selecione una opcion. ")
    if not puntos.isdigit():
        print("Error, Ingrese un numero valido")
        continue
    puntos = int(puntos)
          
          
    if puntos < 1 or puntos > 3:
        print("Error: opción fuera de rango.")
        continue      
        
       
        
    if puntos ==1: 
        forzar_cerradura +=1
        print("Costo: energia -20 , tiempo -2 ")
        energia = energia - 20 
        tiempo = tiempo - 2 
            
        if forzar_cerradura >= 3:
            alarma = True
            print ("Se activo la alarma. ")
            continue
                
            
    
        if energia <40: 
            print ("Riesgo de alarma")
                
            elegi_numero = input ("Seleccione un numero del 1/3")
            if not elegi_numero.isdigit():
                print("Error, Ingrese un numero valido")
                continue
            elegi_numero = int(elegi_numero)
                
            if elegi_numero < 1 or elegi_numero > 3:
                print("Error: opción fuera de rango.")
                continue
            
            if elegi_numero == 3:
                alarma = True
            
        if alarma == False:
            cerraduras_abiertas +=1
            print ("1 Cerradura abierta")        
            
    elif puntos ==2 :
        forzar_cerradura = 0
        
        print("Costo: energia -10 , tiempo -3 ")
        energia = energia - 10 
        tiempo = tiempo - 3 
        
        for i in range (4):
                codigo_parcial += "A"
                
        if len ( codigo_parcial) >=8 and cerraduras_abiertas <3:
            cerraduras_abiertas +=1
            print("Se abrio una cerradura automaticamente. ")
                    
    elif puntos ==3:
        forzar_cerradura = 0
        
        print ("Descansando ")
        tiempo -= 1
        energia += 15
        
        if energia >100:
            energia = 100
        
        if alarma == True:
            energia -=10
            
            
if cerraduras_abiertas == 3:
    print("🎉 VICTORIA: abriste la bóveda")

elif energia <= 0 or tiempo <= 0:
    print("💀 DERROTA: te quedaste sin energia o tiempo")

elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("🚨 DERROTA: la alarma bloqueó el sistema")
    
    

#------------------------------------------------#
'''Ejercicio 5  — “Escape Room:"La Arena del 
Gladiador"'''
#------------------------------------------------#
             
         
while True:
    gladiador = input("ingrese su nombre de luchador: ")
    if gladiador != "" and gladiador.isalpha():
        break
    print("Error, escriba su nombre sin espacios ni numeros")
    
    
vida_jugador = 100 
vida_enemigo = 100
pociones = 3
daño_jugador = 15
daño_enemigo = 12
turno_jugador = True
    
while vida_jugador >0 and vida_enemigo >0:
    print(f"{gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo})")
    
    
    print("-------------------------------------")
    print("Elige una ocpion: ")
    print("1- Ataque pesado")
    print("2- Rafagas veloz")
    print("3- Curacion")
    
    opciones = input("Eliga una opcion: ")
    if not opciones.isdigit():
        print("Error, elige una opcion valida. ")
        continue
    opciones = int(opciones)
    
    if opciones <1 or opciones >3:
        print("Error: opción fuera de rango.")
        continue
    
    if opciones ==1:
        if vida_enemigo <20:
            critico = daño_jugador * 1.5
            vida_enemigo -= critico
            
            print(f"Atacastes al enemigo con {critico} de daño. ")
        
        else:
            vida_enemigo -= daño_jugador
        
        
            
              
    elif opciones ==2:           
        
        for i in range (3):
            vida_enemigo -=5
            print ("Golpe conectado con 5 de daño. ")
            
    elif opciones ==3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            
            if vida_jugador > 100:
                vida_jugador = 100
                
            print(f"Te curaste 30 de vida. Vida actual: {vida_jugador}")
            print(f"Pociones restantes: {pociones}")

        else:
            print("No te quedan pociones ")
            
    
    
    vida_jugador -= daño_enemigo
    print(f"El enemigo te atacó por {daño_enemigo}")  

if vida_jugador > 0: 
    print (f"¡VICTORIA! {gladiador} has ganado la batalla.")  

elif vida_jugador <=0 :
     print (f"¡DERROTA! has caido en combate.")  