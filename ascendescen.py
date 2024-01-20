fh=open('output8.txt','w')
a= [3,1,4,5,9,2,11,13]

print('list:', a)
fh.write(f'given list is {a}')
a.sort()
print('In ascending order:', a)
fh.write(f'\nlist in ascending order is {a}')
a.sort(reverse=True)
print('In descending order:',a)
fh.write(f'\nlist in descending order is {a}')
fh.close()