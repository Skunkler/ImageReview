#This script was written by Warren Kunkler in support of the 2019 Clark County Image QA Project
#This takes 2 inputs. 1: A directory of images to be scanned and 2: An output for a txt file
#The output txt file contains a list of images where at least 3 of the 4 bands have a minimum pixel value of 0

import arcpy, os
from arcpy import env


input1 = raw_input("enter workspace directory to walk through: ")

ListFile = raw_input("Please enter location to output list of bad tiles to txt: ")

problemFiles = list()



#determin minimum value for each band in raster
def get_min_val(rasterFile):
    count = 0

    for i in range(1, 5):
        rasterBand = rasterFile + '\\' + 'Layer_' + str(i)
        if int(arcpy.GetRasterProperties_management(rasterBand, 'MINIMUM').getOutput(0)) == 0:
            count += 1
    return (count, rasterFile)
    


#write problem tile directory and problem tiles to a text file
def write_list_zeros(outfileLoc):
    outfile = open(outfileLoc,'w')
    
    for i in range(0, len(problemFiles)):
        outfile.write(problemFiles[i][0] + ',' + problemFiles[i][1] + '\n')
    outfile.close()
    

#call get_min_val of each raster tile, if a raster has a 3 or more bands with a minimum value of 0, output that to the problem list
for root, dirs, files in os.walk(input1):
    for filename in files:
        if 'sample' not in root and 'corrected' not in root:
            if filename[-4:] == '.tif':
                print root + '\\' + filename
                evaluateMins = get_min_val(os.path.join(root,filename))
                if evaluateMins[0] >= 2:
                    directory = '\\'.join(evaluateMins[1].split('\\')[:-1])
                    problemFiles.append((directory, evaluateMins[1].split('\\')[-1]))
problemFiles.sort()
write_list_zeros(ListFile)






            
            

