#Test001 : 1105201318 
'''
import os
import secrets

random_hex = secrets.token_hex(8)
print(random_hex)

pth0 = '/usr/bin/python3.6 /home/slimed/Desktop/Flask/Flask_Blog/' 
fn0 = pth0 + 'Test.py'
_, file_ext = os.path.splitext(fn0)
picture_fn = random_hex + file_ext

print(picture_fn)

build_picture_flnm = lambda flnm : secrets.token_hex(8) + os.path.splitext(flnm)[1]
build_picture_path = lambda flnm: os.path.join(pth0, 'static/profile_pics', build_picture_flnm(flnm))

print(build_picture_flnm(fn0))
print(build_picture_path(fn0))
'''

#Test002 1105201338
'''
# Python code to illustrate delattr() 
class Geek: 
  stu1 = "Henry"
  stu2 = "Zack"
  stu3 = "Stephen"
  stu4 = "Amy"
  stu5 = "Shawn"
  
names = Geek() 
  
print('Students before delattr()--') 
print('First = ',names.stu1) 
print('Second = ',names.stu2) 
print('Third = ',names.stu3) 
print('Fourth = ',names.stu4) 
print('Fifth = ',names.stu5) 
  
# implementing the method 
#delattr(Geek, 'stu5') 

# implementing the operator 
del Geek.stu5 
  
  
print('After deleting fith student--') 
print('First = ',names.stu1) 
print('Second = ',names.stu2) 
print('Third = ',names.stu3) 
print('Fourth = ',names.stu4) 
# this statement raises an error 
#print('Fifth = ',names.stu5) 
'''


#Test003 14224587
'''
<!--                01111000    00110011    11100100
    n field         Register    Login       Account
    1 infos         0           0           1
    2 name          1           0           1
    3 email         1           1           1
    4 pass          1           1           0
    5 confirm       1           0           0
    6 picture       0           0           1
    7 remember      0           1           0
    8 forget        0           1           0
-->

code_forms = { 'register':'01111000', 'login':'00110011', 'account':'11100100'}
fields = ['infos', 'name','email','pass','confirm','picture','remmeber','forget']
print(code_forms['register'][fields.index('confirm')])
'''
