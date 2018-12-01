"""person = "   Jamiul Alam    "
print('_' + person + '_')
print('_' + person.lstrip() + '_')
print('_' + person.rstrip() + '_')
print('_' + person.strip() + '_')# Remove All Space"""
#Slice
name = 'Jamiul'
for n in range(len(name)):
    even = name[::2]
    odd = name[1::2]

print(even)
print(odd)
