import ee

# Initialize Earth Engine
ee.Initialize()

# 1. Define a smaller Region of Interest (ROI)
small_roi = ee.Geometry.Polygon(
    [
        [5.5, 51.5], [6.0, 51.5], [6.0, 52.0], [5.5, 52.0]
    ]
)

# 2. Load the AHN2 0.5m Non-Interpolated DEM dataset (available for 2012)
dataset = ee.Image('AHN/AHN2_05M_NON')

# 3. Select the elevation band
elevation = dataset.select('elevation')

# 4. Resample the image to a coarser resolution (e.g., 5m)
elevation_resampled = elevation.resample('bicubic').reproject(
    crs=elevation.projection(),
    scale=5  # Set a coarser scale to reduce pixel count
)

# 5. Clip the resampled elevation dataset to the smaller region
elevation_roi = elevation_resampled.clip(small_roi)

# 6. Calculate statistics for the smaller region
elevation_stats = elevation_roi.reduceRegion(
    reducer=ee.Reducer.minMax().combine(ee.Reducer.mean(), sharedInputs=True),
    geometry=small_roi,
    scale=5,  # Coarse resolution
    maxPixels=1e8  # Adjust for fewer pixels
)

# 7. Print the elevation statistics for the region
print("Elevation statistics for the region:")
print(f"Minimum Elevation: {elevation_stats.get('elevation_min').getInfo()} meters")
print(f"Maximum Elevation: {elevation_stats.get('elevation_max').getInfo()} meters")
print(f"Mean Elevation: {elevation_stats.get('elevation_mean').getInfo()} meters")
