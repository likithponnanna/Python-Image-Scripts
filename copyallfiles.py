import os
import shutil
dir = os.getcwd()

for root, dirs, files in os.walk(dir):  # replace the . with your starting directory
   for file in files:
      path_file = os.path.join(root,file)
      shutil.copy2(path_file,'C:/Users/lbelliappa/Desktop/AllDocs/')