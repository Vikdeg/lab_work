list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

len_ = len(list_players) # количество людей в команде
len_2 = int(len_ / 2) # количество людей в 1 группе (всего 2 группы)

gang_1 = list_players[:len_2]
gang_2 = list_players[len_2:]

print(gang_1)
print(gang_2)