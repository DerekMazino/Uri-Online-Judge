def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

if __name__ == "__main__":
    nCasos=int(input())
    resp=[]
    for i in range(nCasos):
        n1, n2= input().split(' ')
        resp.append(mcd(int(n1),int(n2)))
    for i in resp:
        print(i)