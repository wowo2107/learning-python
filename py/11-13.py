'''wy = ['yue','wang','miao',6]
number = [1,2,3,4]
abc = [5,'b','c',6]
d = {1 : 5,'wang': 2 ,'yue': 3}
print(d[1])
print(d['yue'])
[print(k,v) for k,v in zip(wy,number)]
print(zip(wy,number))



mzz = classmates.get('mz', 'fake mz')

print(f"mz is {mzz}")
'''
classmates = {
    'wt': 'bkswt',
    'mz': 666
}


if 'mz' in classmates:
  mz = classmates['mz']
else:
  mz = 'fake mz'
print(f"mz is {mz}")
