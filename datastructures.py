simple_list =[1,2,3,4]
simple_list.extend([5,6,7])
del simple_list[0]
print (simple_list)

d = {'name': 'Isurika'}  # dictionary
print(d.items())
for k, v in d.items():
    print(k, v)
del(d['name'])

t = (1,2,3)   # tuple
print(t.index(1))
#del(t[0]) a tuple is immutable
print(t)

s = {'Isurika', 'Anna', 'Isurika'} # set
#del(s['Isurika']) a set is mutable but doesn't support deletion, use discard
print(s)