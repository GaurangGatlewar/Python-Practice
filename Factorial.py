class Factorial():
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
		if(n == 1):
			return 1
		else:
			return (n * self.fact(n-1))

if __name__ == '__main__':
	Factorial()