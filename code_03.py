'''file = open('swati.txt', 'r')
content = file.read()
print(content)


file = open('swati.txt', 'r')
#content = file.read()
line = file.readline()
print(line)


file = open('swati.txt', 'r')
#content = file.read()
lines = file.readlines()
print(lines)


'''


'''
file = open('swati.txt', 'r')
file = open('swati.txt', 'w')
file.write('Hello, Swati\n')
content = file.read()
print(content)

file = open('swati.txt', 'r')
# file = open('swati.txt', 'w')
#file.write('Hello, Swati\n')
content = file.read()
print(content) 
'''

'''

file = open('swati.txt', 'a')
file.write('\nHello, tush\n')

file = open('swati.txt', 'r')
#file = open('swati.txt', 'a')
#file.write('\nHello, tush\n')
content = file.read()
print(content) 




file.close()
'''



import os
import os.path
import shutil

# os.mkdir('my_folder')
#a=os.listdir('.')
#print(a)

'''
x= os.path.exists('swati.txt')
print("swati.txt exists:", x)
'''
'''
x= os.path.exists('Python_DevOps')
print("Python_DevOps exists:", x)
'''

#os.rmdir('my_folder')


'''
shutil.rmtree('Python_DevOps')
a= os.listdir('.')
print(a)
'''