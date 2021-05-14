import os
import re

class fileList():
    def __init__(self, initial_route) -> None:
        self.initial_route = initial_route
    
    def createGenesisBlocks(self): 
        '''This function will get the initial files and create genesis blocks for them on the blockchain'''

        ignore_list = ["node_modules", "site-packages"]

        fd = open("text_location.txt",'w')
        #path ="/home/okohedeki/Desktop"
        
        #we shall store all the file names in this list
        filelist = []

        for root, dirs, files in os.walk(self.initial_route):
            for file in files:
                #append the file name to the list
                filelist.append(os.path.join(root,file))

        #print all the file names

        for ignore in ignore_list:
            for name in filelist:

                if not re.search(('.*{}.*').format(ignore), name):

                    fd.write(str(name) + "\n")
                    print(name)

        fd.close()