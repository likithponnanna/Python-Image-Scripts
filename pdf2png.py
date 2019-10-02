import os

rootdir = r'C:\Users\lbelliappa\Desktop\NewDocs'
os.chdir(rootdir)
List = os.listdir(rootdir)
for i in range(len(List)):
    os.mkdir(List[i].split('.')[0])
    temp = os.path.join(rootdir, List[i].split('.')[0])
    print(temp)
    # output = os.path.join(temp, List[i])
    # print(os.path.join(rootdir, List[i]))
    
    os.system('gm convert -density 300 -quality 100 -channel gray %s +adjoin %s' %(os.path.join(rootdir, List[i]), temp + '\%03d.png'))
    print(os.path.join(rootdir, List[i]))