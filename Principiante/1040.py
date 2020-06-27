cadena=input().split(' ')
n1=float(cadena[0])
n2=float(cadena[1])
n3=float(cadena[2])
n4=float(cadena[3])
media=(n1*2+n2*3+n3*4+n4)/10
print('Media: {:.1f}'.format(media))
if media>=7.0:
    print('Aluno aprovado.')
elif media<5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n5=float(input())
    print('Nota do exame: {:.1f}'.format(n5))
    media=(media+n5)/2
    if media>=5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media))
