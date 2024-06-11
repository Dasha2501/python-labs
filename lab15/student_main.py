import re

def clean_data(data):
    if isinstance(data, str):
        data = data.split(',')
    cleaned = [item.strip().lower() for item in data]
    return cleaned

def filter_emails(emails_string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    valid_emails = re.findall(pattern, emails_string)
    valid_emails_list = [email for email in valid_emails if email.count('@') == 1]
    return valid_emails_list

def extract_keywords(words, min_length):
    return [word for word in words.split() if len(word) > min_length]

def process_text(texts):
    def clean_text(text):
        text = text.strip().lower()
        text = re.sub(r'[^a-zA-Z]', '', text)
        return text
    return [text for text in map(clean_text, texts.split(',')) if text]

def normalize_data(numbers):
    numbers_list = [float(num) for num in numbers.split(',')]
    max_value = max(numbers_list)
    normalized = [round(num / max_value, 3) for num in numbers_list]
    return normalized

def concatenate_strings(data, separator):
    return ''.join(data.split(separator))

def sum_numeric_strings(numbers):
    numeric_strings = [num for num in re.findall(r'-?\d+\.?\d*', numbers) if num]
    return sum(map(int, numeric_strings))

def filter_numbers(input_string, threshold):
    numbers_list = [int(num) for num in re.findall(r'\d+', input_string)]
    filtered_numbers = [num for num in numbers_list if num > threshold]
    return filtered_numbers

def map_to_squares(numbers):
    return [int(x) ** 2 for x in numbers.split(',')]

def reverse_strings(words):
    return [word[::-1] for word in words.split(',')]
