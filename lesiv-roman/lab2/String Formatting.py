data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s." #%s — означає, що на його місце буде підставлено значення у вигляді рядка.
print(format_string % data)