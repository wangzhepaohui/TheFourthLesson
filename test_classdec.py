class Test(object):
    def __init__(self, func):
        print(f'func name is {func.__name__}')
        self.__func =func

    def __call__(self, *args, **kwargs):
        print("it is a wapper")
        self.__func()

    # def tasta(self):
    #     print('test')

# t = Test()
# print(t())

@Test
def test():
    print('this is a test')

test()