# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

default eleccion = None

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

define i = Character("Itsuki")
image i normal = "itsuki serious"
image i smile = "itsuki smile"
image i smile2 = "itsuki smile2"
image i disgusted = "itsuki disgusted"
image i disgusted2 = "itsuki disgusted2"

define t = Character("Tsubame")
image t normal = "tsubame neutral"
image t normal2 = "tsubame neutral2"
image t serious = "tsubame serious"
image t serious2 = "tsubame serious2"
image t happy = "tsubame happy"
image t smile = "tsubame smile"
image t smile2 = "tsubame smile2"
image t talking = "tsubame talking"

define y = Character("Yuki")
image y happy = "yuki happy"
image y happy2 = "yuki happy2"
image y serious = "yuki serious"
image y serious2 = "yuki serious2"
image y smile = "yuki smile"


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
    "{i}{cps=4}¿Qué?{/cps}{i}{nw}"

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
    play sound "footsteps1.mp3"
    pause 3.0

    "{i}Ya llegué al trabajo{i}"

    scene bg interior7
    play music "Catwalk.ogg" fadein 1.0
    show maruo serious at center

    "{color=#e8f800ff}Miren quién se digno a llegar, ni un mensaje, carta, señal de humo... Nada para avisarnos que no venías ¿Tu te manejas cómo quieres?{/color}"
    "{color=#e8f800ff}Este es un trabajo serio, necesito responsabilidad o te vas{/color}"
    "Lo siento mucho Maruo, lo que paso es que..."

    menu:
        "¿Qué excusa puedo decirle?"
        "No encontré mi medicamento":
            "{i}El sabe que necesito mi medicación, lo entenderá{i}"
            jump medicamento_scene
        "Tuve que acompañar a mi hermana a la escuela":
            "{i}Yo le avisé que me hacía cargo de mi hermana, lo debe entender{i}"    
            jump verdad_scene
        "Me quedé dormido":
            "{i}Quizás la sinceridad sea lo mejor...{i}"
            jump verdad_scene

    label medicamento_scene:

        "{color=#e8f800ff}Bueno... La salud es importante{/color}"  
        "{color=#e8f800ff}Al menos dime que lo encontraste{/color}"   
        "Bueno, la verdad es que... no..."

        hide maruo serious
        show maruo happy at center

        "{color=#e8f800ff}Jajajaja... Ay qué voy a hacer contigo y tus excusas... Ponte a trabajar y luego lo resolvemos{/color}"

        hide maruo happy
        jump escena_comun2

    label verdad_scene:

        "{color=#e8f800ff}Es una irresponsabilidad hacía el trabajo, deberías apreciar esta oportunidad que te doy de trabajar en este restaurante, no tirarla a la basura{/color}"
        "{color=#e8f800ff}Vamos, ponte a trabajar y luego lo resolvemos{/color}"
        "Si, perdón, no volverá a suceder"

        hide maruo serious
        jump escena_comun2

    label escena_comun2:

        "{i}Bueno, eso podría haber salido peor, guardaré mis cosas a comenzar con el trabajo{i}"
        "{color=#9c7359ff}¡Por fin llegaste! Ayudame, no doy abasto{/color}"

        scene bg itsuki cg2
        with dissolve
        play music "Groovy Saturday.ogg" fadein 1.0

        "¡Itsuki! Disculpa que llegue tarde y te deje toda la apertura a ti, no volverá a pasar amiga"
        "{color=#9c7359ff}¿Está todo bien? Es la primera vez que te demoras tanto tiempo en llegar, normalmente incluso eres más puntual que yo{/color}"
        "{i}Conozco a Itsuki hace solo unos meses, pero se preocupa mucho, es buena persona{i}"
        "Si, está todo bien, solo que el despertador no sonó y tuve que llevar a mi hermana a la escuela, fue una mañana complicada"

        scene bg itsuki cg4

        "{color=#9c7359ff}Sé que te esfuerzas mucho por tu hermana. Además ya conoces al señor Maruo, a él lo único que le interesa es el restaurante{/color}"
        "{color=#9c7359ff}Nos va bien y tenemos una clientela fiel, y aun así él es súper estricto.{/color}"
        "Aun así… Creo que me empezaré a despertarme una hora antes, solo por precaución, no puedo perder el trabajo"

        scene bg itsuki cg3

        "{color=#9c7359ff}Jajaja No dejes que te afecte{/color}"
        "{color=#9c7359ff}Antes el señor Maruo era más amable, cuando ella todavía estaba aquí…{/color}"
        "¿Ella?"

        scene bg itsuki cg1

        "{color=#9c7359ff}Olvidalo, no es importante...{/color}"
        "{color=#9c7359ff}Debemos seguir trabajando o se enojará nuevamente{/color}"

        menu:
            "¿De qué está hablando?"
            "Ahora quiero saber, insistir":
                "Itsuki ahora ya hablaste, cuéntame rápido de qué estabas hablando"
                jump confesion_scene
            "Dejar pasar":
                "Es cierto, si no comienzo a trabajar Maruo me dejará en la calle, vamos a eso"
                jump escena_comun3

    label confesion_scene:
        scene bg interior7
        show itsuki maid serious at center
        stop music fadeout 25.5

        "{color=#9c7359ff}Cuando empecé a trabajar aquí hace un tiempo, había una chica que trabajaba antes de que me contrataran{/color}"
        "{color=#9c7359ff}No recuerdo su nombre, pero sí recuerdo que el señor Maruo era muy amable con ella. Él la consentía mucho, supongo que estaba enamorado de ella{/color}"
        "{color=#9c7359ff}Solo estuve con ella unas pocas semanas, hasta que dejo de venir al trabajo{/color}"

        scene bg interior7shadow
        hide itsuki maid serious
        show itsuki maid2 disgusted at center

        "{color=#9c7359ff}Me acuerdo que era muy linda, y muy gentil con todos. Muchos clientes solían venir en su horario de trabajo, porque querían ser atendidos por ella{/color}"
        "{color=#9c7359ff}Un día ella dejó de venir al trabajo, cuando le preguntamos al señor Maruo sobre ella, solo nos dijo que estaba enferma, y que no vendría por un tiempo{/color}"

        scene bg interior7
        show itsuki maid2 disgusted at center

        "{color=#9c7359ff}A partir de ese día, el empezó a actuar cada vez más cortante con los demás empleados, y con los clientes que venían por la chica{/color}"
        "{color=#9c7359ff}Pero en fin... Son cosas que pasan ¿no?"

        hide itsuki maid2 disgusted
        show itsuki maid happy

        "{color=#9c7359ff}En fin, trabajemos antes que Maruo se de cuenta que estamos solo charlando{/color}"
        "{i}¿Quién será esa chica? Qué extraño{i}"
        jump escena_comun3

        label escena_comun3:
            scene bg interior7
            with dissolve
            show itsuki maid happy2 at center
            play music "Catwalk.ogg" fadein 1.0

            "{color=#9c7359ff}¡A trabajar!{/color}"
            "{color=#9c7359ff}Vamos amigo, empieza por limpiar todos los utensilios que me quedaron, yo atenderé, tenemos muchos comensales hoy{/color}"

            hide itsuki maid happy2

            "{i}Y así comienza una nueva jornada laboral{i}"

            scene bg black
            with dissolve

            "{i}El día transcurrió tranquilamente, Maruo dejo de molestarme con mi llegada tarde{i}"
            "{i}Pero algo me dice que no lo dejará pasar tan fácilmente{i}"
            "{i}Finalmente llegó la hora de retirarme, Maruo ya no se encuentra en el restaurante y junto a Itsuki terminamos de limpiar y ordenar todo{i}"

            scene bg bar3
            with dissolve
            show itsuki maid2 smile2 at center

            "{color=#9c7359ff}Buen trabajo, nuestro turno ya está por terminar y llegan nuestros reemplazos{/color}"
            "{color=#9c7359ff}¿No tienes que ir a buscar a tu hermana a la escuela?{/color}"
            "Si, es cierto Itsuki, ya me voy, no quiero hacerla esperar mucho"

            hide itsuki maid2 smile2
            show itsuki maid2 smile at center

            "{color=#9c7359ff}Qué hermano responsable{/color}"
            "{color=#9c7359ff}Descansa, nos vemos mañana{/color}"
            "Hasta mañana Itsuki, cuidado al volver"

            hide itsuki maid2 smile

            "{i}Ahora si, paso a buscar a Nino y luego a descansar, fue un día agotador{i}"

            scene bg nightstreet
            with dissolve
            play music "callen.mp3" volume 0.6 fadein 0.7

            "{i}Ya no estoy muy lejos de la escuela de Nino, igual sabe que llego con un poco de demora, está esperando con la profesora{i}"
            "{i}Esa profesora realmente se preocupa por ella por suerte, tendremos que hacerle un regalo algún día{i}"
            "{i}Esa que veo desde lejos, es...{i}"
            "{i}¿Tsubame?{i}"

            show tsubame neutral2 at center

            "{color=#41beddff}Ho... Hola... Qué sorpresa encontrarte por aquí{/color}"

            play music "Lost in the Dessert.ogg" fadein 1.0

            "{i}Ella es Tsubame, vive cerca de nuestra casa, la conocía desde antes de mudarnos. Pero desde que regresamos nos hicimos demasiados cercanos. Demasiado cercanos…{i}"
            "{i}Tsubame me ha ayudado con Nino, y con la casa, creo que gracias a ella nos pudimos acomodar{i}"
            "{i}Es un milagro haberla conocido{i}"

            menu:
                "¿Cómo debería saludarla?"
                "Hola Tsubame ¿Qué haces por aquí sola?":
                    "Tsubame ¿Qué haces caminando por aquí? Ya está anocheciendo"
                    $ eleccion = "no_declararse"
                    jump tsubame_scene1
                "¡Qué suerte que nos encontramos!":
                    "Tsubame, qué suerte que nos encontramos ¿Cómo estás?"
                    jump tsubame_scene2

    label tsubame_scene1:
        show tsubame happy at center
        "{color=#41beddff}Solo estaba de paso por aquí, haciendo unas compras, ¿tu cómo estás?{/color}"
        "Siempre viendo el lado buenos a las adversidades"

        hide tsubame happy
        show tsubame smile at center

        "{color=#41beddff}Como siempre tan metaforico{/color}"
        "{color=#41beddff}¿Y cómo está Nino?{/color}"
        "Está bien, logró acostumbrarse al ritmo de la ciudad y al de su nueva escuela. Según ella, dice que sus compañeros son amables con ella, y la ayudan con lo que necesite"
        "{color=#41beddff}Es genial, me alegro de que se haya podido adaptar a la ciudad, sé que debe ser complicado mudarse de una ciudad a otra{/color}"
        "{i}Lo cierto es que estoy enamorado de Tsubame, pero no creo que sea el momento para declararme. Cuando sea el momento se lo diré, no quisiera que nuestra amistad se arruine ahora{i}"
        jump escena_comun4
    


    label tsubame_scene2:
        show tsubame happy at center
        "{color=#41beddff}¡Hola!{/color}"

        hide tsubame happy
        show tsubame talking at center

        "{color=#41beddff}A mi también me alegra verte pero ¿Por qué dices lo de la suerte?{/color}"
        "{i}Lo cierto es que estoy enamorado de Tsubame, pero no creo que sea el momento para declararme. Cuando sea el momento se lo diré, no quisiera que nuestra amistad se arruine ahora{i}"
        "Tsubame, hay algo de lo que quiero hablar. He estado pensando en nosotros últimamente, y siento que..."

        hide tsubame talking
        show tsubame neutral at center

        menu:
            "{i}¿Debería declararme?{i}"
            "Lo que siento por ti es más que amistad. Estoy enamorado de ti.":
                "{i}Al carajo, es repentino pero si no lo hago ahora jamás lo haré...{i}"
                $ eleccion = "declararse"
                jump tsubamesi_scene
            "No es momento":
                "{i}Es muy repentino, no quiero arruinar nuestra amistad ahora{i}"
                $ eleccion = "no_declararse"
                jump tsubameno_scene

    label tsubamesi_scene:
        "Tsubame, te amo, estoy enamorado de ti, realmente no tuve el mejor de los días, pero solo viéndote acercandote me cambio totalmente"

        hide tsubame serious
        show tsubame neutral2 at center

        "Sé que es repentino, pero siento que si no lo digo ahora no lo diré nunca, esto es algo que vengo aguantando desde hace tiempo"
        "{color=#41beddff}Vaya, esto es inesperado. No sé qué decir en este momento. Dame un minuto para procesarlo{/color}"

        hide tsubame neutral2
        show tsubame serious at center
        window hide(None)
        window auto
        pause 2.0

        hide tsubame serious
        show tsubame smile2 at center
        window hide(None)
        window auto
        pause 2.0

        hide tsubame smile2
        show tsubame happy at center

        "{color=#41beddff}No sabia que tenias esos sentimientos por mi…Si te soy sincera, tu tambien me gustas{/color}"
        "{color=#41beddff}Pensaba guardar estos sentimientos, ya que no quería que afectará a nuestra amistad{/color}"
        "Entonces qué dices ¿Te gustaría salir conmigo?"
        "{color=#41beddff}¡Si! Es muy repentino pero te amo... eso me da mucha vergüenza decirlo... Deberé acostumbrarme...{/color}"
        "Realmente este paso de ser un día más al mejor de mi vida en un segundo... Tsubame... Yo..."
        "{color=#41beddff}Dime, soy toda oidos{/color}"
        jump escena_comun4

    label tsubameno_scene:

        "Quería decirte que realmente aprecio todo lo que has hecho por mi, eres una de las personas más importantes que conozco, sé que es algo repentino, pero gracias por todo"
        
        hide tsubame neutral
        show tsubame smile at center

        "{color=#41beddff}Tu eres muy importante para mi también, quiero lo mejor para ti y tu hermana, no hace falta que me agradezcas{/color}"
        "{i}Dios, este momento podría ser ideal para declararme, aún no es muy tarde{i}"
        jump escena_comun4

    label escena_comun4:
        show tsubame happy at center
        play sound "phone.mp3"
        stop music

        "{i}Es mi telefono, mi hermana dice que van a cerrar ya la escuela, debo apurarme{i}"

        play music "callen.mp3" volume 0.6 fadein 0.7

        "¡Oh rayos! Me olvidé que tengo que ir a buscar a Nino a su escuela"
        hide tsubame happy
        show tsubame talking at center
        if eleccion == "declararse":
            hide tsubame talking
            show tsubame happy at center
            "{color=#41beddff}Ve, yo me quedo alegre con estos minutos, realmente me cambiaste la noche{/color}"
            "{color=#41beddff}Descansa, tengo un regalo guardado que pensaba darte en tu cumpleaños, pero ahora quiero que sea el primer regalo como tu novia, mañana te lo llevo{/color}"
            "No puedo esperar a saber que es"
            hide tsubame happy
            show tsubame neutral at center
        elif eleccion == "no_declararse":
            "{color=#41beddff}¡Si! Se está haciendo tarde, ve a buscarla, luego terminamos de hablar{/color}"    
        "Adiós Tsubame buenas noches. Iré a la escuela de Nino antes que se haga más tarde"

        hide tsubame talking
        show tsubame happy at center

        "{color=#41beddff}Buenas noches{/color}"

        hide tsubame happy

        "{i}A correr{i}"

        scene bg schoolnight
        with dissolve
        play music "Radiohead.ogg" fadein 1.0
        show nino ghappy at center

        "{color=#05f8af}¡Hermano!{/color}"
        "Nino, disculpa la demora"
        "{color=#05f8af}Descuida, unas amigas me estuvieron haciendo compañía hasta que tú llegaras{/color}"
        "Lo siento, me tope con Tsubame cuando salí del trabajo y nos pusimos a hablar"

        hide nino ghappy
        show nino vhappy at center

        "{color=#05f8af}Oh ya veo, ¿Qué tal está?{/color}"
        "Ella está bien, te contaré más en el camino, vámonos a casa, es bastante tarde"
        "{color=#05f8af}Si, vámonos, estoy cansada{/color}"

        hide nino vhappy
        scene bg otaku_room night
        with dissolve
        play music "Warmth.ogg" fadein 1.0 volume 0.7

        "{i}Por fin en la cama{i}"
        "{i}Sé que dormí hasta tarde, pero no dejo de ser un día agotador{i}"
        "{i}Tuve que correr todo el día{i}"
        if eleccion == "declararse":
            "{i}Aún así fue un gran día{i}"
            "{i}Aún no entra en mi cabeza que Tsubame y yo seamos... ¿Pareja?{i}"
            "{i}Y mañana va a traer un regalo{i}"
            "{i}Me muero de ansiedad por saber qué es{i}"
        elif eleccion == "no_declararse":
            "{i}Ver a Tsubame lo alegro un poco al menos, esa chica me vuelve loco{i}"
        "{i}Aún así lo que no puedo quitarme de la cabeza es, más ahora antes de dormir...{i}"

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
    "{i}Lo último que recuerdo de Yuki es...{i}"

    hide yuki_polaroid
    show yuki_polaroid2 at center
    stop music
    play sound "demon.mp3"
    show veinmask at center
    window hide(None)
    window auto
    pause 2.4

    hide yuki_polaroid2 
    hide veinmask 

    "{i}¿Qué?{i}"

    pause 3.0

    "{i}En fin, es hora de dormir{i}"
    "{i}Buenas noches{i}"     

    scene bg black
    with dissolve
    pause 2.0
    window hide(None)
    play sound "alarma.mp3"
    pause 2.8

    scene bg otaku_room
    with dissolve
    play music "Puzzles.ogg"

    "{i}Bueno se ve que hoy si funcionó la alarma{i}"
    "{i}Otro día llegando tarde, el señor Maruo no me lo iba a perdonar{i}"
    "{i}Es demasiado estricto a veces, y complicado de entender, pero creo que en el fondo lo hace porque se preocupa por nosotros y no solo por el restaurante como a veces pensamos{i}"
    "{i}Bueno, a prepararnos que empieza el día{i}"

    play sound "Zipper.ogg"
    pause 1.0

    if eleccion == "declararse":
            "{color=#05f8af}¡Hermano Tsubame está aqui!{/color}"
            "{i}Cierto, Tsubame dijo que iba a venir a traerme un regalo hoy{i}"
            "{i}Estoy tan ansioso por saber qué es y por verla...{i}"
            "¡Nino hazla pasar!"
            "{i}¡Qué nervios!{i}"

            show tsubame happy at center

            "Hola Tsubame buenos días ¿Cómo estás?"
            "{color=#41beddff}Hola... amor...{/color}"
            "{i}Tsubame me dijo amor, creo que voy a morir{i}"
            "{color=#41beddff}Cómo te prometí, te... traje tu regalo, quiero que sepas que es muy valioso para mi, al igual que tu...{/color}"

            hide tsubame happy
            hide bg otaku_room
            show bg tsubame cg
            with dissolve
            play music "Lost in the Dessert.ogg" fadein 1.0

            "{color=#41beddff}Quería traerte mi diario personal, sé que parece raro, sé que no es lo que esperabas, pero realmente te...{/color}"
            "{color=#41beddff}Te...{/color}"
            "{color=#41beddff}Te amo... así que quiero ir en serio contigo, si vamos a estar juntos quiero mostrarte quién soy realmente y no soy la mejor a veces con las palabras cara a cara pero si escritas{/color}"
            "{color=#41beddff}Así que aquí tienes mi ser, quién soy, quiero que lo leas y me conozcas por quién soy{/color}"
            "{i}Wow realmente no me esperaba esto, Tsubame es tan linda...{i}"
            "No sé qué decirte, me parece un regalo hermoso y estoy muy feliz que me des esta confianza ¿Estás segura que quieres darme tu diario así?"
            "{color=#41beddff}Si, todo lo que está ahí son mis pensamientos, gustos y quién soy, quiero que lo tengas, quizás incluso pueda ayudarte algún día, quién sabe{/color}"
            "Gracias... Mi amor..."

            show bg otaku_room
            with dissolve
            play music "Puzzles.ogg" fadein 1.5
            show tsubame happy:
                xalign 0.30
                yalign 1.0
            show nino talking:
                xalign 0.75
                yalign 1.0


            "{color=#05f8af}Oigan no me gusta interrumpirlos y no quiero, pero hermanito, ya se está haciendo tarde, tenemos que ir a la escuela y al trabajo{/color}"
            "Cierto, Tsubame, ven con nosotros, vives cerca de la escuela de Nino, puedo acompañarte"
            "{color=#41beddff}Me encantaría, vamos{/color}"

            hide tsubame happy
            hide nino talking

    elif eleccion == "no_declararse":
            "{i}¡A trabajar!{i}"
            

    show bg res11
    with dissolve
    play music "Catwalk.ogg" fadein 1.0

    show maruo serious at center

    "¡Hola señor Maruo! Ya estoy listo para comenzar a trabajar"
    "{color=#e8f800ff}Hola ¿Qué tal?{/color}"
    "{color=#e8f800ff}Para compensar tu llegada tarde de ayer necesito que hoy te quedes más tiempo, necesito que luego del cierre te quedes lavando los platos y terminando de acomodar todo, no abrimos hasta el lunes y va a haber un gran evento ese día{/color}"
    "{color=#e8f800ff}Por lo que necesito todo impecable, llama ya a tu hermana y avisale que no puedes ir a buscarla, volverás tarde{/color}"
    "{color=#e8f800ff}Y antes que preguntes, es más que una hora que es lo que tardaste ayer, así que si, será pago el tiempo extra{/color}"
    "{i}Realmente no tenía planes de trasnochar en el restaurante... Pero no queda de otra{i}"
    "Ok Maruo, lo haré"
    "{i}¡Con ganas! A comenzar{i}"

    scene bg black
    with dissolve
    hide maruo serious

    "{i}Y así pasaron las horas hasta que llegó el cierre{i}"
    "{i}Itsuki se quedo ayudandome un rato hasta que su familia comenzó a llamarla y debió irse{i}"
    "{i}Finalmente aquí estoy solo{i}"
    "{i}Maruo a veces puede ser demasiado estricto con sus empleados, si no hubiera mencionado que se pagaba extra ya me hubiera ido{i}"
    "{i}Y si no tuviera que cuidar a mi hermana y pagar mis pastillas...{i}"
    "{i}Que por cierto, hace dos días no tomo ahora que lo pienso...{i}"

    stop music
    play sound "am-radio-tuning.mp3"
    pause 6.0
    window hide(None)
    play music "To You Radio.mp3" fadein 0.4
    show bg bar3
    with dissolve


    "{i}¿Qué demonios es eso?{i}"
    "{i}¿Cómo esa radio se encendió sola?{i}"
    "{i}Y esa canción, me resulta tan familiar{i}"

    play sound "Chair.ogg"

    "{i}¿Algo se movió?{i}"
    "¿¡Qui... Quién anda ahí!?"

    window hide(None)
    pause 1.5

    "{i}Silencio absoluto...{i}"
    "{i}Quizás deba ir a revisar la cocina{i}"
    "{i}Recuerdo que Maruo tiene una vieja radio ahí{i}"

    "{i}Además... Un cuchillo para defenderme no vendría mal si es necesario{i}"

    play sound "Footsteps.ogg"

    "{i}Cada paso cuesta, estoy casi paralizado{i}"

    play sound "Footsteps.ogg"

    "{i}¿No sería mejor correr?{i}"

    play sound "Footsteps.ogg"

    "{i}No, debo enfrentar a quién sea que este ahí{i}"

    play sound "Footsteps.ogg"

    "{i}Y ahora yo...{i}"

    stop music
    play sound "radio.mp3"
    pause 3.0
    window hide(None)
    stop sound
    

    "{i}¿Qué?{i}"

    play sound "latido_corazon_rapido.mp3" loop volume 0.5

    "{i}Alguien ha apagado la radio y veo una sombra desde la puerta{i}"
    "{i}Estoy indefenso{i}"
    "{i}Este será mi final{i}"

    stop sound

    show yuki serious2 at center
    window hide(None)
    pause 1.5

    "{cps=4}Yu... Yu... Yuki...{/cps}{nw}"
    "{color=#d38bbdff}{cps=4}Hola...{/cps}{/color}{nw}"

    hide yuki serious2
    show bg black
    with dissolve

    "Esta ha sido la demo del juego"
    "¡Muchas gracias por haber jugado!"
    "Esperamos que les haya gustado y poder, pronto, tenerlos con nosotros jugando el primer capítulo completo"
    "¡Gracias!"
    
    
    




    



return