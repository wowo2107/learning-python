bag = ['A','B','C','D','E','F','G']
print(bag)
print(len(bag))
print(bag[0],bag[1],bag[2],bag[3],bag[4],bag[5],bag[6])
print(bag[-1],bag[-2],bag[-3],bag[-4],bag[-5],bag[-6],bag[-7])
bag.append('喵')
print(bag)
bag.insert(1,'a')
bag.insert(3,'b')
print(bag)
bag.pop()
print(bag)
bag.pop(1)
bag.pop(2)
'''这里如果是bag.pop（3）,会删掉C而非b，因为删了a之后，各个元素的索引变了'''
print(bag)
tuple = (1,)
'''tuple是固定的有序列表，但是当只有一个元素时，会产生歧义，被认为是普通的变量，故而加个逗号区分'''

'''万能的py也有吃瘪的时候啊，毕竟自动定义的话难免会有歧义的'''

'''tuple虽然不能修改，但是其中的元素list中的元素是可以修改的'''

'''
age = input('enter ur age plz:')
age = int(age)
if age >= 18:
    print(f'your age is {age},\nadult')
elif age >=6:
    print(f'your age is {age},\nteenager')
else:
    print(f'your age is {age},\nkid')
'''

n=0
for name in bag:
    n=n+1
    print(n,name)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

'''是不是c里的那种for(x = 0;x <= 100;x++);这种代码，在py里就，for x in range（101）。
总觉得不知道为什么，py里的for循环总觉得是依赖于range函数，感觉有很多限制不过对比而言，c也算是依赖特定的函数吧。'''

sum1 = 0
n1 = 1
while n1 <= 100:
    sum1=sum1 + n1;
    n1 = n1 +1;
print(sum1)
