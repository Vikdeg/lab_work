numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_1 = numbers[:4] # слайсирование до none
numbers_2 = numbers[5:] # слайсирование после none
sum_numbers = sum(numbers_1 + numbers_2)
len_numbers = len(numbers) # количество элементов с none
none_ = sum_numbers/len_numbers # расчет none путем сред.ариф.
numbers[4] = none_
print("Измененный список:", numbers)