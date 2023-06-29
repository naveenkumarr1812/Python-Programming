# dictionary = A changeble, unordered collection of unique key:value pairs
#             Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'berlin'})
capitals.pop('China')
# capitals.clear()

print(capitals['Germany'])          # if not exist, it return error
print(capitals.get('Germany'))      # if not exist, it return None(Useful)
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for x in capitals.items():
    print(x)

