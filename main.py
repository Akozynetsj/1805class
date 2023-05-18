class OddIterator:
    def __init__(self, n):
        if  n <= 0 and isinstance(n, int):
            raise ValueError('Treba cile natur chuslo')
        self.n = n
        self.current = 1
    def __next__(self):
        return self
    def __next__(self):
            if self.current > self.n:
                raise StopIteration
            else:
                result = self.current
                self.current += 2
                return result

try:
    for num in OddIterator(10):
        print(num)
except ValueError as e:
    print(e)




