day_nomer=int(input("введите  число от 1-7"))
days={1:"понедельник",
      2:"вторник",
      3:"среда",
      4:"четверг",
      5:"пятница",
      6:"суббота",
      7:"воскресенье"}
day_name=days.get(day_nomer)
if day_name:
    print(f'день недели: {day_nomer}-{day_name}')
else:
    print("ошибка")





