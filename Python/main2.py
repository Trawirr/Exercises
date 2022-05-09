# add(1)(2)(3); // == 6
# add(1)(2)(3)(4); //  == 10
# add(1)(2)(3)(4)(5); // == 15

class AddInt(int):
    def __call__(self, value):
        return AddInt(self + value)

def add(n):
    return AddInt(n)