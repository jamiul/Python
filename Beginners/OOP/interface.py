# Interface is an empty class
# It has only method declaration
# Method has no body part
class AdvancedArithmetic(object):
    def sum(self,num1,num2):
        raise NotImplementedError

class Math(AdvancedArithmetic):
    def sum(self,num1,num2):
        return num1+num2




m = Math()
print(m.sum(2,3))
