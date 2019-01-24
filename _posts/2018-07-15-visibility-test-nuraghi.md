---
author: Zoran
categories:
- Spatial analysis &amp; GIS
date: 2018-07-15 15:11:08
guid: http://landscapearchaeology.org/?p=86
id: 86
image: /wp/wp-content/uploads/2018/07/Sardegna-nuraghi-teaser-740x348.jpg
layout: post
permalink: /2018/visibility-test-nuraghi/
tags:
- QGIS visibility plugin
- qgis
title: 'Benchmarking viewshed algorithm: Nuraghi of Sardinia'
---

The new [viewshed plugin for QGIS 3](https://landscapearchaeology.org/2018/visibility-analysis-0-6/) features an improved algorithm which should result in perceptible improvements in terms of efficiency. So let's give it a try!

{% include image.html path="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Torralba_San_Antine_10.JPG/640px-Torralba_San_Antine_10.JPG"
caption = "Nuraghe in Toralba-Sant'Antine © Michel Royon / Wikimedia Commons" %}

The test data I'm using are the famous nuraghi of Sardinia, drystone towers dating to the 2. millennium BC. These structures, sometimes combining in small settlements, are extremely numerous on the island. There are some 7000 documented sites, which means much more were originally present. Such quantities of archaeological sites are exceptional for European Bronze Age.

A list of Sardinan nuraghi is available on [nurnet.crs4.it/nurnetgeo](http://nurnet.crs4.it/nurnetgeo), which is great! (Thanks archaeologists!). It is not a scientific database, however, I'm using it for fun.
Elevation model used is the EU-DEM with 25 meters resolution.

**Result**: for cumulative viewshed from 6013 nuraghi, in 5 km radius and observation point 10 metres high, I needed some **two and a half minutes**. My computer has 8 gigabyte RAM and Intel Core i5-3437U @ 1.90GHz. I'm quite happy with this result :)

{% include image.html path= "http://landscapearchaeology.org/wp/wp-content/uploads/2018/07/Sardegna-nuraghi.jpg"
caption="Intensity of visual exposition of Sardinia's nuraghi" %}

## Further information
[Google on Nuraghi](https://google.com/search?q=nuraghi)

[Nuraghi initiative (and database)](http://www.nurnet.it)

[EU-DEM (elevation model)](https://www.eea.europa.eu/data-and-maps/data/copernicus-land-monitoring-service-eu-dem)