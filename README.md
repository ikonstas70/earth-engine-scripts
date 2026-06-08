# Google Earth Engine Scripts

**Author:** Ioannis Konstas — IT Solutions USA

Python scripts for geospatial and environmental analysis using the Google Earth Engine (GEE) Python API. Organized into two groups: Netherlands elevation analysis using the AHN2 high-resolution DEM, and broader environmental and forest change analysis.

**Requirements:**
```bash
pip install earthengine-api
earthengine authenticate
```

---

## `elevation/` — Netherlands Elevation Analysis

A series of scripts querying the **AHN2 0.5m Non-Interpolated DEM** (`AHN/AHN2_05M_NON`) for a region in the Netherlands (lat 51.5–52.0°N, lon 5.5–6.0°E). Scripts progress from a single-run query to a structured, reusable function architecture.

| Script | Description |
|---|---|
| `gee_netherlands_elevation_single_run.py` | Computes min, max, and mean elevation for the Netherlands ROI — single run, no interaction |
| `gee_netherlands_elevation_basic.py` | Same AHN2 query wrapped in a reusable `get_elevation_statistics()` function with explanatory output |
| `gee_netherlands_elevation_interactive.py` | Adds an interactive loop prompting the user to explore other GEE datasets after each query |
| `gee_netherlands_elevation_interactive_v2.py` | Variant of the interactive version with minor output formatting differences |
| `gee_netherlands_elevation_main_fn.py` | Cleanest structure — separate `get_elevation_statistics()` and `explore_datasets()` functions with a `main()` entry point |
| `gee_netherlands_elevation_with_roi.py` | Prints the full GeoJSON ROI geometry alongside elevation stats for geometry verification |
| `gee_netherlands_elevation_resampled.py` | Resamples AHN2 DEM from 0.5m to 5m via bicubic interpolation before computing stats — significantly reduces API quota usage |

---

## `environmental/` — Global Environmental Analysis

Scripts for global forest change and land surface temperature analysis using NASA and Hansen datasets.

| Script | Description |
|---|---|
| `gee_connection_test.py` | Authenticates with Earth Engine and loads the Hansen GFC 2020 dataset — confirms API access is working before running heavier scripts |
| `gee_modis_land_surface_temperature.py` | Queries MODIS MOD11A1 for a California region — computes mean daytime land surface temperature in Celsius for January 2024 |
| `gee_amazon_deforestation_analysis.py` | Calculates total forest loss in hectares for an Amazon ROI between 2015 and 2020 using the Hansen Global Forest Change 2023 v1.9 dataset |

| Dataset | ID | Resolution |
|---|---|---|
| AHN2 Non-Interpolated DEM | `AHN/AHN2_05M_NON` | 0.5m |
| MODIS LST Day | `MODIS/061/MOD11A1` | 1km |
| Hansen GFC 2023 | `UMD/hansen/global_forest_change_2023_v1_9` | 30m |

---

*© Ioannis Konstas — IT Solutions USA*
