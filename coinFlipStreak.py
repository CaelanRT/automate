import random


streak_count = 0
h_streak = ['H', 'H', 'H', 'H', 'H', 'H']
t_streak = ['T', 'T', 'T', 'T', 'T', 'T']

# function to get a random head or tail
def get_hot():
    num = random.randint(0,1)
    if num == 0:
        return 'H'
    else:
        return 'T'
    
# function to check for a streak
def check_streak(list, h_streak, t_streak):
    flag = 0
    for i in range(len(list) - 5):
        new_slice = list[i:i+6]
        if new_slice == h_streak:
            flag = 1
            break
        elif new_slice == t_streak:
            flag = 1
            break
    return flag



# experiments loop
for experiment_number in range(10000):

    hot_list = []
    #code to populate list
    for i in range(100):
        hot_list.append(get_hot())

    #code to check for streak and return streak count
    streak_count += check_streak(hot_list, h_streak, t_streak)

print('Chance of streak: %s%%' % (streak_count / 10000 * 100))