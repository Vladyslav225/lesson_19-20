class IterClass:

     def __init__(self, value_list):
         self.index = 0
         self.value_list = value_list

     def __iter__(self):
          return self
     
     def __next__(self):
          self.index += 1

          keys_self = list(self.__dict__.keys())

          if self.index == len(self.value_list):
               self.index = 0
               raise StopIteration

          return keys_self[self.index]

# class SmartDict(IterClass):

     def __getattr__(self, key):
          print(key)
          print('key', key)
          return self.__dict__[key]

     def __set__(self, key, value):
          print('____')
          print('key', key)
          print('value', value)
          self.__dict__[key] = value

     def _func(self):
          print(list(self.__dict__.keys()))


iter_classes = IterClass(value_list = [1, 2, 3, 4])

smarty = IterClass
smarty.name = '1'
smarty.name1 = 'S1'
smarty._func(iter_classes)

# for key in iter_classes:
#      print(next(iter_classes[key]))


