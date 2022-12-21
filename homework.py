import re

# people = ['Abraham Lincoln\n', 'Andrew P Garfield\n', 'Connor Milliken\n', 
#           'Jordan Alexander Williams\n', 'Madonna\n', 'programming is cool\n']

def catalogue_names():

    with open ('regex_test.txt') as file:
        data = file.read()

    pattern = re.compile(r"""(?P<Group>([A-Z][a-z]+).+([A-Z][a-z]+))""")

    for item in pattern.finditer(data):
        # print(item)
        match = item.group('Group')
        if match:
            print(match)
        else:
            print("None")

catalogue_names()

# people = ['Abraham Lincoln\n', 'Andrew P Garfield\n', 'Connor Milliken\n', 
#           'Jordan Alexander Williams\n', 'Madonna\n', 'programming is cool\n']

# def catalogue_names():
#     names_pattern = re.compile("[A-Z][a-z]+).+([A-Z][a-z]+$")
    
#     for item in people:
#         match = names_pattern.match(people)
#         if match:
#             print(people)
#         else:
#             print("None")
            
# catalogue_names()
# , re.M|re.X
