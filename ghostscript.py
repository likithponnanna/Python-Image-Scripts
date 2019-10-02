import os
import subprocess
dir = os.getcwd()

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            i = 1
            r.append(os.path.join(root, name))
            test = os.path.join(root, name)
            #print("Full: " + test)
            if name != "ghostscript.py" and name.endswith('.pdf'):
                #myCmd = 'gm convert -density 300 -quality 100 -channel Gray +adjoin ' +  test +' ' + test.replace('.pdf', '')+'-%02d'+ str(i) +'.png'
                myCmd = 'gm convert -density 300 -quality 100 -channel Gray +adjoin ' +  test +' ' + test.replace('.pdf', '')+'-%02d'+'.png'
                print("File: " + myCmd)
                os.system(myCmd)
                i += 1
    return r
	
	
list = list_files(dir)
#print(str(list))
#test = os.system("ls -l")
#os.system(myCmd)
#myCmd = 'gm convert -density 300 -quality 100 -channel Gray +adjoin 0406_1500219832_LoanApplication-URLA_2.pdf 0406_1500219832_LoanApplication-URLA_2-%02d.png'
#test = os.system(myCmd)
#print(test)