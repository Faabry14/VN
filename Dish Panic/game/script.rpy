# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define n = Character("Nino")
image n normal = "nino serious"
image n vhappy = "nino vhappy"
image n worried = "nino worried"
image n talking = "nino talking"
image n happy = "nino happy"
image n ghappy = "nino ghappy"

define m = Character("Maruo")
image m normal = "maruo serious"
image m happy = "maruo happy"
image m smile = "maruo smile"



# El juego comienza aquí.

label start:
    scene bg blue_nebula_05 
    with dissolve
    play music "Nostalgic.ogg"  # Reproduce el audio de fondo "Nostalgic.ogg"

    "{i}Me encuentro en la nada misma.{i}"
    "{i}Por fin mi cabeza descansa un poco.{i}"
    "{i}Esas malditas voces no están{i}"
    "{i}Solo soy yo, en el infinito, en la nada{i}"
    "{i}Pero creo que ya va siendo hora{i}"
    "{i}Este sueño acabará y el despertador va a sonar para comenzar otro día{i}"
    "{i}Al menos mañana llega mi día libre, es el último esfuerzo de la semana{i}"
    "{i}Pero eso significa que quizás... Pueda descansar un poco más...{i}"
    stop music
    "{color=#05f8af}¡Hermanito! Despierta ya, es muy tarde.{/color}"
    "{i}¿Qué?{i}"

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
    "{i}No va a pasar nada porque hoy no tome la medicación, no sé donde la guardé y no tengo tiempo para buscarla{i}"
    "{i}Ahora bien ¿Llegaré más rápido en subte o caminando? No sé cuánto tardará en llegar el subte y no tengo tiempo para esperar{i}"

    menu:
        "¿Cómo vas a ir al trabajo?"
        "Caminando":
            "{i}Caminando llegaré más rápido, la escuela de mi hermanita además queda en el camino{i}"
            jump caminar_scene
        "En subte":
            "{i}Caminando voy a tardar mucho, el subte es la opción más rápida, me arriesgaré a que tarde en llegar{i}"    
            jump subte_scene

    label caminar_scene:
        "¡Vamos Nino!"

        scene bg kiosk2
        with dissolve
        show nino vhappy at center
        play music "Puzzles.ogg" fadein 1.0

        "Ya casi llegamos a tu escuela hermana ¿Cómo te sientes?"
        "{color=#05f8af}Muy bien, me encanta cuando paseamos juntos{/color}"
        "Ay Nino, esto no es un paseo, estamos llegando 1 hora tarde a nuestras responsabilidades"

        hide nino vhappy
        show nino happy at center

        "{color=#05f8af}Más adrenalina al paseo{/color}"
        "{i}Lleve a mi hermana en su silla de ruedas a toda la velocidad que pude, ella parecía divertirse con la situación{i}"
        "{i}Disfruta mucho el tiempo conmigo{i}"
        "Ya casi estamos Nino, mucha suerte en tus clases de hoy, si te regañan por llegar tarde echame la culpa a mi"

        hide nino vhappy
        show nino ghappy at center

        "{color=#05f8af}Gracias hermano, saben que vivimos nosotros dos solos en la escuela, comprenden la situación{/color}"
        "{color=#05f8af}No te preocupes, mucha suerte para ti también en tu trabajo{/color}"
        "¡Adiós Nino!"

        hide nino ghappy

        "{i}Con esto dicho, a correr hacía mi trabajo, cuánto antes llegue seguro menos posibilidad de quedarme SIN trabajo{i}"


        jump escena_comun


    label subte_scene:
        "Nino revisa en tu celular cuándo sale el próximo subte"
        "{color=#05f8af}¡En 15 minutos!{/color}"
        "Hay que correr, vamos"
        "{color=#05f8af}¡Si! Lleguemos rápido!{/color}"

        scene bg train
        with dissolve
        show nino talking at center
        play music "Puzzles.ogg" fadein 1.0

        "Ya estamos cerca de la parada de tu colegio Nino, preparate"
        hide nino talking
        show nino worried at center
        "{color=#05f8af}Menos mal, el subte me hace marear un poco...{/color}"
        "Lo sé hermanita, ya casi estamos"

        scene bg kiosk2
        with dissolve
        hide nino worried
        show nino talking at center
    
        
        "Ya estamos a unos pocos metros ¿Estás mejor Nino?"
        "{color=#05f8af}Eso creo... Pero no te preocupes hermano, tu ve a tu trabajo tranquilo{/color}"
        "Si llega a pasar cualquier cosa, te sientes muy mal o algo, llamame o dile a tu profesora que me llame ¿ok?"
        "{color=#05f8af}Si, ya va a ir pasando, fue por el subte que siempre me marea, ve a trabajar que ya es muy tarde{/color}"
        "Si, adiós hermanita, mucha suerte"

        hide nino talking

        "{i}Aunque me preocupe que Nino se siente mal, debo correr al trabajo, confio en que me avisará cualquier cosa{i}"
        "{i}Por suerte trabajo bastante cerca, así que llegaré rápido{i}"

        jump escena_comun

    label escena_comun:

    scene bg res11
    with dissolve

    "{i}Ya casi estoy{i}"
    "{i}Mis compañeros ya empezaron su turno puedo verlos desde aquí comenzando a atender a los comensales"
    "{i}Espero que el señor Maruo no este de malhumor, si no, este va a ser mi último día en este restaurante{i}"
    "{i}Aunque aún no puedo quitarme de la cabeza...{i}"

    scene bg res11blur
    with dissolve
    play music "Warmth.ogg" fadein 1.0
    show yuki_polaroid at center

    "{i}Yuki... Mi amiga de toda la vida{i}"
    "{i}Yuki siempre se preocupo por mi y mi hermana, incluso ella fue quién se encargo de comprar la silla de ruedas de Nino tras la muerte de mi padre{i}"
    "{i}Recuerdo como consiguió un trabajo de medio tiempo para hacerlo luego de que se rompió su primer silla de ruedas{i}"
    "{i}Pero...{i}"
    "{i}Ella desapareció hace un año, esa es la razón por la que mi hermana y yo nos mudamos aquí hace dos meses{i}"
    "{i}Solíamos ir a la escuela juntos, tras terminarla yo me mudé junto a mi hermana a otra ciudad{i}"
    "{i}Vivimos un año allí hasta que nos llegó la noticia de que Yuki desapareció, por lo que quisimos volver a la ciudad y ayudar en su busqueda{i}"
    "{i}Pero claro, cada quién debe cumplir sus responsabilidades, y en el mientras tanto, yo debo trabajar para cuidar y pagar los estudios de Nino{i}"
    "{i}Una de las pocas cosas que me quedan de ella es esta foto{i}"
    "{i}Lo último que recuerdo de Yuki es{i}"

    hide yuki_polaroid
    show yuki_polaroid2 at center
    stop music
    play sound "demon.mp3"
    
    "{i}Yu... Yu... ¿Yuki?{i}"

    hide yuki_polaroid2
    scene bg res11

    "{i}Ya llegué al trabajo{i}"

    scene bg interior7
    play music "Catwalk.ogg" fadein 1.0
    show maruo serious at center

    "{color=#e8f800ff}Miren quién se digno a llegar, ni un mensaje, carta, señal de humo... Nada para avisarnos que no venías ¿Tu te manejas cómo quieres?{/color}"
    "{color=#e8f800ff}Este es un trabajo serio, necesito responsabilidad o te vas{/color}"




    return
