class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, changedName, changedAge):
        self.name = changedName
        self.age = changedAge

    def setGroupNumber(self, changedGroupNumber):
        self.groupNumber = changedGroupNumber


Default = Student()
print(f"Name: {Default.getName()}")
print(f"Age: {Default.getAge()}")
print(f"Group: {Default.getGroupNumber()} \n")

Artyom = Student()
Artyom.setNameAge("Artyom", 15)
Artyom.setGroupNumber("15C")
print(f"Name: {Artyom.getName()}")
print(f"Age: {Artyom.getAge()}")
print(f"Group: {Artyom.getGroupNumber()}\n")

Kerish = Student()
Kerish.setNameAge("Kerish", 20)
Kerish.setGroupNumber("20A")
print(f"Name: {Kerish.getName()}")
print(f"Age: {Kerish.getAge()}")
print(f"Group: {Kerish.getGroupNumber()}\n")

Tony = Student()
Tony.setNameAge("Tony", 25)
Tony.setGroupNumber("1A")
print(f"Name: {Tony.getName()}")
print(f"Age: {Tony.getAge()}")
print(f"Group: {Tony.getGroupNumber()}\n")

Alex = Student()
Alex.setNameAge("Alex", 28)
Alex.setGroupNumber("28G")
print(f"Name: {Alex.getName()}")
print(f"Age: {Alex.getAge()}")
print(f"Group: {Alex.getGroupNumber()}\n")


