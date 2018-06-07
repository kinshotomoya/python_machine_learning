list = [3, 5, 1, 8, 9, 10, 45, 89, 0, 34, 97, 39, 32]
item = 32

for index in range(0, len(list)):
    if item == list[index]:
        print(f"{index + 1}番目に、{item}を見つけました!")
        break
    elif index == (len(list) - 1):
        print(f"{item}は、listには存在しません")
