class Math:# Parent Class
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

class MathXtention(Math):# Child Class
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def subtract(self):
        return self.num1 - self.num2

obj = MathXtention(8,3)
print(obj.sum())
print(obj.subtract())
