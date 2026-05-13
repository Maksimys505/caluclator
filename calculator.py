print("Первое число:")
a=float(input())
print('Второе число:')
b=float(input())
print('Выберите действие:')
print('1.+')
print('2.-')
print('3.*')
print('4./')
c=input()
if c=='1':
    print(a+b)
elif c=='2':
    print(a-b)
elif c=='3':
    print(a*b)
elif c=='4':
    if a%b==0:
        print(a//b)
    else:
        print(a/b)