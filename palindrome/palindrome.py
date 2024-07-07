from collections import deque

def is_palindrome(s):
    # видаляємо пробіли та приводимо до нижнього  регістру

    s = ''.join(filter(str.isalnum, s)).lower()

    # заповнюємо двостороню чергу

    char_deque = deque(s)

    # перевіряємо на паліндром

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
        
    return True


# приклади використання
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("No lemon, no melon"))           # True
print(is_palindrome("Hello, world!"))                # False