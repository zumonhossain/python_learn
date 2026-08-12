items = ["onigiri", "tea", "bento"];

items.append("pudding");
items.remove("tea");

for i, item in enumerate(items, start=1):
    print(f"{i}. {item}");