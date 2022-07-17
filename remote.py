from gpiozero import Motor
from time import sleep

m1 = Motor(27, 22)
m2 = Motor(21, 20)

while(1):
    
    x=input()
    
    
    if x=='f':
        m1.forward()
        m2.forward()
        
    if x=='s':
       m1.backward()
       m2.forward()
        
    if x=='c':
        m1.stop()
        m2.stop()
        
    if x=='stop':
        m1.stop()
        m2.stop()
        exit()
