#------------------------------
#Ejercicio: Práctica p5 sensores y actuadores --> Ultrasonidos
#Autores: Jorge Martín y Rebeca Sánchez
#Fecha límite de entrega: 30/11/22
#Objetivo: clasificar las distancias medidas por el ultrasonido
#------------------------------

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BCM)
      #Establecer pines ultrasonido
      PIN_TRIGGER =15 
      PIN_ECHO = 18
      #Establecer pines leds
      LED_VERDE = 21
      LED_AMARILLO = 20
      LED_ROJO = 16
      
      TIME = 2
      VEL_SON = 34300
      TIME_TRIG = 0.00001
      
      #establecer saslidas y entradas
      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)
      GPIO.setup(LED_VERDE, GPIO.OUT)
      GPIO.setup(LED_AMARILLO, GPIO.OUT)
      GPIO.setup(LED_ROJO, GPIO.OUT)
      
      while True:
          #Apagar todo
          GPIO.output(PIN_TRIGGER, GPIO.LOW)
          GPIO.output(LED_VERDE,GPIO.LOW)
          GPIO.output(LED_AMARILLO,GPIO.LOW)
          GPIO.output(LED_ROJO,GPIO.LOW)

          print ("Esperando a que se estabilice el US")
          time.sleep(TIME)
          #Primer pulso de al menos 10microsegundos
          GPIO.output(PIN_TRIGGER, GPIO.HIGH)
          time.sleep(TIME_TRIG)
          GPIO.output(PIN_TRIGGER, GPIO.LOW)
          #Tiempo de inicio
          while GPIO.input(PIN_ECHO)==0:
                inicioPulso = time.time()
          #Tiempo final
          while GPIO.input(PIN_ECHO)==1:
                finPulso = time.time()
          
          #Calcular distancia      
          duracionPulso = finPulso - inicioPulso
          distancia = round(duracionPulso * (VEL_SON / 2), TIME)
          
          if distancia <= 10:
              GPIO.output(LED_ROJO,GPIO.HIGH)
          elif (distancia >=10.01) and (distancia <= 20):
              GPIO.output(LED_AMARILLO,GPIO.HIGH)
          else:
              GPIO.output(LED_VERDE,GPIO.HIGH)

          print ("Distancia: ", distancia, " cm")
          time.sleep(TIME)

finally:
      GPIO.cleanup()

#---------------------
#CASOS DE USO:
#-La distancia mímima que calcula es de 2cm
#-La distancia máxima que hemos conseguido medir es de 40 cm pero en la datasheet expicifíca que es de 4m
#-No disminuir el tiempo TIME_TRIG pues tiene que ser ese o superior
#-En caso de tener algún pin mal conectado nunca llegará a recibir las ondas de veulta y se quedará pensando
#-En caso de no mandar el primer pulso también se queda pensando
#---------------------
