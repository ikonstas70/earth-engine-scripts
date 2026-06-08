import ee

# Initialize Earth Engine
try:
    ee.Initialize()
except Exception as e:
    ee.Authenticate()
    ee.Initialize()

# Define the dataset and region
modis = ee.ImageCollection('MODIS/061/MOD11A1')

# Define the region (coordinates as an example)
region = ee.Geometry.Rectangle([-120.0, 35.0, -119.0, 36.0])

# Filter the dataset for a time period and region
image = modis.filterDate('2024-01-01', '2024-01-31').filterBounds(region).mean()

# Reduce the region to get mean temperature data
result = image.reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=region,
    scale=1000,
    maxPixels=1e13
)

result_info = result.getInfo()

# Check and safely handle 'LST_Day_1km' value
lst_value = result_info.get('LST_Day_1km', None)

if lst_value is not None:
    kelvin_value = lst_value * 0.02
    celsius_value = kelvin_value - 273.15
    print(f"Average Land Surface Temperature (Celsius): {celsius_value:.2f}°C")
else:
    print("LST_Day_1km key is not available or has no value.")
