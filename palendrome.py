"""
1 занятие - Домашняя работа
4 задание
"""
def Palindrome(word):
    f_palindrom = True
    for i in range(len(word)//2):
        if word[i] == word[len(word)-1-i]: continue
        f_palindrom = False
    return f_palindrom

print(Palindrome('лепсспел'))  # True
print(Palindrome('helloworld'))  # False
print(Palindrome('level'))  # True
print(Palindrome('racecar'))  # True
print(Palindrome('python'))  # False