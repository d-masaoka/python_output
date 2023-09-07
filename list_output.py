# リストはオブジェクトであればなんでも入る。
# リスト内は0から始まる。
# リストの最後からは-1から始まる。
# シークエンシャル
fruits = ['apple', 'peach']
hetro_list = ['string', 1, 3.4, True, fruits]

""" print(hetro_list)
print(hetro_list[1]) """

'''
リスト型のメソッド
.append
.insert
.remove
.sort
len()
'''

# .append: 新しいオブジェクト(banana)を追加する
fruits.append('banana')
print(fruits)

# .insert: 指定したindexに指定したオブジェクトを追加する
fruits.insert(1, 'lemon')
print(fruits)

# .remove: マッチした最初のオブジェクトを除く
fruits.remove('banana')
print(fruits)

# .sort(): 昇順に並び替える
fruits.sort()
print(fruits)

# 降順にする
fruits.reverse()
print(fruits)

# len(): リストの要素数を取得する
print(len(fruits))


# "+"演算子でリストを結合する。
a = [2, 4, 6]
b = [8, 10, 12]
c = a + b
print(c)
#appendすると要素として追加。
a.append(b)
print(a)