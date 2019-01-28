'''
Sample Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika


Sample Output:
56.00

print("{0:.2f}".format(sum(value)/3))
'''
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for key,value in student_marks.items():
    if query_name == key:
        add = 0
        count = 0
        for i in value:
            add=add+i
            count = count + 1
        avg = float(add/count)
        avg = format(avg,'.2f')
        print(avg)
