#!/bin/python3

import sys

class ReverseArray():
	def __init__(self):
		pass

	def Solve(self, arr):
		s = ""
		for i in range(n):
		    s += str(arr[n-i-1])
		    s += ' '
		return s


if __name__ == "__main__":
	print ("Enter array size:")
	n = int(input().strip())
	print ("Enter the array elements:")
	arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

	ans = ReverseArray().Solve(arr)
	print (ans)