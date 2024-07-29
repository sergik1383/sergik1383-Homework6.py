my_dict= {'имя':'Сергей','Год рождения': 1983}
print(my_dict)
print(my_dict['имя'])
my_dict['месяц']=8
print(my_dict)
print(my_dict.get('пол'))
my_dict.update({'дочь':'Кира','Родилась в':2014})
print(my_dict)
a=my_dict.pop('дочь')
print(my_dict)
print(a)
my_set= {1,2,3,4,1,2,3,4,5,6,(4,3,2,1)}
print(my_set)
my_set.add(9)
my_set.add(8)
print(my_set)
my_set.discard(1)
print(my_set)




