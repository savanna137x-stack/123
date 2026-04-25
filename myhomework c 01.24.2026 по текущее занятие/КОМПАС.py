def main(path: str, startcords: tuple = (0, 0)) -> tuple:

    if not isinstance(path, str):
        return ("ошибка",)
    if not isinstance(startcords, tuple) or len(startcords) != 2:
        return ("ошибка",)

    x, y = startcords


    for step in path:
        if step == "S":
            y -= 1
        elif step == "N":
            y += 1
        elif step == "W":
            x -= 1
        elif step == "E":
            x += 1


    x_min, x_max = 0, 100
    y_min, y_max = 0, 100

    if x_min <= x <= x_max and y_min <= y <= y_max:
        return (x, y)
    else:
        return ("не в координатах", x, y)
print(main("NNEW", (0, 0)))
