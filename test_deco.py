import time

def func():
    print('this is in func')



# def timecal(func):
#     start = time.time()
#     func()
#     finish = time.time()
#     print(f'time elapsed:{finish - start} sec(s)')

def timecal(func):

    #定义一个内嵌的包装函数
    def wrapper(name):
        start = time.time()
        func(name)
        finish = time.time()
        print(f'time elapsed:{finish - start} sec(s)')

    return wrapper

# func = timecal(func)
# func()

@timecal
def func(name):
    print(f'this is in func {name}')

name = 'heiheiehie'

func(name)