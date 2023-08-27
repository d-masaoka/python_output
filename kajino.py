'''
challenge1
ユーザに年齢を聞き、18歳以上なら入れるカジノを作成する
challenge2: カジノに入ったらゲームを選べるようにする。
できるゲームは
1: ルーレット
2: ブラックジャック
3: ポーカー
選択後、ゲーム内容をprint()する。
'''
age_restriction = 18
age = int(input("年齢を教えてください"))
game_text = '''プレイするゲームを選んでください。
1: ルーレット
2: ブラックジャック
3: ポーカー
'''

if age >= age_restriction:
    print(f"{age}歳ですね。どうぞお入りください。")
    game = input(game_text)
    if game == "1":
        print("ルーレットを選択しました。")
    elif game == "2":
        print("ブラックジャックを選択しました。")
    elif game == "3":
        print("ポーカーを選択しました。")
    else:
        print("1~3の中で選択してください。")
    
else:
    print(f"{age}歳は18歳未満なので入場できません。")

