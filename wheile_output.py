""" # while ループ 
実務ではそんなに使わないかも
forループでは実行しづらいときにwhile を使うと簡単にできたりする
# break(ループを終了) と continue(次のループに異動、書くと親切)
# 注意
無限ループを作らない。（条件がFALSE or breakのところを作る。）
 """
#challenge リファクタリング

age = int(input("何歳ですか？:"))
casino_age = 18
game_text = """プレイするゲームを選択してください. 
1: ルーレット
2: ブラックジャック 
3: ポーカー
:"""

if age >= casino_age:
    print("どうぞお入りください")
    while True:
        game = input(game_text)
        if game == '1':
            print("あなたはルーレットを選びました")
            break
        elif game == '2':
            print("あなたはブラックジャックを選びました")
            break
        elif game == '3':
            print("あなたはポーカーを選びました")
            break
        else:
            print("1~3を選んでください")
else:
    print("{}歳未満の方はカジノへは入れません！".format(casino_age))