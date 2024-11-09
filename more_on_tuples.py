# operations on tuple
books=('python','java','mySQL')
lib=('kids','novels','text books','journals')
print(books+lib)

print(books*2)

print(2*lib)

et=(2,4,6,8)
ot=(1,3,5,7)

print(et>ot)

et1=(0,2,4,6,8)
print(et1>ot)

print(6 in et)

print(10 in et)

print(et[2:4])

print(ot[ :3])

# coping and deliting tuple
books=('novel','tb','comics')
b1=books
print(b1)

print(id(b1))
print(id(books))

del b1
print(books)

# inputting a tuple
tup=eval(input("input a tuple: "))
print(tup)

l=[]
for i in range(4):
    ele=int(input('enter an element: '))
    l.append(ele)
tup=tuple(l)
print(tup)
