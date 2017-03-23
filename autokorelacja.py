import sys
print sys.argv

#base_ format: XXXX
#example: 0001

#polynomial_ format: [X X X]
# example: polynomial_ - 4 3 1 
#4 3 1 equals to x^4 + x^3 + 1

def lfsr(base_, polynomial_):
	current = base_
	result = []
	result_ = []
	while 1:
		result_.append(current[-1])
		xor = current[len(polynomial_) - polynomial_[1]]
		result.append(xor ^ current[-1])
		for i in range(len(base_) - 1):
			result.append(current[i])
		current = []
		for x in result:
			current.append(x)
		result = []
		print current
		print "\n" 
		if current == base_:
			break
	return result_

def autocorrelate(Rxx, n):
	for i in range(len(Rxx)):
		if Rxx[i] == 0:
			Rxx[i] = -1
	Rxx_n = Rxx[n:] + Rxx[:n]
	print Rxx
	print Rxx_n
	result = [c_i * c_n for c_i, c_n in zip(Rxx, Rxx_n)]
	print result
	result = sum(result)
	print result


result = lfsr([0, 0, 0, 1], [4,3,1])
autocorrelate(result, 15)
