# Since the last digit is 0 hence the square root must have a zero in end
# If the square root has one 0 in end than the square will have 2 zeroes in the end
# Hence the second last digit will also be zero
# Also The square root must end up with a 3 or 7 as the square has 3rd last digit a 9
# Initial value is correct since it is just more than square root of 1020304050607080900.

import time

start = time.time()
i = 1010101030

while True:
    if str(i*i)[::2] == "1234567890":
        break
    i += 40
    if str(i*i)[::2] == "1234567890":
        break
    i += 60

elapsed = time.time()-start
print "Ans = ",i
print "Time taken to find the result = %s seconds"%elapsed
