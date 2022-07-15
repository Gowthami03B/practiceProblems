# Python3 program to find Nth Fibonacci
# number using recursion


# Function to find Nth Fibonacci term
def Fibonacci(N:int):
	# Base Case
	if (N < 2):
		return N

	# Recursively computing the term
	# using recurrence relation
	return Fibonacci(N - 1) + Fibonacci(N - 2)


# Driver Code
if __name__ == '__main__':
	N = 5

	# Function Call
	print(Fibonacci(N))
"""
Time Complexity: O(2N)
Auxiliary Space: O(1)
"""
 # Python3 program to find Nth Fibonacci
# number using recursion

# Function to find Nth Fibonacci term
def Fibonacci(N):
	f=[0]*(N + 2)

	# 0th and 1st number of the
	# series are 0 and 1
	f[0] = 0
	f[1] = 1

	# Iterate over the range [2, N]
	for i in range(2,N+1) :

		# Add the previous 2 numbers
		# in the series and store it
		f[i] = f[i - 1] + f[i - 2]
	

	# Return Nth Fibonacci Number
	return f[N]


# Driver Code
if __name__ == '__main__':
	N = 5

	# Function Call
	print(Fibonacci(N))
"""
Time Complexity: O(N)
Auxiliary Space: O(N)
"""
