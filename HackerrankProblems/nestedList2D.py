Here is code provided as solution and its explanation

n = int(input())
marksheet = [ [input(), float(input())] for i in range(n)]
second_highest = sorted(list(set([marks  for name, marks in marksheet])))[1]
print('\n'.join([name for name,mark in sorted(marksheet) if mark == second_highest]))


## step 1 -->

n = int(input())

## either you can use the for loop or you can use the list comprehension
## [input(), float(input())]  is to get student name and marks
## for i in range(n) this is used to iterate loop


marksheet = []

for i in range(n):
    name = input()
    mark = float(input())
    marksheet.append([name,mark])

## or

marksheet = [ [input(), float(input())] for i in range(n)]

print(marksheet)

##[['Mark', 23.4], ['John', 22.6], ['Eric', 33.2], ['Allison', 22.6]]

## list all the marks from marksheet
## marks is to list all marks
## for name, marks in marksheet == this is to iterate through  marksheet

# step 2 -

marks = [marks  for name, marks in marksheet]

print(marks)

## [23.4, 22.6, 33.2, 22.6]


### Now out of list remove any duplicates and you can remove duplicate by converting list to set


# step 3 -

marks = set(marks)

print(marks)

## {33.2, 22.6, 23.4}

# step 4 -

## Now convert set to list to get second highest and sort the list
## Note - List allow you to access eliments with index hence again we are converting set to list


marks = sorted(list(set(marks)))

print(marks)

## [23.3, 32.7, 35.2]

## step 5 - You can access list with index marks[0] is 1st eliment and marks[1] is second


second_highest = sorted(list(set(marks)))[1]

print(second_highest)

## 23.4

## step 6 -- print the student name
## for name,mark in sorted(marksheet) - read all the name and mark from marksheet
## if mark == second_highest check if mark equal to 2nd highest if yes print name
## join is used to print as new line -- https://www.tutorialspoint.com/python3/string_join.htm


print('\n'.join([name for name,mark in sorted(marksheet) if mark == second_highest]))

## Mark
