
# W-4000
W-4000 is a telepresence robot built with a Raspberry Pi, 2 DC motors and a controller.



## l298n:

Driver voltage:

Connect your motor supply voltage here, voltage between 5 and 35V DC (maximun). Remove 12V jumper if >12V DC.
if you're using between 7 and 12V DC to driver the motors (with 12V jumper in place), the module can also supply your Arduino (etc) with 5V DC. This is the third coso (V logic)
This module can be used to drive two DC motors at up to 2A each

```
Maximum Power	25W
Maximum Motor Supply Voltage	46V
Maximum Motor Supply Current	2A
Driver Voltage	5-35V
Driver Current	2A
```

He visto que lo alimentan con una bateria de las cuadras a 9v.

More info:
    - https://microcontrollerslab.com/dc-motor-l298n-driver-raspberry-pi-pico-tutorial/


## Arduino
Connecting DC motors with an Arduino.

https://www.instructables.com/How-to-Use-L298n-to-Control-Dc-Motor-With-Arduino/

http://circuitmagic.com/arduino/how-to-control-dc-motor-with-l298n-driver-and-arduino/

https://tronixstuff.com/2014/11/25/tutorial-l298n-dual-motor-controller-modules-and-arduino/


## Raspberry - safe voltage levels

The power management IC (PMIC, see section 3) is a MXL7704 with an input voltage range of 4.0 V to 5.5 V and an absolute maximum rating of 6 V that must not be exceeded.
The reasonable voltage range to power the Pi therefore is: 4.7 V to 5.25 V
Raspberry Pi 4 spec recommends a 3 A supply (15 W), with a minimum current of 2.5 A if downstream USB peripherals consume less than 500 mA in total.


Rasberry Pi pins map:
https://linuxhint.com/gpio-pinout-raspberry-pi/

How to use Python Lib:
https://www.ics.com/blog/control-raspberry-pi-gpio-pins-python

How to power the Raspberry Pi UPS (without a wire to the wall)
https://blog.330ohms.com/2021/09/03/como-hacer-una-raspberry-pi-portatil/





## Pila / battery recargable LCR 18650 Motoma de 2600mAh - 3.7Vcc
¡IMPORTANTE! “NO” CARGAR ESTAS PILAS CON NINGÚN CARGADOR EN LA CUAL EL VOLTAJE DE CARGA EXCEDA LOS 4.2V, DADO QUE LAS MISMAS, AL NO TENER CIRCUITO DE PROTECCION DE CARGA INCLUIDO, SE CORTARÁN Y DE NINGUNA MANERA SE RECONOCERÁ LA GARANTÍA.
COMPOSICIÓN:
- De Litio-Ion


## Modulo Energia Para Raspberry Pi 3b 4b Ups Pro 18650 Hat
- Instale la batería primero y luego conecte el UPS Al Raspberry Pi.
- La luz LED iluminada puede mostrar rápidamente la potencia restante y soportar la descarga mientras se carga. Puede conectarse directamente a la fuente de alimentación externa para cargar. Al mismo tiempo, el Raspberry Pi no se apagará.
- Las baterias se cargan desde el USB C de costado. Yo lo hice desde la compu.
- DO NOT PLUG Power supply to Raspberry Pi in USB-C port during Using UPS, it may damage UPS!!!!


Mas info: 
    - https://es.aliexpress.com/item/33011106536.html
    - https://wiki.52pi.com/index.php?spm=a2g0o.detail.1000023.17.45e824fauLpZVU&title=EP-0136
    - https://notenoughtech.com/raspberry-pi/ups-pro-hat/


## Next steps
- Try serving a live streaming with libcamera app already installed in the Raspberry: https://www.raspberrypi.com/documentation/computers/camera_software.html#network-streaming
- Try opening google meet with a shell command: 
  `xdg-open https://meet.google.com/xxx-xx-xxxx`
  This one works, but ask for clicking "join" so it won't join dirctly. See how to deactivate this
- Pi camera is working fine, but its not working for Chromium, so Meet fails detecting it.
- This service could be a workaround to let people access from outside: https://www.socketxp.com/iot/how-to-access-python-flask-app-from-internet/





