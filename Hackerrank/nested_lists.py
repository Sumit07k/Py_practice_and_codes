'''
Sample Input 0

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

Sample Output 0

Berry
Harry

Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    new_lst = []
    score_lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new_lst.append([name,score])
        score_lst.append(score)
    new_lst = sorted(new_lst)
    score_set = sorted(set(score_lst))
    second_lowest = (score_set[1])
    for i in new_lst:
        for j in i:
            if j == second_lowest:
                print(i[0])