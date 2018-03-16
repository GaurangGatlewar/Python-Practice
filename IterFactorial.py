class IterFactorial():
	def __init__(self):
		print ("Please enter a number greater than 1")
		n = int(input().strip())
		if(n<1):
			print ("Invalid input")
			return
		answer = self.fact(n)
		print (answer)
		return

	def fact(self,n):
		answer = 1
		for i in range(2,n+1):
			answer *= i
		return (answer)

if __name__ == '__main__':
	IterFactorial()