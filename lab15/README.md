# Лабораторна робота №15: Overview of Big Data Technologies

## 2.2 Мета
Коротко опишіть мету лабораторної роботи та очікувані результати.

Метою цієї лабораторної роботи є ознайомлення з основними технологіями обробки великих даних за допомогою Python. Очікувані результати включають вміння очищувати, фільтрувати, нормалізувати та обробляти текстові та числові дані, використовуючи вбудовані функції та регулярні вирази.

## 2.3 Опис завдання
Детально опишіть завдання, яке потрібно виконати.

Завдання, які потрібно виконати, включають:

1. **Очищення даних**: Написати функцію `clean_data()`, яка приймає довгий рядок даних, розділених комами, та використовує `map()`, щоб повернути список, де кожен елемент очищено від пробілів і переведено у нижній регістр.
2. **Фільтрація електронних адрес**: Створити функцію `filter_emails()`, яка приймає рядок, що містить електронні адреси, та використовує регулярні вирази для повернення списку, що містить лише дійсні електронні адреси (ті, що містять рівно один символ '@').
3. **Виділення ключових слів**: Написати функцію `extract_keywords()`, яка приймає довгий рядок слів та використовує `filter()`, щоб повернути список слів, що довші за задану довжину.
4. **Обробка текстових даних**: Написати функцію `process_text()`, яка приймає довгий рядок текстових даних, використовує `map()` для очищення від пробілів, видалення спеціальних символів і перетворення у нижній регістр, потім використовує `filter()`, щоб повернути список без порожніх або дуже коротких елементів.
5. **Нормалізація даних**: Написати функцію `normalize_data()`, яка приймає довгий рядок числових значень, розділених комами, і нормалізує їх до діапазону між 0 та 1 на основі максимального значення.
6. **Конкатенація рядків**: Розробити функцію `concatenate_strings()`, яка приймає декілька рядків, розділених спеціальним символом, і об'єднує їх в один рядок без роздільника.
7. **Сума числових рядків**: Створити функцію `sum_numeric_strings()`, яка приймає рядок, що містить числа, розділені комами, і обчислює їх загальну суму.
8. **Фільтрація чисел**: Написати функцію `filter_numbers()`, яка відфільтровує числа з рядка, що перевищують заданий поріг.
9. **Зведення до квадрату**: Створити функцію `map_to_squares()`, яка приймає рядок чисел, переводить їх у квадрати і повертає їх у вигляді списку.
10. **Реверс рядків**: Розробити функцію `reverse_strings()`, яка приймає рядок слів, розділених комами, і перевертає кожне слово.

## 2.4 Виконання роботи
Опишіть кроки, які було виконано для досягнення мети. Включіть таку інформацію:
- Кожна лабораторна робота повинна бути завантажена у окрему папку на GitHub.
- Назва папки повинна містити номер лабораторної роботи (наприклад, lab14).
- Кожна папка повинна містити наступні файли:
  - Основний програмний код (наприклад, `main.py`).
  - Файл README з детальними поясненнями.
  - Структуру проєкту.
  - Опис кожного файлу та його призначення.
  - Опис основних функцій та методів з поясненням їх роботи.
  - Приклади використання.

### Приклад кроків:
1. Створені функції для кожного завдання, як описано в Описі завдання.
2. Протестовано кожну функцію з прикладами вхідних даних для забезпечення коректності.
3. Завантажено лабораторну роботу у папку з назвою `lab14` на GitHub.
4. Включено всі необхідні файли та описи у папку.

## 2.5 Результати
Опишіть отримані результати та додайте скріншоти або приклади виведення програми.

Отримані результати включають успішну реалізацію та тестування різних операцій з великими даними. Нижче наведені приклади виведення програми:

### Завдання 1: Очищення даних
```python
def clean_data(data):
    if isinstance(data, str):
        data = data.split(',')
    cleaned = [item.strip().lower() for item in data]
    return cleaned

data = " Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned)  # ['apple', 'banana', 'orange']
```

### Завдання 2: Фільтрація електронних адрес
```python
def filter_emails(emails_string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    valid_emails = re.findall(pattern, emails_string)
    valid_emails_list = [email for email in valid_emails if email.count('@') == 1]
    return valid_emails_list

emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails)  # ['test@example.com', 'example@test.co']
```

### Завдання 3: Виділення ключових слів
```python
def extract_keywords(words, min_length):
    return [word for word in words.split() if len(word) > min_length]

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words)  # ['apple', 'banana']
```

### Завдання 4: Обробка текстових даних
```python
def process_text(texts):
    def clean_text(text):
        text = text.strip().lower()
        text = re.sub(r'[^a-zA-Z]', '', text)
        return text
    return [text for text in map(clean_text, texts.split(',')) if text]

texts = " Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print(processed_texts)  # ['hello', 'yes', 'no']
```

### Завдання 5: Нормалізація даних
```python
def normalize_data(numbers):
    numbers_list = [float(num) for num in numbers.split(',')]
    max_value = max(numbers_list)
    normalized = [round(num / max_value, 3) for num in numbers_list]
    return normalized

numbers = "10, 20, 30"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers)  # [0.333, 0.667, 1.0]
```

### Завдання 6: Конкатенація рядків
```python
def concatenate_strings(data, separator):
    return ''.join(data.split(separator))

data = "hello*world*again"
concatenated = concatenate_strings(data, '*')
print(concatenated)  # 'helloworldagain'
```

### Завдання 7: Сума числових рядків
```python
def sum_numeric_strings(numbers):
    numeric_strings = [num for num in re.findall(r'-?\d+\.?\d*', numbers) if num]
    return sum(map(int, numeric_strings))

numbers = "1, 2, test, 3, 4"
total_sum = sum_numeric_strings(numbers)
print(total_sum)  # 10
```

### Завдання 8: Фільтрація чисел
```python
def filter_numbers(input_string, threshold):
    numbers_list = [int(num) for num in re.findall(r'\d+', input_string)]
    filtered_numbers = [num for num in numbers_list if num > threshold]
    return filtered_numbers

numbers = "10 test 30 40"
filtered = filter_numbers(numbers, 25)
print(filtered)  # [30, 40]
```

### Завдання 9: Зведення до квадрату
```python
def map_to_squares(numbers):
    return [int(x) ** 2 for x in numbers.split(',')]

numbers = "1, 2, 3, 4"
squared_numbers = map_to_squares(numbers)
print(squared_numbers)  # [1, 4, 9, 16]
```

### Завдання 10: Реверс рядків
```python
def reverse_strings(words):
    return [word[::-1] for

 word in words.split(',')]

words = "apple,banana,carrot"
reversed_words = reverse_strings(words)
print(reversed_words)  # ['elppa', 'ananab', 'torrac']
```
## Структура проєкту
```
lab14/
├── student_main.py
├── README.md
```

### `student_main.py`
Містить реалізацію всіх функцій, необхідних для виконання завдань лабораторної роботи.

### `README.md`
Надає детальні пояснення про проєкт, включаючи опис кожного файлу, основних функцій та їх роботи, а також приклади використання.
