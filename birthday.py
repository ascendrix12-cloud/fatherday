class person:
    def __init__(self,name,height,weight,gender,age,salary):
      self.name = name
      self.height = height
      self.weight = weight
      self.gender = gender
      self.age = age
      self.salary = salary


    def display_info(self):
       print(f'name : {self.name}')
       print(f'weight : {self.weight}')
       print(f'height : {self.height}')
       print(f'gender : {self.gender}')
       print(f'age : {self.age}')
       print(f'salary : {self.salary}')

    def have_birthday(self):
       self.age = self.age+1
       print(f"happy birthday!,your age is: {self.age}")

    def salary(self):
       self.salary = self.salary
   

person1 = person('salina','5.0','48','f','15-02-2004','120K',)
person2 = person('Astha','5.3','58','f','13-01-2024','100k')
person3 = person('Anupam','5.5','65','m','03-01-2004','160k')
person4 = person('Bikram','6.0','68','m','23-04-2004','120k')

person1.display_info()
person2.display_info()
person3.display_info()
person4.display_info()