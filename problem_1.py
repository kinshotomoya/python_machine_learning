# 3と５の倍数
# 1000未満の3 or 5の倍数になっている数字の合計
array = []
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        array.append(i)        
print(sum(array))

# 一行で書く
print(sum([i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0]))
