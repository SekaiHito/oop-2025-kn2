```python
a = object()
b = object()
a_list = [a] * 5
b_list = [b] * 5
combined_list = a_list + b_list

print("a_list contains %d objects" % len(a_list))
print("b_list contains %d objects" % len(b_list))
print("combined_list contains %d objects" % len(combined_list))

if a_list.count(a) == 5 and b_list.count(b) == 5:
    print("Perfect!")
if combined_list.count(a) == 5 and combined_list.count(b) == 5:
    print("Nice work!")
