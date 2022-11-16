a=0
q=int(input('1)2*2=? '))
if q==4:
    a+=1

w=int(input('2)25*25=? '))
if w==625:
    a+=1

e=int(input('3)100-81=? '))
if e==19:
    a+=1

r=int(input('4)1000-7=? '))
if r==993:
    a+=1

t=int(input('5)19+45-23=? '))
if t==41:
    a+=1

y=int(input('6)81/9=? '))
if y==9:
    a+=1

u=int(input('7)50+50+50+50+50+50=? '))
if u==300:
    a+=1

i=int(input('8)741-1-40-700=? '))
if i==0:
    a+=1

o=int(input('9)1000/250=? '))
if o==4:
    a+=1

p=int(input('10)1*2*3*4*5*6*7=? '))
if p==5040:
    a+=1

if 8<=a:
    print('вы молодец')
elif 5<=a:
    print('удвертительно')
else:
    print('повез в следущий раз')