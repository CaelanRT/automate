def display_inventory(inventory):
    count = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        count += v
    print('Count: ' + str(count))

def add_to_inventory(inventory, added_items):
    
    for item in added_items:
        if item in inventory.keys():
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)