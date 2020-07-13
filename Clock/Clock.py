import time

hours = 0
minutes = 0
seconds = 0

print("Favor indicar o horário atual:\n")
IHour = int(input("Hora = "))
IMinute = int(input("Minutos = "))
ISecond = int(input("Segundos = "))

ActualTime = IHour*3600 + IMinute*60 + ISecond

while True:
    for Ttime in range(ActualTime, 86400):
        if Ttime == 86399:
            ActualTime = 0
        hours = Ttime // 3600
        minutes = (Ttime % 3600) // 60
        seconds = (Ttime % 3600) % 60

        print(hours, ":", minutes, ":", seconds)
        time.sleep(1)