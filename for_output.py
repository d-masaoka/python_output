# for ループ
fruits = ['apple', 'peach', 'greapes', 'banana']

""" for fruit in fruits:
    print(f"I love {fruit}!!")

# forループ の動き
# ループでまわす　イテレーションする
# イテレーションできるオブジェクト イテラブル
for char in "hello world!!":
    print(f"char: {char}") """

# challenge1

""" # 好きなフルーツを入力
fruits_like = input("好きなフルーツを入力してください。")
# ループ処理
for fruit in fruits:
    if fruit == fruits_like:
        print(f"{fruit}が好き")
    else:
        print(f"{fruit}は好きじゃない") """

# challenge2
""" fruits_love= []
b = []
for fruit in fruits:
    q = input(f"{fruit}は好きですか？ y/n")

    if q == "y":
        fruits_love.append(fruit)
    else:
        b.append(fruit)
print(f"好きなフルーツは{fruits_love}です。")
print(f"嫌いなフルーツは{b}です。") """

# range(start, stop, step)
# step はデフォルトで1
""" for i in range(1, 7):
    print(i)

for i in range(10):
    print("hello")
 """
# challenge 
for i in range(1, 51):
    if i % 15 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Bazz")
    else:
        print(i)
   
