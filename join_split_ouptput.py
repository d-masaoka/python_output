# join
# リストと深い関わり有
# join string型が持っているメソッド
# 各単語をハイフン・スラッシュ・スペースでくっ付けたい時に使うことが多い。
text = " ".join(['Hi', 'My', 'name', 'is', 'Daisuke'])
print(text)

# split string型のメソッド。リストで返す
# 文字列の操作でよく使う

filename = 'sample.py'
print(filename.split(".")[0])