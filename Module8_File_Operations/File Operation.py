
#======================= Operation on .txt file ============================

#import os

import os

os.getcwd() # Check current directory location

#Set the directory 
os.chdir('D:\\AA-SUNIL\\PROGRAMING AND DATABASE\\Programming\\Python\\My_Practice\\Program')

#Read .txt file 
newfile = open("C:\\Users\\HP\\Spyder\\Python_py.txt", "w+")

for i in range(1,10):
    print(i)
    newfile.write("\n Hello, Welcome to Python:") #Write in the file

newfile.close() #Close file

newfile = open("Python_Py.txt","r")

for i in range(1, 10):
    print(newfile.read())
    break

newfile.close()


# File methods

os.rename("Python_Py.txt","Python2.txt")

os.remove("Python2.txt")

os.listdir(os.getcwd())

os.mkdir('new')

os.chdir('C:\\Users\\SUNEEL PATEL\\Desktop\\py\\D3') 


#2.===================== Operation on .csv files =============================

fp = open("USArrests.csv", "r")
for line in fp:
    print(line)
    
print(fp.read())
fp.close()


import codecs

fp = codecs.open(os.path.join('C:\\Users\\SUNEEL PATEL\\Desktop\\py\\D2','worldcities.csv'), 'r')
cnt = 0
for line in fp:
    print (cnt)
    if cnt <= 10:
        print(line)
    else:
        break
    cnt += 1
fp.close()


os.rename('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2\\worldcities.csv', 
          os.path.join('C:\\Users\\SUNEEL PATEL\\Desktop\\','County.csv'))



wp = open(os.path.join('C:\\Users\\SUNEEL PATEL\\Desktop\\py\\D2\\', 'counry.DAT'), 'w')

rp = open(os.path.join('C:\\Users\\SUNEEL PATEL\\Desktop\\py\\D2','worldcities.csv'), 'r')
cnt = 0
for line in rp:
    if cnt <= 10:
        wp.write(line)
        wp.write('\n')
    else:
        break
    cnt += 1
rp.close()
wp.close()


for line in reversed(list(open(os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2','worldcities.csv'), 'r'))):
    print(line.rstrip())




d1 = {'fname': 'Steve', 'lname': 'Jobs'}
d2 = {'fname': 'Steve', 'lname': 'Jobs', 'age': 21}

import json
wp = open(os.path.join('C:\\Users\\SUNEEL PATEL\\Desktop\\py\\D2', 'test_new.json'), 'w+')
for x in range(3):
    if x == 0:
        wp.write(json.dumps(d1))
    elif x == 1:
        wp.write(json.dumps(d2))
    else:
        wp.write(json.dumps({'age':24, 'salary':10000}))
    wp.write('\n')
wp.close()



#import json
wp = open(os.path.join('C:\\Users\\SUNEEL PATEL\\Desktop\\py\\D2', 'test_new.json'), 'w+')
for x in range(5):
    if x == 0:
        wp.write(json.dumps(d1))
    elif x == 1:
        wp.write(json.dumps(d2))
    else:
        wp.write(json.dumps({'age':24, 'salary':10000}))
    wp.write('\n')
wp.close()



#import json
rp = open(os.path.join('C:\\Users\\SUNEEL PATEL\\Desktop\\py\\D2', 'test_new.json'), 'r')
# content = json.loads(rp.read())
for line in rp:
    #print(line)
    rec = json.loads(line)
    #print(rec, type(rec))
    print(rec.get('salary', 'Not found'))
    
rp.close()



# d1['key'] and d1[key]
path = os.path.join('C:\\Users\\SUNEEL PATEL\\Desktop\\py\\D2', 'test_new.json')
print(path)


os.path.exists(os.path.join('Misc/old', 'test.json'))


os.path.exists(os.path.join('C:\\Users\\SUNEEL PATEL\\Desktop\\py\\D2', 'test_new.json'))

#==============================================================================

"""
Suneel Patel - Data Scientist for Nation, Society and Humanity

Learn & Teach - Online Training Platform

Email: sunilpatel18@gmail.com   |   M.No: +91-7771007070
Follow on LinkedIn : https://www.linkedin.com/in/suneelpatel/
Twitter: https://twitter.com/sunilpatel18

"""