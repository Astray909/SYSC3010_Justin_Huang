for number in range(1, 51):
	 factors = 0
	 print(number, end=": ")
	 for divisor in range(1, number+1):
		 if number%divisor == 0:
			 print(divisor, end=" ")
			 factors+=1
	 if (factors == 2):
		
	 else:
		print()