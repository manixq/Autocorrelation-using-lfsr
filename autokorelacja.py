#base_ format: XXXX
#example: 0001

#polynomial_ format: [X X X]
# example: polynomial_ - 4 3 1 
#4 3 1 equals to x^4 + x^3 + 1

def lfsr(base_, polynomial_):
	current = base_
	nbits = base_[0]
	result = [0] * len(base_)
	while 1:
		xor = current[len(polynomial_) - polynomial_[1]]
		result[0] = xor ^ current[-1]
		for i in range(len(base_) - 1):
			result[i + 1] = current[i]
		current = []
		for x in result:
			current.append(x)
		print current
		print "\n" 
		if current == base_:
			break


lfsr([0, 0, 0, 1], [4,3,1])
