# P5-DistanciaUS

## Introducción
La finalidad de esta práctica es entender los sensores de nivel y proximidad, en concreto, el sensor de ultrasonidos. 

El ultrasonidos aporta información muy precisa sobre la distancia a objetos de una forma muy sencilla. Se considera ultrasonido si la frecuencia es mayor que la frecuencia audible por el oído humano que es de aproximadamente de 20KHz y su funcioamiento se basa en el efecto DOppler. El núcleo del sensor es un material piezoeléctrico, esto se da cuando una tensión salida (Vout) debida a una presión ejercicda sobre el material se deforma y emite una onda mecánica, o en este caso, una onda ultrasónica.

![Fórmula distancia emisor-receptor](https://github.com/rsanchez2021/Image/blob/main/formula_distancia_emisor-receptor.png)

Para más información te recomendamos ojear esta [pániga web](https://www.radiologyinfo.org/es/info/genus) donde explica más detalladamente el funcionamiento del sensor.

## Sensor de ultrasonidos HC-SR04

El ultrasonidos facilitado en el kit es el [HC_SR04](https://github.com/clases-julio/p5-distanciaus-rsanchez2021/blob/main/HC-SR04.pdf). Este sensor cuenta con cuatro pines, cada un tiene una función:

- **VCC** pin de alimentación del sensor (5V)
- **TRIG**: pin de disparo
- **ECHO**: señal de entrada al sistema
- **GND**: pin negativo de toma de tierra

Su funcionamiento se basa en la primera emisión de un pulso que debe ser de al menos 10μs por el pin TRIG, posteriormente el pin manda una serie de 8 pulsos de 40KHZ y pone el pin ECHO en alto y permanecerá en ese estado hasta que reciba el eco de los pulsos. Ese tiempo es el que se cuenta para estimar la distania a la que se encuentra el objeto

## Práctica

### Conexiones del dispositivo

AÑADIR IMAGEN DEL CIRCUITO

### Programación del ultrasonidos

Para enterder el código y unificarlo con la explicación de la teoría del sensor, iremos explicando casi línea por línea lo que se espera que haga el snippet. Para empezar, el ultrasonidos debe mandar el primer pulso de **al menos** 10μs:

```python
GPIO.output(PIN_TRIGGER, GPIO.HIGH)
time.sleep(TIME_TRIG)
GPIO.output(PIN_TRIGGER, GPIO.LOW)
```

Posteriormente, se espera la respuesta mientras cuenta el tiempo hasta que recibe los paquetes: 

```python
while GPIO.input(PIN_ECHO)==0:
    inicioPulso = time.time()
while GPIO.input(PIN_ECHO)==1:
    finPulso = time.time()
```
Posteriormente se calcula la distancia mediante el uso de la [fórmula](https://github.com/rsanchez2021/Image/blob/main/formula_distancia_emisor-receptor.png) mostrada en el primer apartado.

### Ejercicio 

EL ejercicio nos pide añadir tres leds para avisar al usuario de las distancias del objeto al ultrasonida. Leyendo el [datasheet](https://github.com/clases-julio/p5-distanciaus-rsanchez2021/blob/main/HC-SR04.pdf) del ultrasonido la distancia mínima que llega a medir es de 2cm yla máxima de 4m. De forma práctica, lo mínimo que hemos llegado a medir de forma fiable es de 2,5cm y un máximo de 40cm, por ello, hemos puesto en rojo a las distancias menores de 10cm, amarilla entre 10cm y 20cm y en verde mayores de 20cm.

Como cosas importantes, es importante no disminuir el tiempo del puerto TRIGGER pues es imprescidible que sea al menos eso. Además, en caso de no mandar el primer pulso o no recibir las respuestas, el ultrasonido se quedará "pensando" y no avanzará, será necesario cerrar y volver a ejecutar el programa.
