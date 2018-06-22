import time
import math
start_time = time.time()
# 素因数分解
# 1000以下の素数を全て表示するプログラム

# 素数・・・1以上の自然数で、1と自分自身でしか割り切れない数

# 1. 愚直に2から1000までの数字で割ってみる
array = []
for i in range(2, 1001):
    sosu = True
    for n in range(2, i):
        if i % n == 0:
            sosu = False
            break
            # 割り切れる場合（素数ではない場合）
            # 一回でも何かの数値で割り切れたら素数ではない
    if sosu:
        array.append(i)
print(array)

# 2_1. 偶数は、素数ではない
array = []
for i in range(2, 1001):
    sosu = True
    for n in range(2, i):
        if i == 2 and i % 2 == 0:
            # そもそも偶数は素数ではない
            sosu = False
            break
        if i % n == 0:
            sosu = False
            break
            # 割り切れる場合（素数ではない場合）
            # 一回でも何かの数値で割り切れたら素数ではない
    if sosu:
        array.append(i)
print(array)

# 2_2 range()で2の倍数を飛ばすことができる
array = [2]
for i in range(3, 1001, 2):
    # 3から始まって、2づつ増えていく
    sosu = True
    for n in range(2, i):
        if i % n == 0:
            sosu = False
            break
            # 割り切れる場合（素数ではない場合）
            # 一回でも何かの数値で割り切れたら素数ではない
    if sosu:
        array.append(i)
print(array)



# 3. その数を、これまで取得した素数で割れなかったら素数である
array = []
for i in range(2, 1001):
    sosu = True
    for n in range(len(array)):
        if i % array[n] == 0:
            # これまで取得した素数で割る
            sosu = False
            break
    if sosu:
        array.append(i)
print(array)


# 4. ある数iの平方根以上の素数では、割り切れない
array = [2]
for i in range(3, 1001, 2):
    sosu = True
    for n in range(len(array)):
        if array[n] > math.sqrt(i):
            break
        if i % array[n] == 0:
            # これまで取得した素数で割る
            sosu = False
            break
    if sosu:
        array.append(i)
end_time = time.time()
elapse_time = end_time - start_time
print(array)
print(elapse_time)
