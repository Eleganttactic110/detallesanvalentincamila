import webbrowser
import os

# Contenido HTML con interactividad para San Valentín
html = """
<!DOCTYPE html>
<html>
<head>
    <title>San Valentín</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
        body { text-align: center; font-family: 'Dancing Script', cursive; margin: 0; padding: 20px; background-color: #000000; color: #FFFFFF; }
        .menu, .content { display: none; }
        .initial { cursor: pointer; margin-top: 50px; max-width: 200px; }
        .menu img { cursor: pointer; margin: 20px; max-width: 150px; }
        .content img { max-width: 500px; }
        .back-button { position: absolute; top: 20px; left: 120px; padding: 10px 20px; background-color: #ff6666; color: white; border: none; cursor: pointer; }
        .back-button:hover { background-color: #ff3333; }
        .roses { margin: 20px 0; max-width: 150px; } /* Tamaño reducido de la imagen de rosas */
        .acrostic-container { display: flex; justify-content: center; align-items: center; gap: 20px; margin-top: 20px; } /* Flexbox para alinear */
        .acrostic { font-size: 1.8em; text-align: center; } /* Alineado centrado */
        .message { margin-top: 20px; font-size: 1.5em; line-height: 1.5em; } /* Letras más grandes y separación entre líneas */
        .corner-decoration { position: fixed; width: 100px; } /* Agrandado a 100px */
        .top-left { top: 0; left: 0; }
        .top-right { top: 0; right: 0; }
        .bottom-left { bottom: 0; left: 0; }
        .bottom-right { bottom: 0; right: 0; }
        .letter { font-size: 1.6em; } /* Agrandar letras de la carta */
    </style>
    <script>
        function showMenu() {
            document.getElementById('initial').style.display = 'none';
            document.getElementById('menu').style.display = 'block';
        }

        function showContent(contentId) {
            document.getElementById('menu').style.display = 'none';
            var contents = document.getElementsByClassName('content');
            for (var i = 0; i < contents.length; i++) {
                contents[i].style.display = 'none';
            }
            document.getElementById(contentId).style.display = 'block';
        }

        function goBack() {
            var contents = document.getElementsByClassName('content');
            for (var i = 0; i < contents.length; i++) {
                contents[i].style.display = 'none';
            }
            document.getElementById('menu').style.display = 'block';
        }
    </script>
</head>
<body>
    <img src="https://media.tenor.com/keDRZSftqacAAAAM/sonia-felix-lan-valentin.gif" class="corner-decoration top-left">
    <img src="https://media.tenor.com/keDRZSftqacAAAAM/sonia-felix-lan-valentin.gif" class="corner-decoration top-right">
    <img src="https://media.tenor.com/keDRZSftqacAAAAM/sonia-felix-lan-valentin.gif" class="corner-decoration bottom-left">
    <img src="https://media.tenor.com/keDRZSftqacAAAAM/sonia-felix-lan-valentin.gif" class="corner-decoration bottom-right">

    <h1>Feliz San Valentín 💖</h1>
    <p class="message">Este detalle es para ti. Espero sea de tu agrado, eres la mujer mas hermosa y maravillosa del mundo. Haz clic en el corazon para comenzar.</p>
    
    <!-- Imagen inicial -->
    <img id="initial" class="initial" src="https://i.pinimg.com/originals/e6/7e/5d/e67e5d057fcda25f47f860c7be150e2f.gif" alt="Haz clic aquí" onclick="showMenu()">
    
    <p style="font-size: 1.5em;">🌹Desde el fondo de mi corazon espero sea de su agrado este pequeño detalle y sobre todo le pido a Dios por tu vida🌹</p>
    <p style="font-size: 1.5em;">🌹Que Dios siempre la bendiga a usted y su familia en todo, es maravillosa y se mrece lo mejor🌹</p>

    <!-- Menú de opciones -->
    <div id="menu" class="menu">
        <h1>Elige una opción:</h1>
        <p class="message">Espero algún día poder decirte lo importante que eres para mí en persona y lo maravillosa que eres🌹. Me encantaría invitarte a salir y disfrutar de tu compañía😍. Aquí tienes tres opciones con todo el cariño del mundo ☺. HAZ CLICK SOBRE LAS IMAGENES PARA VER EL CONTENIDO</p>
        <p class="message">📧La PRIMERA IMAGEN del SOBRE es una carta para ti📧</p>
        <p class="message">❤🎶La SEGUNDA IMAGEN del CORAZON CON AUDIFONOS es una canción que te la dedico❤🎶</p>
        <p class="message">🌹La TERCERA IMAGEN de la ROSA son una flores y un detalle sorpresa🌹</p>
        <img src="https://i.pinimg.com/736x/b3/4d/34/b34d342d4fd2082809e0d221c82dcef6.jpg" alt="Carta" onclick="showContent('content1')">
        <img src="https://media.istockphoto.com/id/1204367764/es/vector/ilustraci%C3%B3n-vectorial-de-personajes-de-coraz%C3%B3n-rojo-feliz-escuchando-m%C3%BAsica-en-auriculares.jpg?s=612x612&w=0&k=20&c=4ERXsSomQ9U5rgcSY9XnVbytacWRLOzJX7Kvp-znpnQ=" alt="Canción" onclick="showContent('content2')">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm2eMCnTU3rjWWuufh1abXHQqYTyDgsFPLXA&s" alt="Rosas" onclick="showContent('content3')">
    </div>
    
    <!-- Contenido 1: Carta -->
    <div id="content1" class="content">
        <button class="back-button" onclick="goBack()">Regresar</button>
        <h1>💌Carta💌</h1>
        <p class="letter">Querida Señorita Camila Cordero/Mi Brigadier🌹,</p>
        <p class="letter">Espero que este pequeño detalle le alegre su dia o noche y mis palabras y actos puedan llegar a su corazón, asi mismo espero pueda sacarle una sonrisa que alegre su vida al menos por el momento.😁🌹</p>
        <p class="letter">Mi Brigadier, es para mi muy bonito poder de cierta forma tenerla cerca y poder hablar con usted, le agradezco su tiempo, sus palabras y en si todo lo que ha hecho por mi siempre, si se pregunta que mas ha hecho por mi, dejeme decirle que su legado de respeto, valores y armonia que dejo en mi, lamentablemente nunca estuve bajo su mando pero me siento afortunado de al menos haber visto su forma correcta y amable de ser, llena de calidez con la que trataba a los demas, incluso aunque no me conocia me respondia los saludos, esos eran mis momentos felices en el que podia cruzar un "hola" con la chica mas hermosa del colegio, dejeme decirle que ese titulo nadie se lo va a quitar nunca de haber sido:🌹la mejor brigadier y la mas hermosa🌹, la verdad desde el primer momento en que la vi me enamore de usted ❤, disculpe que se lo diga asi directo mediante esta carta y no personalmente pero ya no puedo aguantar mas, han sido años para ser mas especificos 3 años en los que nunca pude decirle lo maravillosa y hermosa que es, lo talentosa y bondadosa que siempre ayuda a los demas. Usted es la mujer que no ha salido de mi mente ni de mi corazon desde hace años💖, soy conciente de que usted es 3 años mayor que yo y que por ende tiene una mayor madurez y criterio mas formado en base a sus experiencias, es por eso que no quiero decirle lo que siento solo con palabras si no también con actos que aunque soy un poco menor la puedo amar, igualmente quiero que sepa que la amo con todo mi corazon y que si le digo esto es porque al menos quiero confesar este sentimiento y 👀 ver que piensa usted al respecto 🤔 ya sea que me rechaze o no 🤔 aqui estare siempre para usted😁, el amor que siento por usted es algo que llevo aqui en mi pecho 💖 y en mi mente 🧠 se siente bien poder decirle lo que siento por usted despues de tantos años, lo que le pido con esta declaración/confesión es:</p>
        <p class="letter">🌹"Pedirle una oportunidad de conocerla y conquistarla, asi mismo de demostrarle que sin importar edad, distancia y diferencias podemos conocernos e inondicionalmente amarla y respetarla como se merece, podria darme esta oportunidad? Por favor"🌹</p>
        <p class="letter">Ya sea que me rechaze o acepte le prometo que me voy feliz sabiendo que le pude confesar que la amo y asi mismo sabiendo que esta bien y que no me equivoque cuando al verla a los ojos 👀 supe que llegaria muy lejos, perdon si soy imprudente o atrevido, le pido perdon, asi mismo no se si tiene novio o esta enamorada de alguien asi que disculpeme por favor si soy imprudente, caso contrario le pido que porfavor lo piense y al menos me permita invitarla 1 vez a salir aunque sea para despedirme, usted se merece ser feliz y respetare sea cual sea su decisión, en estos años nunca pude olvidarla yo la amo mi brigadier, no se si psicologicamente exista el amor a primera vista pero puedo prometerle que desde el primer momento que la vi yo me enamore de su belleza y de cada una de sus cualidades, por que usted es unica y una mujer que sea de buen corazón como usted es dificil encontrar y que sea tan maravillosa como usted ya no hay. Porfavor pienselo y gracias por leer esta larga carta.</p>
        <p class="letter">Con cariño, quien la quiere,admira y ama. Anthony.R</p>
        <img src="https://cdn.memegenerator.es/descargar/2077353" alt="Decoración">
    </div>
    
    <!-- Contenido 2: Cancion -->
    <div id="content2" class="content">
        <button class="back-button" onclick="goBack()">Regresar</button>
        <h1>❤🎶Cancion❤🎶</h1>
        <p class="letter">Mi estimada y querida Brigadier le dedico estas dos canciones que me recuerdan a usted, disculpe si no son lso ritmos que capaz le gusten pero le pido lea la siguiente descripción de cada canción y asi mismo si es posible las abra en una pestaña diferente por favor, gracias</p>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT31uK2uePjjSwP6XIZpd0zDZ7triTtNJMmJw&s" alt="Imagen relacionada con la canción">
        <p class="message">1.<a href="https://www.youtube.com/watch?v=r08d9XEik3s">Enlace a la canción</a></p>
        <p class="message">2.<a href="https://www.youtube.com/watch?v=bx9VFLCbWYw">Enlace a la canción</a></p>
        <p class="message">3.<a href="https://www.youtube.com/watch?v=bOzBA41J83A">Enlace a la canción</a></p>
        <p class="message">(1). Esta canción te la dedico porque eres única y siento que por fin encontré a la mujer más maravillosa del mundo después de tanto tiempo. Una mujer por la que vale la pena esperar y darle todo el amor y cariño que se merecer y ahcerla feliz incondicionalmente, apoandola en las buenas y en las malas</p>
        <p class="message">(2). Esta otra canción es de cierta forma como una cerenata y bueno me hace recordarla por cada palabra que dice usted esta en mi mente y si usted esta bien yo también me siento bien y que mi vida se lo entrego a usted.</p>
        <p class="message">(3). Esta canción es por si talvez no deseas darme una oportunidad por diversoso motivos o circunstancias, pero quiero que sepas que te esperare y se que algun dia volveras o al menos soñaré con ello, espero que no sea este el caso pero de todas formas te la dedico</p>
        <p class="message">Espero las canciones sean de su agrado</p>
        <p class="message">Disfrutelas!!</p>
    </div>
    
    <!-- Contenido 3: Rosas y Acróstico -->
    <div id="content3" class="content">
        <button class="back-button" onclick="goBack()">Regresar</button>
        <h1>🌹Rosas🌹</h1>
        <p class="message">Hice un pequeño acrostico con tu nombre, trate de describirla lo mejor posible, pero a una mujer con tantas cualidades es imposible describirla solo con palabras❤. Igualmente disculpeme por tomaruna foto suya pero debia hacerlo para con su belleza y personalidad plasmar en este detalle.</p>
        <div class="acrostic-container">
            <img src="https://i.pinimg.com/originals/3e/de/b3/3edeb39869d749cef1fbe1025347d2e0.gif" alt="Rosas" class="roses">
            <div class="acrostic">
                <p>C:arismática y encantadora, llena de vida todo lugar</p>
                <p>A:mable y siempre atenta, tiene un brillo unico y singular</p>
                <p>M:aravillosa en todos los sentidos</p>
                <p>I:nteligente y juiciosa, acelera mis latidos </p>
                <p>L:uminosa, ilumina mi vida con su sonrisa </p>
                <p>A:uténtica y única, como una calida brisa</p>
            </div>
            <img src="mi-imagen.jpg" alt="Decoración" class="roses" style="width: 250px; height: 350px;"> <!-- Imagen guardada localmente -->
        </div>
    </div>
</body>
</html>
"""

# Guarda el contenido en un archivo HTML con codificación UTF-8
with open("detalle_san_valentin.html", "w", encoding="utf-8") as file:
    file.write(html)

# Abre el archivo HTML en una nueva pestaña del navegador
webbrowser.open("file://" + os.path.realpath("detalle_san_valentin.html"))


