my_dict = {'Alexandra': 2019, 'Elizaveta': 2021}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Alexandra'])
print('Not existing value: ', my_dict.get('Avrora'))
my_dict.update({'Avrora': 2019, 'Agata': 2019})
a = my_dict.pop('Agata')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)

my_set = {5, 'books', True, 5, 'books', True}
print('Set: ', my_set)
my_set.add('newspapers')
my_set.add (10)
my_set.discard(True)
print('Modified set: ', my_set)