dummy_data_dict = {}
dummy_data_set = ()
dummy_data_tupple = ()
dummy_data_list =  [
    {"name": "Alice", "age": 25, "occupation": "Engineer"},
    {"name": "Bob", "age": 30, "occupation": "Doctor"},
    {"name": "Charlie", "age": 35, "occupation": "Artist"},
    {"name": "David", "age": 40, "occupation": "Teacher"},
    {"name": "Emma", "age": 27, "occupation": "Software Developer"},
    {"name": "Frank", "age": 32, "occupation": "Lawyer"},
    {"name": "Grace", "age": 45, "occupation": "CEO"},
    {"name": "Hannah", "age": 29, "occupation": "Nurse"},
    {"name": "Ian", "age": 38, "occupation": "Chef"},
    {"name": "Jenny", "age": 33, "occupation": "Marketing Manager"}
]

""" 
Todo 

[mid-level]

-filter all people that are older than > 20
-the filter should be an dicdtionary

-do the same but for this time do with tupples 

-create a structure like this {Grace: {age: 23, occupation: Check}}, so create a new array having this order 
"""

"""
[Advanced]
-cover more advance features of comprehension by using comprehensions inside another comprehension 
- inner for loop  inside comprehension
"""


"""
[Advanced]
-Filte in combination with comprehensions 
-map in combination with comprehensions
-reducer in combination with comprehensions

"""

1,2,3,4,5
5,4,3,1,2
pairs = [(name1, name2) for name1 in [person['name'] for person in people[:3]] for name2 in [person['name'] for person in people[-3:]]]
print(pairs)