import math

summa = 0
differens = 0
n = input("Vilket n?")
#Beräknar summan beroende på vilket n man anger
for i in range(1, int(n)+1):
    summa = summa + (1/(i*i))
differens = ((math.pi)*(math.pi)/6)- summa
print("Summa: " + str(summa) + "\nDifferens: " + str(differens))
