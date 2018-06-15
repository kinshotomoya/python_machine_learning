# １. フィボナッチ数列（ジェネレータ）
def fib(n):
    a, b = 1, 2
    for i in range(n):
        yield a
        a, b = b, a + b

print([i for i in fib(10)])

# 2. appendでフィボナッチ数列を作成
fibo = [1, 2]
sum_array = []
while sum(fibo) < 4000000:
    sum_num = fibo[-1] + fibo[-2]
    fibo.append(sum_num)

for i in range(len(fibo)):
    if i % 2 == 0:
        sum_array.append(fibo[i])
print(sum(sum_array))

