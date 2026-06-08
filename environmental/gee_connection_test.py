import ee

# Initialize the Earth Engine API
ee.Initialize()

# Check if the Earth Engine API is connected
try:
    # Try a simple operation like getting information about a dataset
    dataset = ee.Image('UMD/hansen/global_forest_change_2020_v1_8')
    print("Connection successful! Dataset info:", dataset.getInfo())
except Exception as e:
    print("Error connecting to Earth Engine:", e)
