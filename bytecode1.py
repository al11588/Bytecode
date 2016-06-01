import dis #importing the dissambler 

def add_with_assign(g, e, d): #defined my function to be g e d

	x = g + e / d # adding g and e then dividing d
	return x # returning the x value

dis.dis(add_with_assign) #output the function in binary code

