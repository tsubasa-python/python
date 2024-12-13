d = {"apple": 1, "banana": 2, "orange": 3}
d["apple"] = 0
print(d)
d["みかん"] = 1
print(d)

d = {"apple": 1, "banana": 2, "orange": 3}
d.pop
popped_item = d.pop("みかん", "みかんは入っていません")
print(popped_item)
print(d)
