import sys
import ast

#calc LFSR
#base is a list of binary symbols
#polynomial is represented as [4, 3, 1] = x^4 + x^4 + 1
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
		xor = current[len(polynomial_) - polynomial_[1]]
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
def autocorrelate(Rxx, n):
	for i in range(len(Rxx)):
		if Rxx[i] == 0:
			Rxx[i] = -1
	Rxx_n = Rxx[n:] + Rxx[:n]
	result = [c_i * c_n for c_i, c_n in zip(Rxx, Rxx_n)]
	rows = zip(Rxx, Rxx_n, result)
	print "\n\n=================================================="
	print "\tBase\t|\tShiftet\t|\tMultiplied"
	print "=================================================="
	for row in rows:
		print "\t", row[0], "\tx\t", row[1], "\t=\t", row[2], "\n"
	print "\n\n============================================="
	print"\n\t\tRxx(",n,") = ", sum(result), "\n"
	print "=============================================\n"
	return sum(result)


#if u fail
if len(sys.argv) == 1:
	print sys.argv, "\n"
	print "I need some arguments to discuss...\n"
	print "Input: [Array of starting LFSR] [Array of polynomial values] [Shift]"
	print "Example: ", sys.argv[0], "[0,0,0,1] [3,1,0] 4"
	sys.exit()

#input data...
for i in range(1, 3):
	sys.argv[i] = map(int, sys.argv[i][1:-1].split(","))
sys.argv[3] = int(sys.argv[3]);

#Main program
result = lfsr(sys.argv[1], sys.argv[2])
autocorrelate(result, sys.argv[3])
