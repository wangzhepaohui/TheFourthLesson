#函数按值，按引用调用
a = [1,2,3,4,5]
def square(items):
    for i,x in enumerate(items):
        items[i]= x*x
square(a)
print(a)

def square(x):
    return x*x
b=4
print(square(b))
print(b)

#枚举
seasons = ['spring','summer']
print(1,enumerate(seasons),type(enumerate(seasons)))
print(2,list(enumerate(seasons)))
print(3,list(enumerate(seasons,start=1)))

i=0
seq = ['one','two','three']
for item in seq:
    print(i,seq[i])
    i+=1

for i,element in enumerate(seq):
    print(i,element)

