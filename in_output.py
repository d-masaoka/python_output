# in 演算子
# キー in オブジェクト(list, 辞書)
fruits = ['apple', 'peach', 'greapes', 'banana']
""" print('apple' in fruits)
print('apple' not in fruits)
print('lemon' not in fruits)
print('lemon' in fruits) """

# Challenge

# ユーザーに好きなフルーツを入力してもらう
input_text = input('好きなフルーツを入力してください。')
# 入力したフルーツがリストにあればそのフルーツを削除
if input_text in fruits:
    fruits.remove(input_text)
    print(f"{input_text}をどうぞ。残りは{fruits}です。")
# 入力したフルーツがリストになければ入力されたフルーツを追加
else:
    fruits.append(input_text)
    print(f"{input_text}を補充しました。今ある果物は{fruits}です。")