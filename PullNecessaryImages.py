import os, shutil

InFile = open(r"D:\CC_2019\Export_Output.txt",'r')


lines = InFile.readlines()
ImageList = []




for line in lines:
    if line.split(',')[0] != 'OBJECTID':
        ImageList.append(line.split(',')[2][:-4])


output = r'D:\CC_2019\ImagesWeNeed'
for root, dirs, files in os.walk(r'S:\LV_Valley_Imagery\2019'):
    for filename in files:
        if 'delivery_' in root and filename[:-4] in ImageList:
            print "copying " + root + '\\' + filename
            shutil.copy(root + '\\' + filename, output)
        
