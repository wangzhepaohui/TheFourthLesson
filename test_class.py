class CountFromBy:
    #v,i 传到对向上的两个参数
    def __init__(self, v:int=0, i:int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> None:
        return str(self.val)

    #pass


a = CountFromBy(100,20)

print(a.val)
print(a.incr)

a.increase()

print(a.val)
print(a.incr)

b = CountFromBy(400,33)

print(b.val)
print(b.incr)

b.increase()

print(b.val)
print(b.incr)

print(a,type(a),hex(id(a)))

c = CountFromBy()
c.val = 100
c.increase()
print(c.val)

class animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def shit(self):
        print("拉")
    def pee(self):
        print("撒")
    def cry(self):
        print("animal cry")

class cat(animal):
    def cry(self):
        print("喵喵")
class dog(animal):
    def cry(self):
        print("汪汪")

a = cat()
b = dog()
print(a.cry(),a.drink())
print(b.cry(),b.drink())



