from multiprocessing import cpu_count


demo:list = [1, 'hello', True]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))
# print(type(numbers_list))

# r = list(range(1, 10))
# print(r)

# print(len(demo))
# print(colors[1])
# print('violet' in colors)

# print(dir(colors))

#colors.append('violet')
#colors.extend(['orange', 'black'])

#colors.insert(1, 'violet')
colors.insert(len(colors), 'violet')    

#colors.pop(0)

#colors.remove('red')
#colors.clear()
#colors.sort()





print(colors)
