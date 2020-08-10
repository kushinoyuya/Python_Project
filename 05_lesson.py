print("##########演習5-1##########")
def display_investory(investory):
    print('持ち物リスト:')
    item_total = 0
    for k,v in investory.items():
        print(str(investory[k])+ ' ' + k)
        item_total += v
    print("アイテム総数：" + str(item_total))

stuff = {'ロープ':1, 'たいまつ':6, '金貨':42, '手裏剣':1, '矢':12}
display_investory(stuff)



print("##########演習5-2##########")
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
def add_to_investory(investory, added_items):
    for i in added_items:
        investory.setdefault(i, 0)
        investory[i] += 1
    return investory

inv = {'金貨': 42, 'ロープ': 1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
inv = add_to_investory(inv, dragon_loot)
display_investory(inv)
