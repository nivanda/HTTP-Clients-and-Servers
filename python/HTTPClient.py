#Moodulite importimine
import requests as rq

#Andmete saamine ja välja printimine
data = rq.get('https://demo2.z-bit.ee/todo.json')
print(data.text)