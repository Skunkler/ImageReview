import os


originalInput = r'S:\LV_Valley_Imagery\2019\final_to_repo'

OrigList = []
for root, dirs, files in os.walk(originalInput):
    for filename in files:
        if filename[-4:] == '.tif':
            UnixRoot = root.replace('\\', '/')
            OrigList.append((UnixRoot + '/' + filename, root.split('\\')[-1], filename))
            

RGBInput = r'S:/LV_Valley_Imagery/2019/final_rgb_repo'
outputList = open(r'D:\CC_2019\writeRGBBLS.bls','w')
outputList.write("Input1\tOutput1\n")
OrigList.sort()
for i in range(len(OrigList)):
    secLine = RGBInput + '/' + OrigList[i][1] + '/' + OrigList[i][2]
    Line = '"{0}"'.format(OrigList[i][0]) + '\t' + '"{0}"'.format(secLine)
    outputList.write(Line + '\n')
    

