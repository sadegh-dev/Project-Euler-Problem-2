"""
1, 2, 3, 5, 8, 13, 21, ..., 4.000.000

? = sumi [ 2, 8, ..., 4.000.000 ]

"""
i = 1
j = 2
fibo = [2]
sumi = 0
while (i+j) <= 4000000 :
	sumi = i+j
	if sumi % 2 == 0 :
		fibo.append(sumi)
	i = j
	j = sumi
print ("Fibonacci even-valued : " + str(fibo))

sumi = 0
for x in fibo:
	sumi = sumi + x
print ("sum even-valued : " + str(sumi))
