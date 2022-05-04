class Team:
    name = ""
    games = 0
    win = 0
    draw = 0
    lose = 0
    score = 0
l_names = []
l_team = []

n = int(input())
f1 = 0
f2 = 0
for i in range(n):
    s = input().split(';')
    if s[0] not in l_names:
        t = Team()
        t.name = s[0]
        l_names.append(s[0])
        l_team.append(t)
    if s[2] not in l_names:
        t = Team()
        t.name = s[2]
        l_names.append(s[2])
        l_team.append(t)
    
    for j in range(len(l_names)):
        if s[0] == l_names[j]:
            f1 = j
        if s[2] == l_names[j]:
            f2 = j

    if int(s[1]) > int(s[3]):
        l_team[f1].win += 1
        l_team[f1].games += 1
        l_team[f1].score += 3
        l_team[f2].lose += 1
        l_team[f2].games += 1
    if int(s[1]) < int(s[3]):
        l_team[f1].lose += 1
        l_team[f1].games += 1
        l_team[f2].score += 3
        l_team[f2].win += 1
        l_team[f2].games += 1
    if int(s[1]) == int(s[3]):
        l_team[f1].draw += 1
        l_team[f1].games += 1
        l_team[f1].score += 1
        l_team[f2].draw += 1
        l_team[f2].games += 1
        l_team[f2].score += 1

for i in range(len(l_team)):
    print(l_team[i].name, end=": ")
    print(l_team[i].games,l_team[i].win, l_team[i].draw, l_team[i].lose, l_team[i].score)        