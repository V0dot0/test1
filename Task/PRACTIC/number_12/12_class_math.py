
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


calculation = Math(20, 5)
Math = Math(20, 5)
print(f"Addition: {Math.addition()}")
print(f"Multiplication: {Math.multiplication()}")
print(f"Division: {Math.division()}")
print(f"Subtraction: {Math.subtraction()}")