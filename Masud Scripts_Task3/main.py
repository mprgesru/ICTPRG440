import geopandas as gpd


""" 
Programme Objective: This programme defines and checks a GeoDataFrame, verifies the original CRS,
and converts the coordinate reference system (CRS) from WGS84 to GDA2020 Zone 56. 
It also extracts each country and exports the results as GeoJSON files.

Programme created by: Md Masud Parves Rana
"""


FILE_PATH = r"C:\440_Assessment\WorldCities\LocationCities.shp" # This is the file path of the shapefile of world cities.
OUTPUT_PATH = r"C:\440_Assessment\WorldCities\Output"

# 1. Loading data from the source shapefile into geodataframe

gdf =gpd.read_file(FILE_PATH)

if isinstance(FILE_PATH,str):     # This helps to check File_path is a string or not string
       print("It is a string")
else:
    raise ValueError("Not a string")


# 2. Checking the Geodataframe (Attribute Table) and Geometry

print(gdf.head())

# 3. Checking all the columns in the attribute table

print (gdf.columns)

# 4. Checking the Original CRS of the source shape file

print("Original CRS:", gdf.to_crs)

# 5. Reprojection

def transfrom_WGS84_To_GDA2020(File_Path,ESPG=7856): # this parameter define the transformation from WGS84 to GDA2020

    """
    This function transform coordinates from WGS84 to Another
    """
    
    try:
       gdf = gpd.read_file(File_Path)
       gdf = gdf.to_crs(epsg=ESPG)
    except Exception as e:    # Try and Except helps to identify errors/causes of crashing

     print("This is wrong", e)

    return gdf # return a geodataframe object

transformedgdf =transfrom_WGS84_To_GDA2020(FILE_PATH) # transformed to GDA2020 Z56

print("Transformed CRS:", transformedgdf.to_crs)

#print(transformedgdf.head())

# 6. Showing the list of all countries from the original shapefile

print(transformedgdf["Country"].unique())

# 7. Extracting Countrywise Cities

def Extract_Cities_by_Country(data, Country="Country"):
    Country_gdf=transformedgdf[transformedgdf["Country"]==Country]   # this is for filtering out
    outputfile=OUTPUT_PATH+"\\"+f"{Country}.geojson"                 # exporting file name in output
    Country_gdf.to_file(outputfile)                                  # saving as GeojSON to output after filtering


""" 
   - This function takes gdf and returns a gdf with only data from the specific Country
   - It takes Output folder as a string parameter
   - This function export the file as output.geojson
"""

# 8. For Australia

Extract_Cities_by_Country(data=gdf,Country="Australia")

# 9. For Bangladesh

Extract_Cities_by_Country(data=gdf,Country="Bangladesh")

