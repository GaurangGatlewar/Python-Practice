class Mergesort:
	"""docstring for Mergesort"""
	def __init__(self):
		super(Mergesort, self).__init__()
		print ("Please enter the numbers to be sorted")
		try:
			numbers = list(map(int, input().strip().split(' ')))
		except:
			print ("Invalid input")
			return
		answer = self.mergesort(numbers)
		print ("The numbers in sorted order are:")
		print(answer)
		return

	def mergesort(self, numbers):
		if(len(numbers) < 2):
			pass
		elif(len(numbers) == 2):
			if(numbers[0]>numbers[1]):
				numbers[0], numbers[1] = numbers[1], numbers[0]
		else:
			l1 = self.mergesort(numbers[:len(numbers)//2])
			l2 = self.mergesort(numbers[len(numbers)//2:])
			numbers = self.merge(l1, l2)
		return (numbers)

	def merge(self, l1, l2):
		answer = []
		i = 0
		j = 0
		if(l1[-1]>l2[-1]):
			l1, l2 = l2, l1
		while(i<len(l1)):
			if(l1[i]<l2[j]):
				answer.append(l1[i])
				i += 1
			else:
				answer.append(l2[j])
		for number in l2[j:]:
			answer.append(number)
		return (answer)
		
if __name__ == '__main__':
	Mergesort()