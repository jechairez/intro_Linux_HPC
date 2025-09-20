import sys

if len(sys.argv) < 2:
	print ("Debes de al menos proporcionar 2 datos")
	sys.exit(1)

N = int(sys.argv[1])
suma=sum(range(1, N+1))
print(f"suma de 1 hasta {N} = {suma}")

