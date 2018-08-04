



apetece_helado_input = input("¿te apetece un helado?" (Si/No)
tiene_dinero_input = input ("¿tiene dinero para un helado?") (Si/No)
esta_el_senor_helados_input = input ("esta el señor de los helados?")(Si/No)
esta_tu_tia_input = input = ("¿Estas con tu tia?")


apetece_helado = apetece_helado_input == "Si"
puede_permitirselo = tiene_dinero_input == "Si" or esta_tu_tia_input == "si"
esta_el_senor_helados = esta_el_senor_helados_input == "Si"




if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Pues comete un helado")


else:
    print ("pues nada")

