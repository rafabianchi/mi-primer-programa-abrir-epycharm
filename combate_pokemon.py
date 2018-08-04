pokemon_elegido = input("¿contra que pokemon quieres combatir? (squirtle / charmander / bulbasar): ")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "squirtle":
    vida_enemigo = 90
    nombre_pokemon = "squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "charmander":
    vida_enemigo = 80
    nombre_pokemon = "charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "bulbasar":
    vida_enemigo = 100
    nombre_pokemon = "bulbasar"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿que ataque vamos a usar ? (chizpazo / bola voltio)")

    if ataque_elegido == "chizpaso":
        print("picahu a usado chizpaso , hace un ataque de 10 de daño")
        vida_enemigo -= 10
    elif ataque_elegido == "bola voltio":
        print("pikachu a usado bola voltio, hace un ataque de 12 de daño")
        vida_enemigo -= 12

    print("la vida del {} ahora es de {}".format(nombre_pokemon, vida_enemigo))
    print("{}te hace un ataque de {} daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("la vida de picachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("has ganado")
if vida_pikachu <= 0:
    print("has perdido")


print("el combate ha terminado")
