#Set
#a={1,2,3}
#b=set(1,2,3,1) УНикальный мәндер

#list
#a=[1,2,3]
#b=list(1,2,3)

#tuple
#a=(1,2,3)
#b=tuple(1,2,3)

#dict
#a={"name":"Dauren"}

#type
#print(type(a))
#if type (a) = dict:

a=4
while a <= 5 :
    print("Hello")
    a+=1
    break
print("fin")


b=0
while True:
    if b ==3:
        break
    print("Hi")
    b+=1

c = [(1, 2), (1,), (2, 3), 1]

a = 0
i = 0

while i < len(c):
    if isinstance(c[i], tuple):
        a += 1
    i += 1
print(a)
