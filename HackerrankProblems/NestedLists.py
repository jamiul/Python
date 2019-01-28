'''
# Sample Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

# Sample Output:
Berry
Harry

'''
if __name__ == '__main__':
    marksheet = [ ]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name,score])

    scores =[scores for name,scores in marksheet]

    scores = sorted(list(set((scores))))
    second_highest = scores[1]

    print('\n'.join([name for name,score in sorted(marksheet) if score == second_highest]))
