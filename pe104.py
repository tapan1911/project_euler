import math
import time

start=time.time()
def GetDigits(n):
	Digits = []
 	while n > 0:
     		Digits.append(n % 10)
     		n = int(n / 10)
	return Digits

def main(): 
	a, b = 0, 1
	i = 2

	Phi = (1 + math.sqrt(5)) / 2

 	while True:
     		c = (a + b) % (10 ** 9)
     		a, b = b, c
  
     		LastDigits = GetDigits(c)
    		LastDigits.sort()
     		if LastDigits == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
  			LogFib = i * math.log(Phi, 10) - math.log(math.sqrt(5), 10)
     			d = int(pow(10, LogFib - int(LogFib - 8)))
  
 	    		FirstDigits = GetDigits(d)
     			FirstDigits.sort()
     			if FirstDigits == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
         			break
     			else:
       				i = i + 1
         			continue
		else:
                        i = i + 1
                        continue

      
 
	elapsed=time.time()-start
	print ("Ans : "), i 
	print ("Time take to find the result = %s seconds")%elapsed

if __name__=='__main__':
	main();


