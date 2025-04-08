s = "Hello, World!"

first_char = s[0]
print("Перший символ:", first_char)

substring = s[7:12]
print("Підрядок 'World':", substring)

print("Символи рядка:")
for char in s:
    print(char, end=' ')
print()

if 'W' in s:
    print("Символ 'W' присутній у рядку")