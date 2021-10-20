import json

class FirstClass:

     MODE_READ = 'r'
     MODE_WRITE = 'w'

     def __init__(self, value: dict):
         self.value = value

     def serializer(self, value):

          if type(value) == dict:
               return str(value)

          elif type(value) == str:
               return eval(value)

     def write_file_txt(self):

          value = self.serializer(value=self.value)

          file = open(str(self), self.MODE_WRITE)
          file.write(value)
          file.close
          return value

     def read_file_txt(self):

          value = self.serializer(value=self.value)

          file = open(str(self), self.MODE_READ)
          file.read()
          return value

     def __str__(self):
          return 'name_file'

class SecondClass(FirstClass):

     def __str__(self):
         return 'name_file.json'

     def serializer(self, value):

          value = super().serializer(self.value)
          return value

     def write_file_json(self):

          value = self.serializer(value=self.value)

          file = open(str(self), self.MODE_WRITE)
          json.dump(self.value, file)
          return value
          

     def read_file_json(self):

          value = self.serializer(value=self.value)

          file = open(str(self), self.MODE_READ)
          json.load(file)
          return value
          
          
          
class_txt = FirstClass(value = {'key': 'value', 'key1': 'value1'})
class_txt.write_file_txt()
class_txt.read_file_txt()
data_txt = class_txt.serializer(value = "{'key': 'value', 'key1': 'value1'}")
print(data_txt)

class_json = SecondClass(value = "{'key': 'value', 'key1': 'value1'}")
class_json.write_file_json()
value = class_json.read_file_json()
data_json = class_json.serializer(value = "{'key': 'value', 'key1': 'value1'}")
print(data_json)

