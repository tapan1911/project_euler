def get_digits(n):
    return sorted(str(n))

def same_digits(n, iterations):
    digits = get_digits(n)
    for i in range(1, iterations):
        if not digits == get_digits(n+(i*n)):
            return False
    return True


n = 0
found = False
while not found:
	n += 1
	if same_digits(n,6):
		found = True
print n

