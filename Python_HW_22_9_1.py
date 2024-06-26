# Функция сортировки массива чисел по возрастанию  методом слияния
def sort_merge(array):
    if len(array) == 1:            # Если одиночный элемент -
        return array               # возвращаем его же;
    elif len(array) == 2:          # Если 2 элемента
        if array[0]>array[1]:         # не по возрастанию -
            array[0], array[1] = array[1], array[0]  # меняем местами;
        return array               # Возвращаем отсортированную часть;

    mdl = len(array) // 2             # Если элементов больше 2  - определяем индекс,
                                # делящий массив на 2 (примерно или точно) равных части;
    al = sort_merge(array[:mdl])    # Сортируем каждую
    ar = sort_merge(array[mdl:])    # часть деленного массива;
    b = []                      # Создаем результирующий массив;
    il = 0                      # Инициализируем индексы текущих элементов
    ir = 0                      # для каждой части массива;
    while True:
        if al[il] < ar[ir]:     # Если текущий элемент левой части < элемента правой части -
            b.append(al[il])    # добавляем его к результирующему массиву,
            il += 1             # указываем следующий элемент левой части;
            if il == len(al):   # Если это был последний элемент в левой части,
                return b + ar[ir:]  # то добавляем остаток правой части к результирующему массиву и
                                    # возвращаем его;
        else:                   # Если текущий элемент правой части <= элемента правой части -
            b.append(ar[ir])    # добавляем его к результирующему массиву,
            ir += 1             # указываем следующий элемент правой части;
            if ir == len(ar):   # Если это был последний элемент в правой части,
                return b + al[il:]  # то добавляем остаток левой части к результирующему массиву и
                                    # возвращаем его;
#--------------------------------

# Функция двоичного поиска значения меньше заданного
def b_search_less(array, element, left, right):
    if left > right:    # если левая граница превысила правую,
         return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if element <= array[middle]:  # если элемент <= элемента в середине,
        if element > array[middle-1]:   # но > предыдущего
            return middle-1             # возвращаем позицию предыдущего
                                        # (если это был первый элемент массива, то сравнивается
                                        # с последним, а так как список отсортирован, то сравнение False)
        return b_search_less(array, element, left, middle - 1) # иначе рекурсивно ищем в левой половине
    else:                           # если элемент > элемента в середине,
        if middle + 1 >= len_array:    # проверяем, не выходим ли за правую границу,
            return False                # если выходим, возвращаем False, иначе
        if element < array[middle+1]:   # если элемент > элемента в середине, но < следующего
            return middle               # возвращаем позицию элемента
        return b_search_less(array, element, middle + 1, right) # рекурсивно ищем в правой половине
#--------------------------------

# Основная программа

input_str = input("Введите несколько десятичных чисел через пробел: ")
try:        # Проверяем, что введены десятичные числа
    sl = list(map(float , input_str.split()))   # Преобразуем входную строку в список десятичных чисел
except:     # Если это не так - сообщение об ошибке и закончить программу
    print("Ошибка: во входных данных указны некорректные значения.")
    exit(1)
try:           # Проверяем, что введено десятичное число
    input_num = float(input("Введите любое десятичное число: ")) # Преобразуем в десятичное число
except:     # Если это не так - сообщение об ошибке и закончить программу
    print("Ошибка: введено некорректное значение.")
    exit(1)

sl_sorted = sort_merge(sl)      # Сортируем массив
len_array = len(sl_sorted)      # Длина массива
ind_num = b_search_less(sl_sorted, input_num, 0, len_array - 1)
if ind_num:
    print("Позиция подходящего элемента: ", ind_num)
else:
    print("Введенное число не имеет подходящего элемента в указанном массиве.")
