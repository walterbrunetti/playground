# Robotics readme
More info under each project readme.



## Arduino

### Analog ports:
En la práctica las entradas analógicas medirán valores entre 0V y 5V y serán comprendidas por la tarjeta como valores entre 0 y 1023 (1024 valores)
Ej:  señales de audio
Las entradas analógicas también pueden ser utilizadas como señales digitales, donde A0 equivale al pin 14 en la placa Uno.


### Digital ports
Las señales digitales solo tienen 2 estados, serán reconocidas como 1 o 0, todo o nada, alto o bajo (5V o 0V), como la luz de una habitación que esta encendida o apagada. Arduino Uno tiene 13 señales digitales que pueden funcionar como entrada o salida (definidas en el programa), o sea, leerá 5V o 0V, o entregará 5V o 0V. 


### Warning
Cuando el Arduino está conectado por usb al PC no es recomendable usar pines que tengan identificación de TX y RX, ya que estos corresponden al puerto que está siendo usado por el usb, así que tendrán comportamientos erráticos.


### Power supply
3,3V y 5V son salidas de voltaje desde la tarjeta, con ello podemos alimentar componentes externos. Podemos utilizar cualquier GND como negativo para alimentación. Por otra parte, Vin nos permite alimentar de forma externa la tarjeta Uno con voltajes de hasta 12V, la tarjeta trabaja con 5V y utiliza un regulador que permite esto.


Las formas convencionales de alimentar la tarjeta son, principalmente por el Usb que aparte de funcionar como alimentación nos permite monitorearla para hacer pruebas y por un Jack de alimentación, fundamentalmente para baterías de 9V.

