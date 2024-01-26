users = {'Lenny': 'active', 'kariuki': 'inactive', 'kamau': 'active', 'peter': 'inactive'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
