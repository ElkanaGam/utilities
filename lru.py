class B_Dict():

    def __init__(self, n):
        self.max_size = n
        self.counter = 0
        self.cache = {}
        self.keys  = []

    def __setitem__ (self, k,v):
        if self.counter <  self.max_size:
            self.cache[k] = v
            self.counter += 1
            self.keys.append(k)
        else:
            print ("full")
            to_del = self.keys[0]
            del self.cache[to_del]
            self.keys.pop(0)
            self.cache[k] = v
            self.keys.append(k)
            self.counter += 1

    def __getitem__ (self, k):
        return self.cache[k] if self.cache[k] else print("doesnt exist")


b = B_Dict(2)
for i in range (11):
    b[i] = "i"

print(b.cache)










