---
layout: page
published: true
title: 'Free lidar data [work in progress]'
permalink: /lidar-data/
---



# United Kingdom
An overwiew of current lidar coverage can be found on [lidarfinder.com](https://www.lidarfinder.com/).

## England 
[data.gov.uk/dataset - time stamped tiles](https://data.gov.uk/dataset/8275e71e-1516-42a1-bb0c-4fa73807fe2b/lidar-dtm-time-stamped-tiles): various lidar surveys beggining in 1998
[data.gov.uk/dataset - composite](https://data.gov.uk/dataset/80c522cc-e0bf-4466-8409-57a04c456197/lidar-composite-dsm-1m): Point cloud, DEM/DSM 1m, DEM/DSM 2m

## Scotland
[remotesensingdata.gov.scot](https://remotesensingdata.gov.scot/collections): Point cloud, DSM/DTM 1m, DSM/DTM 2m. See also https://rapidlasso.com/2017/10/03/scotlands-lidar-goes-open-data-too/
## Wales
[lle.gov.wales](http://lle.gov.wales/catalogue/item/lidarcompositedataset/): DEM/DSM 1m, DEM/DSM 2m

# France

[https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html#rge-alti-1m](https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html#rge-alti-1m) DEM 1m, DEM 5m. (Quality is very variable, LiDAR was used for flood risk areas, coast and forrest areas : https://geoservices.ign.fr/ressources_documentaires/Espace_documentaire/MODELES_3D/RGE_ALTI/IGNF_RGEALTIr_2-0.html)

## Auvergne - Rhône - Alpes region
[opendata.auvergnerhonealpes.eu](http://opendata.auvergnerhonealpes.eu/dataset/7-les-donnees.htm?from=0&q=lidar): patchy, small scale lidar surveys of various resolutions.
## Coast
[diffusion.shom.fr](https://diffusion.shom.fr/pro/catalogsearch/result/?q=+lidar): patchy coverage of the coastal strip (Atlantic, Mediterranean)

# Slovenia
[gis.arso.gov.si](http://gis.arso.gov.si/evode/profile.aspx?id=atlas_voda_Lidar@Arso&culture=en-US): point cloud, DTM 1m
NB: the point cloud data format is a mess. There is some missing data at the end of each file : check at [arheologija.neocities.org](https://arheologija.neocities.org/Lidar_tutorial.html ) or [https://paleoseismicity.org](https://paleoseismicity.org/tutorial-how-to-make-a-dem-from-the-slovenian-lidar-data/) for tutorials. 
 
# Italy
[www.pcn.minambiente.it](http://www.pcn.minambiente.it/mattm/procedura-richiesta-dati-lidar-e-interferometrici-ps/): DTM 1 or 2 meters
**NB** A formal request and 2 euros fee are required.

## Trentino-Alto Adige
[territorio.provincia.tn.it](http://www.territorio.provincia.tn.it/portal/server.pt/community/lidar/847/lidar/23954): DSM/STM 1m, 2m, point cloud (upon request).

## Sardegna
[http://www.sardegnageoportale.it/areetematiche/modellidigitalidielevazione/](http://www.sardegnageoportale.it/areetematiche/modellidigitalidielevazione/)

# Belgium
Flanders: [https://overheid.vlaanderen.be/DHM-DHMV-II-brondata](https://overheid.vlaanderen.be/DHM-DHMV-II-brondata)

Wallonie: [http://geoportail.wallonie.be/catalogue/cd7578ef-c726-46cb-a29e-a90b3d4cd368.html](http://geoportail.wallonie.be/catalogue/cd7578ef-c726-46cb-a29e-a90b3d4cd368.html)

# Netherlands  
AHN1 lidar [http://geodata.nationaalgeoregister.nl/ahn1/atom/ahn1_gefilterd.xml](http://geodata.nationaalgeoregister.nl/ahn1/atom/ahn1_gefilterd.xml): point cloud (4-5 pts/m²)

AHN2 lidar: [http://geodata.nationaalgeoregister.nl/ahn2/atom/ahn2_uitgefilterd.xml](http://geodata.nationaalgeoregister.nl/ahn2/atom/ahn2_uitgefilterd.xml) : point cloud (9 pts/m²)

NB 1. These links point to .xml files, you will need to convert these to something browser-readable ([www.google.com/search?q=convert+xml+to+html](www.google.com/search?q=convert+xml+to+html))

NB 2. Non-filtered versions of the data are also available: replace `gefilterd` with `uitgefilterd` in the page adress. 
# Spain 
[centrodedescargas.cnig.es](http://centrodedescargas.cnig.es/CentroDescargas/) : Point cloud, DEM 2m, DEM 5m. 

# Denmark
[https://download.kortforsyningen.dk/content/dhmterr%C3%A6n-04-m-grid](https://download.kortforsyningen.dk/content/dhmterr%C3%A6n-04-m-grid) : DEM 0.4m 

[https://download.kortforsyningen.dk/content/dhmpunktsky](https://download.kortforsyningen.dk/content/dhmpunktsky) : Point cloud 

# Germany
[https://data.geobasis-bb.de/geobasis/daten/dgm/](https://data.geobasis-bb.de/geobasis/daten/dgm/)

# Estonia
[https://geoportaal.maaamet.ee/eng/Spatial-Data/Elevation-data-p308.html](https://geoportaal.maaamet.ee/eng/Spatial-Data/Elevation-data-p308.html)

# Finland: 
[https://tiedostopalvelu.maanmittauslaitos.fi/tp/kartta?lang=en](https://tiedostopalvelu.maanmittauslaitos.fi/tp/kartta?lang=en) : DEM 2m, DEM 10m, point cloud (5 pts/m²)


# Ireland: 
[https://data.gov.ie/dataset/open-topographic-lidar-data](http://www.maanmittauslaitos.fi/en/professionals/digital-products/datasets-free-charge/acquisition-nls-open-data)

# Latvia
[https://www.lgia.gov.lv/lv/Digit%C4%81lais%20virsmas%20modelis](https://www.lgia.gov.lv/lv/Digit%C4%81lais%20virsmas%20modelis) : point cloud (1.5 - 4 pts/m²)

List of files for direct download : [https://s3.storage.pub.lvdc.gov.lv/lgia-opendata/las/LGIA_OpenData_las_saites.txt](https://s3.storage.pub.lvdc.gov.lv/lgia-opendata/las/LGIA_OpenData_las_saites.txt)

## Portugal: 
coastal strip: [http://mapas.igeo.pt/lidar/](http://mapas.igeo.pt/lidar/):  (view only)

<!--
Poland see https://mobile.twitter.com/gunthera_mws/status/1106312408149172225

Iceland : http://atlas.lmi.is/mapview/?application=DEM

Lidar for qgis https://plugins.bruy.me/processing-fusion.html

Austria +DEM FREE https://data.opendataportal.at/dataset/dtm-austria

++ ArcticDEM  : 2 meters for canada
Sao Paolo http://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx
-->

To be continued ...
