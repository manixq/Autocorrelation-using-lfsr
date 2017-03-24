import sys
import matplotlib.pyplot as plt
#===========
#Pawel Mania
#===========

#calc LFSR
#base is a list of binary symbols
#polynomial is represented as [4, 3, 1] = x^4 + x^3 + 1
def lfsr(base_, polynomial_):
	current = base_
	result = []
	result_ = []
	print "\n\n==========="
	print "LFSR"
	print "==========="
	while 1:
		print current, "\n"
		result_.append(current[-1])
		xor = current[len(base_) - 1 - polynomial_[1]]
		result.append(xor ^ current[-1])
		for i in range(len(base_) - 1):
			result.append(current[i])
		current = []
		for x in result:
			current.append(x)
		result = []
		if current == base_:
			break
	return result_

#autocorrelation where n is shifting value
def autocorrelate(Rxx, poly_):
	num_bit = poly_[0]
	x = range(0, pow(2, num_bit))
	y = []
	for i in range(len(Rxx)):
		if Rxx[i] == 0:
			Rxx[i] = -1	
	print "\n\n=============================================\n"
	for n in range(0, pow(2, num_bit)):
		Rxx_n = Rxx[n:] + Rxx[:n]
		result = [c_i * c_n for c_i, c_n in zip(Rxx, Rxx_n)]
		y.append(sum(result))
		print"\t\tRxx(",n,") = ", sum(result), "\n"
	print "=============================================\n"
	plt.title(poly_)
	plt.plot(x, y, 'ro')
	plt.show()
	return sum(result)


#if u fail
if len(sys.argv) == 1:
	print sys.argv, "\n"
	print "I need some arguments to discuss...\n"
	print "Input: [Array of starting LFSR] [Array of polynomial values]"
	print "Example: ", sys.argv[0], "[0,0,0,1] [3,1,0]"
	sys.exit()

#input data...
for i in range(1, 3):
	sys.argv[i] = map(int, sys.argv[i][1:-1].split(","))

if len(sys.argv[1]) != sys.argv[2][0]:
	print "something is wrong with input data..."
	sys.exit()

#Main program
result = lfsr(sys.argv[1], sys.argv[2])
autocorrelate(result, sys.argv[2])
