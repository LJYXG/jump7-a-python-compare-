#????python???
#?7??
number=0


while number <= 100:
	number=number+1
	if number % 7 == 0:
		continue
	if number % 10 == 7:
		continue
	if number // 10 == 7:
		continue
	
	print(number)



#
'''
while number <= 100:
	number=number+1
	if number % 7 == 0 or number % 10 == 7 or number //10 == 7: 
		continue
	print(number)
'''	
