entrada=input().split()
x=int(entrada[0])
y=int(entrada[1])
if x==1:
    v=y*4.00
if x==2:
    v=y*4.50
if x==3:
    v=y*5.00
if x==4:
    v=y*2.00
if x==5:
    v=y*1.50
print('Total: R$ {:.2F}'.format(v))