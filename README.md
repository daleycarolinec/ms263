# Exploring Benthic Structure in California's Nearshore Marine Protected Areas 
## MS263
### Moss Landing Marine Laboratories | Data Analysis Final Project | Spring 2025

## Summary
This project calculates a suite of derived benthic habitat metrics for locations sampled by the [California Collaborative Fisheries Research Program (CCFRP)](https://www.ccfrp.org/), as well as assesses how these metrics covary and differ within and across CCFRP sampling locations. These data can be paired with CCFRP catch data to understand how the benthic landscape of California's network of marine protected areas (MPAs) relates to longterm monitoring outcomes of nearshore fisheries.  


## Dependencies

Before running the ['Analyzing Differences in Habitat Metrics.ipynb'](http://localhost:8888/lab/tree/Project/ms263-main%202/Analyzing%20Differences%20in%20Habitat%20Metrics.ipynb) notebook, please be sure to install the ['habitat_metric_plotting.py'](http://localhost:8888/lab/tree/Project/ms263-main%202/habitat_metric_plotting.py) Python function file. 

### Basic environment 
* [os](https://docs.python.org/3/library/os.html)
* [numpy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [glob](https://docs.python.org/3/library/glob.html)

### Geospatial packages 
* [xDEM](https://xdem.readthedocs.io/en/stable/index.html)
* [geopandas](https://geopandas.org/en/stable/) 
* [rioxarray](https://corteva.github.io/rioxarray/stable/index.html)
* [xarray](https://docs.xarray.dev/en/stable/)
* [rasterio](https://rasterio.readthedocs.io/en/stable/index.html)
* [shapely](https://shapely.readthedocs.io/en/stable/index.html)


### Statistical analysis & data visualization packages 
* [matplotlib](https://matplotlib.org/)
* [seaborn](https://seaborn.pydata.org/)
* [scipy](https://scipy.org/)
* [pingouin](https://pingouin-stats.org/build/html/index.html)


## Data 

### Shapefiles

The shapefiles utilized in this project are listed below and housed in the [Shapefiles](\Shapefiles) folder:  

 * California Marine Protected Area (MPA) shapefile downloaded from [California Department of Fish and Widlife Open Data Portal](https://map.dfg.ca.gov/metadata/ds0582.html). Shapefile of MPAs sampled by CCFRP (California Collaboratiave Fisheries Research Program) was built by refining comprehensive MPA shapefile from CDFW in QGIS based on table of CCFRP sampling sites housed on [CCFRP website](https://www.ccfrp.org/background). 
 
 * California coastline shapefile downloaded from [California Department of Fish and Wildlife Coastal Boundary Zone database](https://map.dfg.ca.gov/metadata/ds0990.html).
 
 * California Collaborative Fisheries Research Program (CCFRP) grid cell shapefile is maintained internally by the CCFRP team. 

### Ditigal Elevation Models 

Bathymetric digital elevations models were downloaded from the [California Seafloor Mapping Program](https://www.usgs.gov/centers/pcmsc/science/california-seafloor-mapping-program). Bathymetric data does not exist for every CCFRP-sampled MPAs. The extent of some MPAs exeedes a single DEM, and multiple DEMs must be mosaiced in QGIS before introduction into Python. Once DEMs have been processed, they should all be placed into a single folder for incorporation into the ['Calculate Habitat Metrics with xDEM'](http://localhost:8888/lab/tree/Project/ms263-main%202/Calculate%20Habitat%20Metrics%20with%20xDEM.ipynb) and ['Zonal Statistics within CCFRP Gridcells'](http://localhost:8888/lab/tree/Project/ms263-main%202/Zonal%20Statistics%20within%20CCFRP%20Gridcells.ipynb) notebooks. The following list outlines the CCFRP-sampled MPAs with full DEM coverage, as well as the California Seafloor Mapping Program DEM files that correspond to each:

* South Cape Mendocino SMR (['Bathymetry_OffshoreCapeMendocino.tif'](https://cmgds.marine.usgs.gov/data-releases/datarelease/10.5066-P9U0SUGL/))


* Stewarts Point SMR (['Bathymetry_OffshoreFortRoss.tif'](https://pubs.usgs.gov/ds/781/OffshoreFortRoss/data_catalog_OffshoreFortRoss.html), ['Bathymetry_OffshoreSaltPoint.tif'](https://pubs.usgs.gov/ds/781/OffshoreSaltPoint/data_catalog_OffshoreSaltPoint.html))


* Bodega Head SMR (['Bathymetry_OffshoreBodegaHead.tif'](https://pubs.usgs.gov/ds/781/OffshoreBodegaHead/data_catalog_OffshoreBodegaHead.html))


* Año Nuevo SMR (['Bathymetry_OffshorePigeonPoint.tif'](https://cmgds.marine.usgs.gov/data/csmp/OffshorePigeonPoint/data_catalog_OffshorePigeonPoint.html), ['Bathymetry_OffshoreSanGregorio.tif'](https://pubs.usgs.gov/ds/781/OffshoreSanGregorio/data_catalog_OffshoreSanGregorio.html))


* Point Buchon (['Bathymetry_OffshorePointBuchon.tif'](https://cmgds.marine.usgs.gov/data-releases/datarelease/10.5066-P9KBGELE/))


* Point Conception (['Bathymetry_OffshorePointConception.tif'](https://cmgds.marine.usgs.gov/data/csmp/OffshorePointConception/data_catalog_OffshorePointConception.html))



## Steps 

Once you have downloaded the data and imported the packages listed in this README file, run the notebooks within this repository in this order to achieve the analysis outlined in the ['Final Paper'](http://localhost:8888/lab/tree/Project/ms263-main%202/Final%20Paper%20%5BDRAFT%5D.ipynb) notebook:


1. ['Calculate Habitat Metrics with xDEM'](http://localhost:8888/lab/tree/Project/ms263-main%202/Calculate%20Habitat%20Metrics%20with%20xDEM.ipynb)


2. ['Zonal Statistics within CCFRP Gridcells'](http://localhost:8888/lab/tree/Project/ms263-main%202/Zonal%20Statistics%20within%20CCFRP%20Gridcells.ipynb)


3. ['Assessing Covariance of Habitat Metrics'](http://localhost:8888/lab/tree/Project/ms263-main%202/Assessing%20Covariance%20of%20Habitat%20Metrics.ipynb)


4. ['Analyzing Differences in Habitat Metrics'](http://localhost:8888/lab/tree/Project/ms263-main%202/Analyzing%20Differences%20in%20Habitat%20Metrics.ipynb)
    
