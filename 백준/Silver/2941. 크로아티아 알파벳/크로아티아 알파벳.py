word = input()
cnt_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in (cnt_list):
    word = word.replace(i, '*')
    
print(len(word))