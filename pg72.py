# syntax sugar
# функция высшего порядка map и filter
users=[
    {'name':'David', 'age': 25},
    {'name':'Matie', 'age': 24},
    {'name':'Iuliia', 'age': 23},
    {'name':'Nina', 'age': 22},
]

filtered_users= filter (lambda u:23<u['age']>24, users)
print(list(filtered_users))

# a=
#
# lambda a,b,: a+b
