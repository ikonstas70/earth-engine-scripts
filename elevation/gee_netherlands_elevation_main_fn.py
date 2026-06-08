import ee

# Initialize Earth Engine
ee.Initialize()

# Define the region of interest (for example, a portion of the Netherlands)
roi = ee.Geometry.Polygon(
    [[
        [5.5, 51.5], [6.0, 51.5], [6.0, 52.0], [5.5, 52.0], [5.5, 51.5]
    ]]
)

# Load the AHN2 0.5m Non-Interpolated DEM dataset
dataset = ee.Image('AHN/AHN2_05M_NON')
elevation = dataset.select('elevation')

def get_elevation_statistics():
    # Calculate elevation statistics for the region with maxPixels and bestEffort settings
    elevation_stats = elevation.reduceRegion(
        reducer=ee.Reducer.minMax().combine(ee.Reducer.mean(), sharedInputs=True),
        geometry=roi,
        scale=0.5,  # 0.5m resolution
        maxPixels=1e9,  # Increase the pixel limit if necessary
        bestEffort=True  # Allow Earth Engine to aggregate at the best resolution
    )

    # Extract statistics and print them with explanations
    min_elevation = elevation_stats.get('elevation_min').getInfo()
    max_elevation = elevation_stats.get('elevation_max').getInfo()
    mean_elevation = elevation_stats.get('elevation_mean').getInfo()

    # Output the statistics with explanations
    print("\n### Elevation Statistics for the Selected Region ###")
    print(f"Minimum Elevation: {min_elevation} meters")
    print(f"Maximum Elevation: {max_elevation} meters")
    print(f"Mean Elevation: {mean_elevation} meters")

    # Description of the elevation data and its relevance
    print("\n### Explanation of the Elevation Data ###")
    print("The data represents the **elevation** of the land in the selected region, measured in meters.")
    print("Here’s a quick breakdown of the statistics:")
    print(f"- **Minimum Elevation**: The lowest point in the area, at {min_elevation} meters. This could indicate areas prone to flooding or valleys.")
    print(f"- **Maximum Elevation**: The highest point in the area, at {max_elevation} meters. This might point to mountainous terrain or elevated regions.")
    print(f"- **Mean Elevation**: The average elevation of the entire region, at {mean_elevation} meters. This value helps understand the general topography of the land.")
    print("\nThis data can be useful for a variety of applications, including environmental monitoring, urban planning, and agriculture.")

def explore_datasets():
    # Ask the user if they want to explore other Earth Engine datasets
    print("\nWould you like to explore other Earth Engine datasets?")
    print("You can browse through the official Earth Engine Data Catalog here:")
    print("https://developers.google.com/earth-engine/datasets/catalog")
    
    response = input("Enter 'yes' to explore or 'no' to continue with the current dataset: ").strip().lower()
    if response == 'yes':
        print("\nGreat! You can search for datasets of interest in the Earth Engine Data Catalog.")
        print("Feel free to copy the dataset ID you wish to use and replace it in the script.")
    elif response == 'no':
        print("\nNo problem! Let's continue with the current dataset.")
    else:
        print("\nInvalid input. Please enter 'yes' or 'no'.")

# Main loop
def main():
    print("\n### Elevation Statistics for the Selected Region ###")
    get_elevation_statistics()
    explore_datasets()

if __name__ == "__main__":
    main()
