# バブルソート
array = [9, 1, 4, 1, 3, 13, 42, 0, 2, 7, 2]

chenged = True
i = 0
move_num_conter = 0
while chenged:
    if array[i] > array[i+1]:        
        left_num = array[i]
        right_num = array[i+1]
        array[i] = right_num
        array[i+1] = left_num
        move_num_conter += 1
    i += 1
    if i == len(array) - 1 and move_num_conter == 0:
        chenged = False
        break
    if i > len(array) - 2:
        i = 0
        move_num_conter = 0
print(array)
