---
layout: post
published: false
title: 'WGS84: the sneaky enemy of GIS'
---
## A New Post


GIS software has become highly sophisticated, perhaps event too much. It can recognise and handle such bewildering number of data formats and then combine all these together. Great, we can crank out our results ever more rapidly, but ... which results exactly?

In my experience understanding and geographical projections seems to become more and more shaky among "GIS users". Some three quarters of questions or error reports I get on QGIS Viewshed Analysis Plugin are due to the use of (downloaded) latitude-longitude data. Check on [stackexchange](https://gis.stackexchange.com/questions/166655/error-memory-on-viewshed-analysis-plugin-qgis). Very rarely do I get questions on the algorithm implemented.

Thus I discovered the awful truth: **there is a vast amount of "GIS analysis" being done out there on unprojected data**. Sure many things can be done without projections, but with raster data? And then, how are the results going to be represented?  



