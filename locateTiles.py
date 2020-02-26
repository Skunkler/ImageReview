import arcpy, os




def checkTileExists(TileName):
    count = 0
    for root, dirs, files in os.walk(r'S:\LV_Valley_Imagery\2019\final_to_repo'):
        for filename in files:
            if filename == TileName:
                print "match between " + filename + " and " + TileName
                count += 1
                break
    return count
    






tileShp = r'P:\Geospatial\X0370\Clark-County-Imagery-RFP-admin\RFP652-15-2019\data\Tiles_data.gdb\CC_Aerial_Tiles_2019'
MissingList = []



with arcpy.da.SearchCursor(tileShp, 'NAME_TIF') as cursor:
    for row in cursor:
        print row[0]
        BoolVal = checkTileExists(row[0])
        if BoolVal == 0:
            MissingList.append(row[0])

print MissingList
            
