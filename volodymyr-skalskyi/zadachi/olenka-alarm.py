t = int(input())
h = int(input())
m = int(input())
total_minutes = h * 60 + m + t
alarm_hours = total_minutes // 60
alarm_minutes = total_minutes % 60
print(alarm_hours)
print(alarm_minutes) 