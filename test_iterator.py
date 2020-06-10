import itertools, zipfile, time
import concurrent.futures

options = 'abcdefghijklmnopqrstuvwxyz0123456789'
#combos made to range from 1 character to 8#
combos = itertools.product((options),repeat = 3)
# x = iter(combos)
# def printnext(it):
#     print(next(it))
#     return 0
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     result = [executor.submit(printnext, x) for _ in range(200)]
count = 0
for i in combos:
    print(i)
    count+=1
    if(count == 200): break

