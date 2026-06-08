import ee
import ee.mapclient  # Only needed for interactive map display (e.g., in Colab)

# Initialize Earth Engine
ee.Initialize()

# 1. Define the Region of Interest (Example: A section of the Amazon in Brazil)
# You can define your own polygon using coordinates from Google Maps or other sources.
amazon_roi = ee.Geometry.Polygon(
    [
        [-55.0, -10.0], [-50.0, -10.0], [-50.0, -5.0], [-55.0, -5.0], [-55.0, -10.0]
    ]
)

# 2. Access the Global Forest Change Dataset (v1.9)
gfc_dataset = ee.Image('UMD/hansen/global_forest_change_2023_v1_9')

# Get the forest loss layer (values represent the year of loss: 2001-2023)
loss_year = gfc_dataset.select('lossyear')

# Get the tree cover in the year 2000 (for masking)
treecover2000 = gfc_dataset.select('treecover2000')

# Define a threshold for tree cover (e.g., > 30% canopy cover in 2000 was forest)
forest_threshold = 30
forest2000 = treecover2000.gte(forest_threshold)

# 3. Filter for a Specific Time Period of Loss (e.g., 2015-2020)
start_year = 2015
end_year = 2020

loss_in_period = loss_year.gte(start_year - 2000).And(loss_year.lte(end_year - 2000)).And(forest2000)

# 4. Calculate the Area of Forest Loss
# Calculate the area of each pixel (GFC data is at 30m resolution)
pixel_area = ee.Image.pixelArea()

# Multiply the loss mask by the pixel area to get the area of loss per pixel
loss_area_image = loss_in_period.multiply(pixel_area)

# Calculate the total area of loss within the region of interest
loss_area_stats = loss_area_image.reduceRegion(
    reducer=ee.Reducer.sum(),
    geometry=amazon_roi,
    scale=30,  # Match the resolution of the GFC data
    maxPixels=1e13
)

# Get the total loss area in square meters and convert to hectares (1 ha = 10000 sq m)
total_loss_sqm = loss_area_stats.get('loss')
total_loss_ha = ee.Number(total_loss_sqm).divide(10000)

# Print the result
print(f"Total forest loss in the defined Amazon region between {start_year} and {end_year}:")
print(total_loss_ha.getInfo(), "hectares")

# 5. Visualize the Results (Optional - for interactive environments like Colab)
# Create a visualization of the forest loss
loss_vis = {'palette': ['red']}
# Add the loss layer to the map
# ee.mapclient.centerMap(-53, -7, 6)  # Center the map over the region
# ee.mapclient.addToMap(loss_in_period.updateMask(loss_in_period), loss_vis, 'Forest Loss')
