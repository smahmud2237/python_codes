'''
1. Dictionary are unordered mappings for storing objects. Previously we saw how lists store objects in an ordered 
sequence, dictionary use a key-value pairing instead.
2. This key-value pair allows users to quickly grab objects without needing to know an index location.
3. Dictionary use curly braces and colons to signify the keys and their associated values like {'key1':'value1', 'key2':'value2'}
4. So when to choose a list and when to choose a dictionary?
=> Well, Dictionaries Objects retrived by key name. Unordered and can not be sorted. But Lists objects retrived by location. 
So, Lists Ordered sequence can be indexed or sliced.
'''
my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key1'])

prices_lookup = {'apple':'3.99', 'orange':'4.5', 'banana':'1.2', 'milk':'5.80'}
print(prices_lookup['milk'])

# inside a dictionary all types supported. Even dictionary in dictionary is allowed...
e = {'k1':123, 'k2':[0,1,'two'], 'k3':{'insideKey': 100}}
print(e['k2'])
print(e['k3']['insideKey'])
# update k1 and k2 values..
e['k1'] = 'Hello'
e['k2'][2] = 2
print(e)
# if wants to see all dictionary keys 
print(e.keys())
# if wants to see all keys values from dict
print(e.values())
# if wants to see all dictionary items 
print(e.items())




