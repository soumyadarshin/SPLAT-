from osgeo import gdal

# Convert HGT to GeoTIFF
input_hgt = 'N20E085.hgt'
output_tif = 'N20E085.tif'
gdal.Translate(output_tif, input_hgt, format='GTiff')

# You would need to use FDO or other tools to convert GeoTIFF to SDF
