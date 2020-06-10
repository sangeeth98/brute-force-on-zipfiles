import itertools, zipfile, time

file = open('perms.txt','w+')
options = 'abcdefghijklmnopqrstuvwxyz0123456789'
combos = itertools.product((options),repeat = 6)
for i in combos:
    file.write(''.join(i)+"\n")
