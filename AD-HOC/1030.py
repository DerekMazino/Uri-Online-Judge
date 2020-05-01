def ruleta(n,k):
    if n==1:
        return 1
    return (ruleta((n-1),k)+k-1)%n+1
if __name__ == "__main__":
    ncasos=int(input())
    for i in range(ncasos):
        casoPrueba=input().split()
        print(ruleta(int(casoPrueba[0]),int(casoPrueba[1])))