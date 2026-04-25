players={'andrey':100,'sanya':200,'matvey':80,'misha':300}
good_player=""
max=-1
for name,x in players.items():
    if x>max:
        max=x
        good_player=name
print(f'лучший игрок:{good_player},его результат:{max}')