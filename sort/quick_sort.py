# クイックソートのプログラム
# 再帰的にメソッドを実行する
import random

array = [3, 4, 6, 7, 2, 9, 10]

def quick_sort(array):
    print(array, "start")
    low_array = []
    high_array = []
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    pivot_count = 0
    for a in range(len(array)):
        if pivot > array[a]:
            low_array.append(array[a])
        elif pivot < array[a]:
            high_array.append(array[a])
        else:
            pivot_count += 1
    print(pivot, low_array, high_array, pivot_count)
    low_array = quick_sort(low_array)
    # ここを抜けた時点で、low_arrayは完成している
    print(pivot, low_array, high_array, pivot_count, "ss")
    high_array = quick_sort(high_array)
    print(pivot, low_array, high_array, pivot_count, "qqq", low_array + [pivot] * pivot_count + high_array)
    return low_array + [pivot] * pivot_count + high_array

print(quick_sort(array))
