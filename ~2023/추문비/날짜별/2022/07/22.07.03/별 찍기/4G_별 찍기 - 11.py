a = "*"
b = " "
def draw(Num):
    for i in range(1, Num + 1):
        print(drawline(Num, i))

def drawline(Num, row):
    if row == 0:
        return b * Num
    if Num == 3:
        if row == 1 or row == 3:
            return a * Num
        elif row == 2:
            return a + b + a
    else:
        if row <= Num // 3:
            return drawline(Num // 3, row) * 3
        elif 0 <= Num - row < Num // 3:
            return drawline(Num // 3, Num - row + 1) * 3
        elif (Num // 3) < row <= (Num // 3 * 2):
            return drawline(Num // 3, row - (Num // 3)) + drawline(Num // 3, 0) + drawline(Num // 3, row - (Num // 3))

draw(int(input()))