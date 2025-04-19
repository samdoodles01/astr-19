import math
import numpy as np

def main():
	#list 1000 numbers between 0 and 2 
	x_values = np.linspace (0, 2, 1000)

	print(" x\t\t sin(x)")
	print("---------------------")

	for x in x_values:
		sin_x = math.sin(x)
		print(f"{x:.5f}\t {sin_x:5f}")


#Run main
main()
