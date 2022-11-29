#!/usr/bin/python
import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BCM)

      PIN_TRIGGER =15 
      PIN_ECHO = 18
      
      LED_VERDE = 21
      LED_AMARILLO = 20
      LED_ROJO = 16

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)
      GPIO.setup(LED_VERDE, GPIO.OUT)
      GPIO.setup(LED_AMARILLO, GPIO.OUT)
      GPIO.setup(LED_ROJO, GPIO.OUT)
      
      while True:

          GPIO.output(PIN_TRIGGER, GPIO.LOW)
          GPIO.output(LED_VERDE,GPIO.LOW)
          GPIO.output(LED_AMARILLO,GPIO.LOW)
          GPIO.output(LED_ROJO,GPIO.LOW)

          print ("Esperando a que se estabilice el US")
          time.sleep(2)

          GPIO.output(PIN_TRIGGER, GPIO.HIGH)
          time.sleep(0.00001)
          GPIO.output(PIN_TRIGGER, GPIO.LOW)

          while GPIO.input(PIN_ECHO)==0:
                inicioPulso = time.time()
          while GPIO.input(PIN_ECHO)==1:
                finPulso = time.time()

          duracionPulso = finPulso - inicioPulso
          distancia = round(duracionPulso * 17150, 2)
          
          if distancia <= 5:
              GPIO.output(LED_ROJO,GPIO.HIGH)
          elif (distancia >=5.01) and (distancia <= 15):
              GPIO.output(LED_AMARILLO,GPIO.HIGH)
          else:
              GPIO.output(LED_VERDE,GPIO.HIGH)

          print ("Distancia: ", distancia, " cm")
          time.sleep(2)

finally:
      GPIO.cleanup()
      

