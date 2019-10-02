# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 

import os
path = r'C:\Users\lbelliappa\Desktop\CD'
#path = 'E:\sorted'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, 'LE-1-'+str(index+1)+'.png'))
	
