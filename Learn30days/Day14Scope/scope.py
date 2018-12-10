class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        self.listNum = [ ]

	# Add your code here
    '''def computeDifference(self):
        sorted_elements = sorted(self.__elements)
        self.maximumDifference = abs(sorted_elements[-1] - sorted_elements[0])'''
    def computeDifference(self):
        for x in a:
            self.listNum.append(abs(x))

        self.maximumDifference = max(self.listNum) - min(self.listNum)    


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
