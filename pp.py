#from bs4 import BeautifulSoup
#from urllib.request import urlopen
#my_address="http://www.lsfx.pudong-edu.sh.cn/infoweb/"
#html_page=urlopen(my_address)
#html_text = html_page.read().decode('gbk')
#my_soup=BeautifulSoup(html_text)
#print(my_soup.get_text())
#print(html_text)


from random import randint
print(randint(0,2))

score=[('zbx',81,87.5,91),('wax',91,95,93),('ccj',81,92,92)]
score=sorted(score,key=lambda d:d[3],reverse=False)
print(score)
5

#job=input("what's your job")
#print("Your job is:",job)

a='Holly World,I am james'
print(a)
a=['Holly World','I am james']
print(a)
print(a[1])
a[1]='Hello World'
print(a)

Name=['Tom scored %s points','James scored %s points']
Tom=80
James=100
print(Name[0] % Tom)
print(Name[1] % James)
Name=['Tom scored %s points','James score%s points','Peter scored %s points']
Tom=80
James=100
Peter=90
print(Name[1]%Tom)
Name=['Tom scored 80 points','James scored 100 points','Peter scored 90 points']
Name.append('Danny scored 95 points')
print(Name)
del Name[2]
print(Name)
a1=[1]
a2=['Tom']
print(a1+a2)
a3=(a1+a2)
print(a3)
print(a3*5)

favorite_sports={'Tom':'Basketball',
                 'James':'Football',
                 'Peter':'Bedminton'}
print(favorite_sports['James'])
del favorite_sports['Tom']
print(favorite_sports)
favorite_sports['Tom']='Volleyball'
print(favorite_sports)

games=('play football')
foods=('chicken')
favorits=(games +' '+ foods)
print(favorits)

import turtle
t=turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

t.reset()
t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)

t.reset()
t.forward(100)
t.left(90)
t.forward(80)
t.left(90)
t.forward(100)
t.left(90)
t.forward(80)
t.left(90)

t.reset()
t.forward(70)
t.left(135)
t.forward(50)
t.left(90)
t.forward(50)
t.left(45)

age=20
if age<=15:
    print('You are too yound!')
    print('You are a yound student')
else:
    print('Why')

a=None
print(a)

age='20'
if age==15:
    print('You are too yound!')
    print('You are a yound student')
age='10'
converted_age=int(age)
if converted_age==10:
    print('You are too yound!')
    print('You are a yound student')

age='10.5'
converted_age=float(age)
print(converted_age)

money=2000
if money>1000:
    print("I'm rich!!")
else:
    print("I'm not rich!!")
    print("BUt I might be later...")

age=500
if age>=100:
    print('not less not more')

if money<500 and money >100:
    print('Too less')
elif money<5000 and money>1000:
    print('soso')
ninjas=30
if ninjas==50:
    print('Too more')
elif ninjas==30:
    print('some chanllenge,but i can handle')
elif ninjas==10:
    print('I can beat ninjas')

for x in range(0,5):
    print('hello')

print(list(range(10,20)))

x=2
print('hello%s'% x) 

x=22
print('hello%s' % x)

a=('A')
for b in a:
    print(a)

#a=1
#b=2
#while a<1000 and b<1000:
    #a=a+3.1415926
    #b=b+3.1415926
    #print(a,b)

for x in range(0,20):
    print('holle %s'% x)
    if x<9:
        break

a=0
while a<10:
    a=a+2
    print(a)

ingredients=['snails','leeches','gorilla belly-button lint',
             'caterpillar eyebrows','cent ipede toes']
for x in ingredients:
    print(x)

for x in range(0,5):
    print(x+1,ingredients[x])
   

a=40
year=1
b=0
while year<15:
    b=a*0.165
    print(year,a,b)
    a=a+1
    year=year+1


def pp(myname,old):
    print('hello % s age % s'%(myname,old))
pp('James','10')

def old(two,twelve,three,one):
    return two+twelve-three-one
print(old(2,12,3,1))

def old():
    first_old=2
    second_old=5
    return first_old*second_old
print(old())

first_old=2
def old2():
    second_old=5
    third_old=0
    return first_old*second_old+third_old
print(old2())

def first(old):
    first_old=0
    for year in range(1,11):
        first_old=first_old+old
        print('Year %s=%s old'%(year,first_old))
first(1)

import time
print(time.asctime())

import sys
def my_old():
    print('How old are you')
    old=int(sys.stdin.readline())
    if old <=15 and old >=9:
        print('What')
    else:
        print('Huh')
my_old()

print('Holle')
temp=input('Guess what I thoughy is what number:')
guess=int(temp)
while guess!=2:
    temp=input('No,please guess again')
    guess=int(temp)
    if guess==2:
         print('How did you guess?')
    else:
        if guess>2:
            print('Big')
        else:
            print('Small')
print('Finally guessed')
    
def pp():
    print('10 years old')
    print('English name is James')
pp()

#import os
#os.mkdir('/Users/pp/Desktop/666666')

import random
secret = random.randint(1,10)
print(secret)

import os
print (os.listdir('/Users/pp/Desktop/'))

import random
f = open('/Users/pp/Desktop/666666/pp.txt','w')
for i in range(0,10):
    for i in range(0,10):f.write(str(random.randint(0,9)))
f.write('\n')
f.close()

try:
    f = open('HaHa.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('T_T\n Because:' + str(reason))
