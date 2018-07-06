first_num = 1112
second_nam = 695

while True:
    result_num = first_num % second_nam
    if result_num == 0:
        print(second_nam)
        break
    first_num = second_nam
    second_nam = result_num

def countdown(num):
    print(num)
    if num <= 0:
        return
    countdown(num - 1)

countdown(3)
