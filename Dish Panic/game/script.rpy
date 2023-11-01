# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define n = Character("Nino", what_youdo="jumpin")
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

    hide nino serious
    show nino talking at center

    "{color=#05f8af}Si... De hecho tendríamos que haber despertado hace 1 hora...{/color}"
    "¡No! Debo ir corriendo entonces, van a echarme si llego tan tarde sin siquiera avisar"

    hide nino talking
    show nino worried at center

    "{color=#05f8af}¡Vamos hermano!{/color}"
    "Dame un segundo, voy a cambiarme y ya salimos, no olvides tomar tu medicamento"
    "{color=#05f8af}¡Tu tampoco!{/color}"

    hide nino worried

    "Hay que apurarse"

    play sound "Zipper.ogg"

    "¡Vamos Nino!"
    "No va a pasar nada porque hoy no tome la medicación, no sé donde la guardé y no tengo tiempo para buscarla"
    "Ahora bien ¿Llegaré más rápido en subte o caminando? No sé cuánto tardará en llegar el subte y no tengo tiempo para esperar"

    menu:
        "¿Cómo vas a ir al trabajo?"
        "Caminando":
            "Caminando llegaré más rápido, la escuela de mi hermanita además queda en el camino"
            jump caminar_scene
        "En subte":
            "Caminando voy a tardar mucho, el subte es la opción más rápida, me arriesgaré a que tarde en llegar"    
            jump subte_scene

    label caminar_scene:
        "¡Vamos Nino!"

        scene bg kiosk2
        with dissolve
        show nino vhappy at center
        play music "Puzzles.ogg"

        "Ya casi llegamos a tu escuela hermana ¿Cómo te sientes?"
        "{color=#05f8af}Muy bien, me encanta cuando paseamos juntos{/color}"
        "Ay Nino, esto no es un paseo, estamos llegando 1 hora tarde a nuestras responsabilidades"

        hide nino vhappy
        show nino happy at center

        "{color=#05f8af}Más adrenalina al paseo{/color}"


        return


    label subte_scene:
        "Nino revisa en tu celular cuándo sale el próximo subte"
        "{color=#05f8af}¡En 15 minutos!{/color}"
        "Hay que correr, vamos"

        scene bg train
        with dissolve
        show nino talking at center
        play music "Puzzles.ogg"

        "Ya estamos cerca de la parada de tu colegio Nino, preparate"
        hide nino talking
        show nino worried at center
        "{color=#05f8af}Menos mal, el subte me hace marear un poco...{/color}"
        "Lo sé hermanita, ya casi estamos"

        return





    
    
    





    return
