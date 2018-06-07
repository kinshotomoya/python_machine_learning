if __name__ == '__main__':
    # ソートされてるのが前提条件
    list = [1, 3, 5, 9, 18, 20]
    low = 0
    high = len(list) - 1
    item = 1 #検索したい数値
    
    while low <= high:
        mid = (low + high) // 2 #//で、小数点以下切り捨てることができる
        guess = list[mid]
        if guess == item:
            print(f"見つかりました！{item}")
            break
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
    if guess != item:
        print(f"{item}は、listに存在しません")
