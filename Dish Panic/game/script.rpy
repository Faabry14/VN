# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define n = Character("Nino")
image n normal = "nino serious"
image n vhappy = "nino vhappy"
image n worried = "nino worried"
image n talking = "nino talking"
image n happy = "nino happy"
image n ghappy = "nino ghappy"



# El juego comienza aquí.

label start:
    scene bg blue_nebula_05 
    with dissolve
    play music "Nostalgic.ogg"  # Reproduce el audio de fondo "Nostalgic.ogg"

    "Me encuentro en la nada misma."
    "Por fin mi cabeza descansa un poco."
    "Esas malditas voces no están"
    "Solo soy yo, en el infinito, en la nada"
    "Pero creo que ya va siendo hora"
    "Este sueño acabará y el despertador va a sonar para comenzar otro día"
    "Al menos mañana llega mi día libre, es el último esfuerzo de la semana"
    "Pero eso significa que quizás... Pueda descansar un poco más..."
    stop music
    "{color=#05f8af}¡Hermanito! Despierta ya, es muy tarde.{/color}"
    "¿Qué?"

    scene bg otaku_room
    with dissolve
    show nino serious at center 

    "{color=#05f8af}Hermano ya se paso la hora, no sonó el despertador, tengo que ir a la escuela y tu al trabajo{/color}"
    play music "Radiohead.ogg"
    "Hola Nino... No me digas... Maldito celular... ¿Qué hora es? No puedo faltar al trabajo"




    return
