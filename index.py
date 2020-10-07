"""
1, 2, 3, 5, 8, 13, 21, ..., 4.000.000

? = sum [ 2, 8, ..., 4.000.000 ]

"""
i = 1
j = 2
fibo = [2]
sum = 0
while (i+j) <= 4000000 :
	sum = i+j
	if sum % 2 == 0 :
		fibo.append(sum)
	i = j
	j = sum
print ("Fibonacci even-valued : " + str(fibo))

sum = 0
for x in fibo:
	sum = sum + x
print ("sum even-valued : " + str(sum))
