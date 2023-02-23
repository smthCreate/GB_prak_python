import os

with open('file.txt','r',encoding='utf-8') as file:
# file1 = open('C:\\Users\\user\\PycharmProjects\\GB_prak_python\\numbers.txt','r',encoding='utf-8')
    text = file.readlines()
    print(len(text[0].strip()))

# text1 = file1.read()
with open('write_to_file.txt','w',encoding='utf-8') as w_file:
    w_file.writelines(text)

cur_dir = (os.getcwd())
ld = os.listdir(cur_dir)
if os.path.exists('write_to_file.txt'):
    print(True)

# print(text)
# print(text)



file.close()
#file's path
#c:/