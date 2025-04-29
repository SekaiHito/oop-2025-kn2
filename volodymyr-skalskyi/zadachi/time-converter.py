seconds = int(input())
days = seconds // (24 * 60 * 60)
seconds %= 24 * 60 * 60
hours = seconds // (60 * 60)
seconds %= 60 * 60
minutes = seconds // 60
seconds %= 60
print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s).") 