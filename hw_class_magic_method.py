class SmartDict:
    index = -1

    def __getattr__(self, key):
        return self.__dict__[key]

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        
    def __iter__(self):
        return self

    def __next__(self):

        self.index += 1
        keys_list = list(self.__dict__.keys())

        try:
            return keys_list[self.index]

        except:
            raise StopIteration


d = SmartDict()
d.qw = 1
d.er = 1
d.ty = 1

for i in d:
    if 'index' in i:
        continue

    else:
        print(i)