from abc import ABC, abstractmethod
class Math(ABC):# Make the class Abstract
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    @abstractmethod # make the method Abstract
    def add(self):
        pass


class MathXtension(Math):
    def __init__(self,num1,num2,num3):
        super().__init__(num1,num2)
        self.num3 = num3
    def add(self):#  we can access abstractmethod through method Overriding
        return self.num1 + self.num2 + self.num3

m = MathXtension(2,3,8)
print(m.add())
