# Лабораторна робота №17: Generators and Data structures

## Мета роботи

Метою цієї лабораторної роботи є розробка та реалізація різноманітних генераторних функцій на мові Python для ефективної обробки та генерації послідовностей даних. Очікувані результати включають створення гнучких та ефективних генераторів, які дозволяють працювати з різними типами даних (списки, словники, файли, дерева, графи) та виконувати різні операції (фільтрація, трансформація, обхід структур даних).

## Опис завдання

Завдання полягає у створенні 35 генераторних функцій, які охоплюють широкий спектр задач:

1. Базові генератори для списків, рядків та файлів.
2. Генератори для математичних послідовностей (Фібоначчі, прості числа, факторіали).
3. Генератори для обходу дерев (pre-order, in-order, post-order).
4. Генератори для обходу графів (DFS, BFS).
5. Генератори для роботи зі словниками.
6. Генератори для комбінаторних задач (декартовий добуток, перестановки, комбінації).
7. Генератори для роботи з вкладеними структурами (списки, словники).
8. Генератори для математичних прогресій та послідовностей.
9. Генератори для обчислення накопичувальних сум та добутків.

## Виконання роботи

1. Реалізовано базові генератори:
   - `number_generator()`, `even_number_generator()`, `odd_number_generator()` для роботи зі списками.
   - `string_chars_generator()` для роботи з рядками.
   - `file_lines_generator()`, `file_words_generator()` для роботи з файлами.

2. Створено математичні генератори:
   - `fibonacci_generator()`, `prime_number_generator()`, `factorials_generator()`.
   - `squares_generator()`, `cubes_generator()`, `powers_of_two_generator()`, `powers_of_base_generator()`.

3. Реалізовано генератори для обходу дерев та графів:
   - `pre_order_traversal()`, `in_order_traversal()`, `post_order_traversal()` для бінарних дерев.
   - `dfs_traversal()`, `bfs_traversal()` для графів.

4. Створено генератори для роботи зі словниками:
   - `dict_keys_generator()`, `dict_values_generator()`, `dict_items_generator()`.
   - `nested_dict_generator()` для вкладених словників.

5. Реалізовано генератори для комбінаторних задач:
   - `cartesian_product_generator()`, `permutations_generator()`, `combinations_generator()`.

6. Створено генератори для роботи з вкладеними списками та послідовностями:
   - `flatten_list_generator()`, `unique_elements_generator()`, `reverse_list_generator()`.
   - `geometric_progression_generator()`, `arithmetic_progression_generator()`.
   - `collatz_sequence_generator()`.

7. Реалізовано генератори для обчислення накопичувальних значень:
   - `running_sum_generator()`, `running_product_generator()`.

8. Додаткові генератори:
   - `tuple_list_generator()`, `parallel_lists_generator()`.

9. Проведено тестування всіх генераторів з різними вхідними даними.
10. Код завантажено у папку `lab17` на GitHub.

## Результати

Розроблені генераторні функції успішно виконують всі поставлені задачі. Приклади використання:

```python
# Робота зі списками
gen = number_generator([1, 2, 3, 4, 5])
print(next(gen))  # 1

# Математичні послідовності
gen = fibonacci_generator()
print([next(gen) for _ in range(5)])  # [0, 1, 1, 2, 3]

# Обхід дерев
root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
gen = in_order_traversal(root)
print(list(gen))  # [2, 1, 3]

# Робота зі словниками
gen = dict_items_generator({'a': 1, 'b': 2})
print(next(gen))  # ('a', 1)

# Комбінаторні задачі
gen = cartesian_product_generator([1, 2], ['a', 'b'])
print(list(gen))  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Робота з файлами (приклад тексту)
sample_text = "First line\nSecond line"
gen = file_lines_generator(sample_text.splitlines())
print(next(gen))  # 'First line'
```

## Висновки

Мета лабораторної роботи була успішно досягнута. Ми створили набір ефективних та гнучких генераторних функцій, які демонструють потужність та елегантність генераторів у Python. Ці функції дозволяють працювати з великими послідовностями даних без завантаження їх у пам'ять цілком, що покращує продуктивність та ефективність використання ресурсів.

Основні переваги використання генераторів:
1. Ефективність використання пам'яті: генеруються лише необхідні значення.
2. Можливість роботи з нескінченними послідовностями (`fibonacci_generator`).
3. Простота та читабельність коду.
4. Гнучкість у роботі з різними структурами даних.

## Інструкції з запуску

1. Вимоги: Python 3.6 або вище, стандартні бібліотеки (`itertools`, `collections`).
2. Запуск: Помістіть файл `student_main.py` у вашу робочу директорію та виконайте `python student_main.py`.

## Структура проєкту

```
lab17/
├── student_main.py
├── README.md
├── requirements.txt
```

### `student_main.py`

Містить реалізацію всіх 35 генераторних функцій. Основні категорії:

- Базові генератори: `number_generator()`, `file_lines_generator()`.
- Математичні генератори: `fibonacci_generator()`, `prime_number_generator()`.
- Генератори для структур даних: `pre_order_traversal()`, `dfs_traversal()`.
- Генератори для словників: `dict_keys_generator()`, `nested_dict_generator()`.
- Комбінаторні генератори: `cartesian_product_generator()`, `permutations_generator()`.
- Генератори послідовностей: `geometric_progression_generator()`, `running_sum_generator()`.

### `README.md`

Цей файл, який містить детальний опис лабораторної роботи, її мету, виконання, результати та інструкції.

### `requirements.txt`

Файл, який містить список всіх залежностей проєкту та їх версій. Для цієї лабораторної роботи він може бути порожнім, оскільки всі використані бібліотеки є стандартними.
