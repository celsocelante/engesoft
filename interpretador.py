class interpretador:
	__init__(self, args):
	      self.args = args
	      entradas = []

					  
	for i in range(0,5):
		entradas.append("")
		
	for i in range(0,len(args)):
		if args[i] == "-e":
			entradas[0] = args[i+1]
		if args[i] == "-t":
			entradas[1] = args[i+1]
		if args[i] == "-p":
			entradas[2] = args[i+1]
		if args[i] == "-a":
			entradas[3] = args[i+1]
		if args[i] == "-r":
			entradas[4] = args[i+1]

	print entradas
