class TestClass:
    x = 5
    def __init__(self):
        pass

    @staticmethod
    def inc_x():
        TestClass.x += 1
        print(TestClass.x)

t1 = TestClass()
t2 = TestClass()

t1.inc_x()
t2.inc_x()

print(TestClass.x)