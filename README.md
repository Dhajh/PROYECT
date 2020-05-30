# Mapeo de los sismos captados en el país
  ### Programa para localizar los sismos captados en el país en la primera semana de junio del 2017
 ### Juan David Hernández Hernández
  ###### Facultad de Ingeniería Civil, Carretera Coquimatlán Kilómetro 9, Coquimatlán 28,400, Coquimatlán, Coli-ma, Juan David Hernández hernández, jhernandez14@ucol.mx
  **Resumen**

El siguiente proyecto resuelve la problemática de conocer la cantidad de sismos transcurridos en un periodo de 10 días y de esta forma conocer las zo-nas donde se dieron la mayor cantidad de sismos toda información recopilada sobre los sismos fue adquirirá de la página del servicio sismológico na-cional, el objetivo principal es fue realizar un análisis sísmico donde denotáramos las zonas donde hay más actividad sísmica en el país. Como resultados obtuvimos dos mapas prácticamente eran iguales solo que a uno de ellos se le fue adherida una fun-ción al código (custler) en el cual nos daba la canti-dad de sismos por zona
Palabras clave: Mapeo, Python, Folium, Csv, mapa.

 
**Abstract**
The project solves the problem of knowing the num-ber of earthquakes that have elapsed in a period of 10 days and, in this way, knowing the areas where the greatest number of earthquakes occurred. All the information collected on the earthquakes was ac-quired from the seismological service page. nation-al, the main objective is to carry out a seismic analy-sis where we denote the areas where there is more seismic activity in the country. As results we obtained two maps that were practically the same, except that one of them had a function attached to the code (custler) in which it gave us the number of earth-quakes per area.
Keywords: Python, Folium, Csv, map.
 
  **1. 	Introducción**
  
En nuestro estado es normal hablar de sismo, esto se debe a que una de las fallas tectónicas más conocidas y con mayor actividad rodea nuestras costas, además el estado cuenta con un imponente volcán que constantemente mues-tra actividad. Un sismo es un fenómeno natural ocasionado por el desplazamiento de las placas tectónicas y el mismo movimiento del magma que proviene desde el núcleo del planeta. La institución que se encarga de monitorear y de registrar este tipo de fenómenos es el Servicio Sismológico Nacional el cual genera una base de datos la cual muestra información de cada uno de los sismos que se manifiestan en todo el país, la información que muestra es la fecha, magnitud y localización de donde sucedió el sismo. Para nuestra área (Topografía) es muy importante mapear características de este tipo, afortunada y actualmente se cuentan con las herramientas necesarias para poder lograr un mapeo y poder plasmar la información que nos brinda el SSN (Servicio Sismológico Nacional) en un plano, la programación nos ofrece las herramientas necesarias para poder graficar dicha información infinidad de veces sin impor-tar la cantidad de datos que se tengan. En la antigüedad el proceso de graficar información era muy complicada pues el dibujar a mano grandes cantidades de información llevaba mu-cho tiempo, ahora cualquier individuo que cuen-te con un dispositivo móvil con internet puede consultar información gráfica de manera rápida y confiable. Esto se puede lograr gracias a los satélites que orbitan nuestro planeta los cuales realizan un proceso de geolocalización el cual se encarga de ubicar en el espacio algún punto. 
Ya es común no saber cómo llegar a una direc-ción y con solo consultar a un navegador llegar al lugar deseado.
Para este proyecto es necesario saber y mos-trar gráficamente en el mapa del país la canti-dad de sismos que se obtuvieron en 10 días, mostrando la localización, magnitud y fecha.




 
  **1.1. 	Ventajas de la Geolocalización.**
  
La geolocalización es una tecnología que cubre un gran número de fines, pero para este proyec-to la principal ventaja es mostrar los puntos de cada uno de los sismos captados en todo el país y como se mencionó anteriormente hace algunos años este proceso tardaba mucho tiempo y no se contaba con la precisión que hoy en día se tiene con ayuda de los satélites. Entonces al momento de querer presentar esta información gráficamente sólo se debe dispo-ner de algún dispositivo móvil e ingresar alguna dirección específica y comenzar a interactuar con esta maravillosa tecnología.

  **1.2. 	Programa por utilizar.**
El programa para utilizar es Spyder con Python 3.7.2, donde se escribió el código que solicita la base de datos .CSV y al mismo tiempo se corrió para poder ver los resultados en dos mapas uno tipo custler y otro sencillo ambos .html, presentando la ubicación, fecha y la magnitud de cada uno de los sismos captura-dos en esos 10 días (12-22 de junio del 2017). 
  **1.3. 	Folium**
Folium es una librería que facilita la visualización de información manipulada en Pyhton en un mapa interactivo. Para poder instalarlo fue ne-cesario instalar Jupyter y trabajar con el código en Notebook respetando el lenguaje de progra-mación Python. 
  **2. 	Desarrollo Experimental**
La finalidad del programa es que mediante una base de datos .CSV bajada del SSN (Servicio Sismológico Nacional) la cual contiene la canti-dad de sismos captados en 10 días en todo el país y que el programa con la librería folium muestre dos mapas, uno tipo custler y otro simple ambos .html, con dicha información de manera gráfica con el fin de que cualquier indi-viduo pueda comprender la información que contiene la base de datos. 
Primero importamos el módulo “pandas”. Este módulo se encarga de leer archivos como el siguiente. La variable “sismos” es un matriz que contiene la información leída de “sis-mo10dias.csv”

El segundo módulo que vamos a importar se llama “folium” y se encarga de crear los mapas. En la variable “mexico” contiene la información retornada de la función de folium.Map, los ar-gumentos de esta función ocupan la localiza-ción del mapa que vamos a crear y el zoom es que este va a tener.
 
Lo siguiente es un ciclo “for” que va a leer la matriz sismos que contiene la información de los sismos, “r” va hacer la variable utilizada adentro de nuestro for, por ende, esta va a con-tener los parámetros para nuestras variables.
La función iterrows sirve para iterar el data fra-me y que de esta forma nos retorne tuplas, para que nos retorne correctamente lo que queremos debemos indicarle la posición; en general la función iterrows sirve para retornar tanto índice como lista. 
Magnitud contiene la magnitud del sismo en cuestión.
Fecha contiene la fecha del sismo en cuestión.
Las siguientes líneas de código son condicio-nes que nos ayudaran a poner el color de cada marcador del mapa.
La variable llamada “col” es de tipo cadena y solo tendrá el nombre del color.
 
La variable info también es de tipo cadena y tendrá concatenada la magnitud y la fecha.
Folium.Marker es una función de folium que nos ayuda a poner marcadores, pondremos la lati-tud y longitud de cada sismo. En el popup se mostrará la cadena info y el icono tendrá el color correspondiente a la magnitud antes con-dicionada. Al final de la función se va adherir al mapa.
 
“Mexico.save” es la función que crea el HTML, en este caso llamada “map.html”.
 
Para el mapa tipo “custler” es básicamente lo mismo.
La función folium.MarkerCluster es el que crea esta modalidad de juntar geométricamente los marcadores. Es función ocupa una etiqueta y que sea adherida a nuestro mapa.
Todo sigue igual, pero en lugar de adherirle directamente los marcadores a nuestro mapa se los ponemos a la variable mapCluster, que es la variable utilizada para crear el cluster.
 
Pero a la hora de crear el HTML si será a nues-tro mapa mexico.

Código mapa tipo Cutler:
 
 https://github.com/Dhajh/PROYECT/blob/master/fotos/9.png
 

Código de mapa simple:
 

 

 

  **3. 	Manejo de datos.**
El proyecto manejó información del Servicio Sismológico Nacional.
  
  **3.1. 	Tipo de datos**

El tipo de datos que se manejan en el programa son:
•	Datos geoespaciales: los cuales son de tipo numéricos puesto que la base de datos maneja coordenadas, magnitud y fecha del sismo.
•	SIG: Un sistema de visualización geo-gráfica el cual plasma la información espacial en un plano. 

  **3.2. 	Sistema operativo.**

El programa esta diseñado para trabajar en el Sistema Operativo Windows y también una ver-sión de Python 3.0 o superior.

  **3.3. 	Equipo de prueba.**

El equipo en el que se realizó el programa fue una lenovo ideapad 110:
 
Figura 1.- Especificaciones del dispositivo.
 
Figura 2.- Especificaciones de Windows.

**4. 	Resultados**  
Cada código da como resultado un mapa .html, la diferencia que existe es que el mapa tipo Cutler muestra la cantidad de sismos en cada zona y eso nos sirve para realizar cálculos pos-teriores también muestra la descripción del pun-to, mientras que el otro código muestra un ma-pa más sencillo con un icono y color según la magnitud del sismo. Cada código primero lee el archivo Excel .CSV (Delimitado por comas) y después interpreta la información y lo plasma gráficamente, el mapa es interactivo por lo que el usuario puede darle ZOOM y ver más a deta-lle la localización del sismo. 
 

Figura 3.- Archivo CSV(delimitado por comas) descargado del SSN.
 
Figura 4.- mapa tipo custler
 
Figura 5.- descripción del punto en mapa tipo custler.
 
Figura 6.- Mapa sencillo creado con las coordenadas.
**5. 	Conclusiones.**
 
El programar con Python nos ofrece una flexibi-lidad a la hora de escribir el código, grandes programas han sido creados gracias a la misma flexibilidad, para este caso Python ayudó para la visualización correcta de la información.
El usuario puede observar con claridad a detalle la descripción de cada punto como se muestra en la siguiente imagen.
 
Figura 7.- descripción del punto.
Teniendo a la mano los dos mapas se realizó el análisis sísmico en el cual nos damos cuenta que en un total de 10 días se registraron un total de 207 sismos,  la zona donde se registró la mayor cantidad fue en la zona de Oaxaca, Chiapas  y que colinda con la frontera de Gua-temala, en esta zona se registraron un total de 176 sismos. La segunda zona con más sismos se encuentra entre los municipios de Colima y Michoacán con un total de 19 sismos y por último la zona donde se registró la menor canti-dad de eventos sísmicos fue en las dos Baja California. 
Esta metodología usada puede servir para apli-carlos en la sismología de la actualidad ya que hoy en día hay mayor monitoreo que los que se tenían en esa época, lamentablemente no se pudo obtener un archivo reciente para poder hacer el análisis multitemporal utilizando fechas distintas.
  **6. 	Referencias.**

•	García, j. (Agosto de 2017). Reseachgate. Obtenido de https://www.researchgate.net/publication/319654852_La_Geolocalizacion

•	Garcia, J.. (2015). Folium: utilizando Le-aflet con Python. 19/05/2020, de Map-pingGIS Sitio web: https://mappinggis.com/2018/10/folium-utilizando-leaflet-con-python
