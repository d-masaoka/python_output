# dictionary: キーと値の組み合わせを複数保持するデータ型 順番に保持しているわけではない

fruits_colors = {'apple': 'red', 'lemon': 'yellow'}
print(fruits_colors)

# []にキーを指定して値を取得する
fruit_key = 'apple'
print(f"{fruit_key} is {fruits_colors[fruit_key]}")

# .keys()
for fruit in fruits_colors.keys():
    print(fruit)

# .values()
for color in fruits_colors.values():
    # 通常値からキーを取得するのにdictionaryは使えないので，colorだけprint()しておく
    print(color)

# .items() よく使う
for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}")



age = int(input("何歳ですか？:"))
casino_age = 18
game_text = "プレイするゲームを選択してください." 
game_dict = {"1": "ルーレット", "2": "ブラックジャック ", "3": "ポーカー"}


if age >= casino_age:
    print("どうぞお入りください")
    while True:
        print("プレイするゲームを選択してください。")
        for num, game_name in game_dict.items():
            print(f"{num}:{game_name}")
        game = input(f":")
        if game in game_dict :
            print(f"あなたは{game_dict[game]}を選びました")
            break
        else:
            print("1~3を選んでください")
            
else:
    print(f"{casino_age}歳未満の方はカジノへは入れません！")