stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    count = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        count += v
    print('Count: ' + str(count))

display_inventory(stuff)