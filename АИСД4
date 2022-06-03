def knapsack(cap, values, weights):
    items = []                        #список, в котором будут находиться элементы в отсортированном виде
    for i in range(len(values)):      #перебор списка values
        itemInfo = {
            'vpw': values[i] / weights[i],     #стоимость на единицу веса
            'weight': weights[i]               #для проверки( поместится ли элемент целиком)
        }
        if len(items) == 0:                 #если количество предметов 0, добавляем этот элемент
            items.append(itemInfo)
        else:
            k = 0           #добавляем новый элемент
            while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
                k += 1
            items.insert(k, itemInfo)
    total = 0       #финальная стоимость груза, который удастся унести
    capacity = cap  #переменная для отслеживания, груз какого веса еще можно добавить в рюкзак после добавления очередного предмета.
    for item in items: #перебор всех предметов
        if capacity - item['weight'] >= 0:       #
            total += item['weight'] * item['vpw']
            capacity -= item['weight']
    return total


cap = 400
values = [60, 100, 120, 300, 50, 48,90 ]
weights = [20, 50, 30, 30, 2, 4, 30]
print(knapsack(cap, values, weights))
