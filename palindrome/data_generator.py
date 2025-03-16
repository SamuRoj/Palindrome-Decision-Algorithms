import random
from palindrome import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    answer = []
    while len(answer) < size:
        answer.append(random.randint(0, limit))
    return answer


def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)


def generate_random_string(size):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(characters) for _ in range(size))

def generate_palindromes(size, samples_by_size, isPalindrome):
    strings = []
    for _ in range(samples_by_size):
        palindrome_chance = isPalindrome
        
        if palindrome_chance:
            half = generate_random_string(size // 2)
            palindrome = ""
            if size % 2 == 0:
                palindrome = half + half[::-1]  
            else: 
                half + random.choice('abcdefghijklmnopqrstuvwxyz') + half[::-1]
            strings.append(palindrome)
        else:
            non_palindrome = generate_random_string(size)
            strings.append(non_palindrome)
    
    return strings


def generate_palindromes_and_non_palindromes(size, samples_by_size):
    strings = []
    for _ in range(samples_by_size):
        length = random.randint(0, size)
        palindrome_chance = random.choice([True, False])
        
        if palindrome_chance:
            half = generate_random_string(length // 2)
            palindrome = ""
            if length % 2 == 0:
                palindrome = half + half[::-1]  
            else: 
                half + random.choice('abcdefghijklmnopqrstuvwxyz') + half[::-1]
            strings.append(palindrome)
        else:
            non_palindrome = generate_random_string(length)
            strings.append(non_palindrome)
        
    return strings