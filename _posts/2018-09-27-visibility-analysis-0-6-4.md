---
layout: post
author: Zoran
categories:
  - Spatial analysis &amp; GIS
date: 'Fri Sep 28 2018 01:00:55 GMT+0200 (heure d’été d’Europe centrale)'
guid: 'https://landscapearchaeology.org/?p=308'
id: 308
permalink: /2018/visibility-analysis-0-6-4/
tags:
  - QGIS visibility plugin
  - qgis
title: 'Visibility analysis for QGIS 3.0 : tackling big data'
published: true
---

[Viewshed plugin for QGIS](http://www.zoran-cuckovic.from.hr/QGIS-visibility-analysis/) is based on Numpy library for handling raster data. Numpy is tuned for high performance and is (relatively) easy to use. However, it relies heavily on available live memory and will break with voluminous datasets. Which is what elevation models usually are...

Version 0.6.4 introduces an addition to the original algorithm which should remove the problem for typical cases. The live memory is not saturated with the entire elevation model any more, but rather with data needed only for a single viewshed range. This means that you can perform a reasonably complex viewshed analysis on an elevation model of any size. However, it will still break with "unreasonable" requests, such as an analysis in 100 kilometre radius on a raster with one metre resolution. Such a query is too heavy by any criteria and, even if calculable, would take quite a long time to perform.   

Maximum allowed memory saturation can be set in processing options as follows:
[![](/wp/wp-content/uploads/2018/09/Capture.png)](/wp/wp-content/uploads/2018/09/Capture.png) 

The "memory buffer size" is expressed in mega-pixels. A raster 1000 by 1000 pixels is thus 1 mega-pixel large, while 10 000 by 10 000 will have 100 mega-pixels. I've set the default to 300 mega pixels, which I estimate as a reasonable amount. Use larger sizes for stronger machines : operations in live memory can be up to 10x faster. 

I've tested the plugin on a large dataset, [elevation model of the Mediterranean littoral](/2018/mediterranean-land-visibility/) (more than 400 mega pixels) and it worked fine.
