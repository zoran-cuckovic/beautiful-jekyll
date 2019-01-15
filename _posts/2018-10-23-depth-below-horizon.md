---
id: 372
title: 'Depth below horizon: new (old) functionality for QGIS viewshed analysis'
date: 2018-10-23T11:42:26+00:00
author: Zoran
layout: post
guid: https://landscapearchaeology.org/?p=372
permalink: /2018/depth-below-horizon/
categories:
  - 'Spatial analysis &amp; GIS'
tags:
  - QGIS visibility plugin
---
The basic idea of visibility analysis is to test whether particular locations are theoretically observable from a given observer point (« theoretically » because our data and algorithms can never ideally replicate real-world situations). Such a query yields a yes/no answer for each tested point, which is typically represented as Boolean raster in GIS software.

But, wouldn’t it be great to know, for all those invisible locations, how much we would have to raise the ground to make them visible? Some places may only be a metre or less below the local horizon, which could be considered as possible visibility, given the usual error margin of typical elevation models. When analysing urban plans, this measure could be used to determine the visual impact of proposed constructions: where and to what extent would buildings protrude form horizon line (aka skyline).

![](/wp/wp-content/uploads/2018/10/Line-of-sight.png)

This measure was already implemented in <a href="http://www.zoran-cuckovic.from.hr/QGIS-visibility-analysis/">Viewshed analysis plugin</a> for QGIS 2, and is now available in QGIS 3 (plugin version 0.6.5). It has been renamed to « Depth below horizon » (DBH), the previously used term « Invisibility » being quite clumsy. There are some other novelties as well. In contrast to standard viewsheds, multiple DBH models cannot be combined by simple addition of values. For this reason the new algorithm operates by choosing the deepest or the shallowest value for each analysed point.<a href="#note1">*</a>

<h2>A brief example: Easter Island historical landscape</h2>

As a proof of concept, let’s make a simple DBH model. Our problem is the famous Easter Island and the impact of potential construction on historical landscapes. The tiny island is covered with impressive archaeological vestiges, namely stone sculptures known as Moai (<a href="https://en.wikipedia.org/wiki/Moai">see more on Wikipedia</a>). Urban planners would like to know which areas of the island could be designated for construction without harming the visual experience of the historic landscape. (The following analysis is just for fun: there is much more to urban planning than a simple GIS calculation!)

![](/wp/wp-content/uploads/2018/10/Moai_Rano_raraku.jpg)
*By Aurbina - [Own work, Public Domain.]('https://commons.wikimedia.org/w/index.php?curid=133096)*

I’ve downloaded a very helpful listing of Easter Island Moai (link below); in order to model the visual experience of their visitors we will generate DBH viewsheds from all statue locations. Now, in cases when two or more models overlap, we need to find the one that is the most vulnerable, i.e. the one which will be the most affected by construction. That would be either the one where the target area is visible (DBH = 0), or the one with the lowest DBH value. The obtained value will tell us how high a construction could reach before appearing on <em>at least one</em> visible horizon (from given observer locations). If, however, we would like to know when a construction would appear in <em>every</em> field of vision (from given observer locations), we would filter the highest DBH value.

The image below represents the minimum DBH model for some 500 statue locations and for a maximum radius of 5 km. Not much of the island would be unaffected, considering the tight criteria chosen (views from all registered statue sites, most of which are probably not accessible to public). Several zones appear in the urbanised zone in the south-western part of the island, though. Thanks to DBH values, we can now propose the maximum height for future buildings. (I repeat, this is a mock study!)

Happy mapping!

![](/wp/wp-content/uploads/2018/10/Moai.jpg)
*Blue: DBH greater than 10 metres*

![](/wp/wp-content/uploads/2018/10/Moai-zoom.jpg)
*Blue: DBH greater than 10 metres*

<a name="note1"></a>* Note that the sum of DBH values can be used to calculate average DBH height, by dividing the sum with an inverse of standard viewshed model (where “false” is 1 and “true” is 0). For multiple points, this can be achieved by subtracting cumulative viewshed from a theoretical maximum, obtained by running the analysis over a flat surface model. However, such a figure would rarely be useful.

<h2>Data and literature</h2>

Fisher. P (1996) <a href="https://www.asprs.org/wp-content/uploads/pers/1996journal/nov/1996_nov_1297-1302.pdf">Extending the applicability of viewsheds in landscape planning</a>. Photogrammetric Engineering and Remote Sensing 62 (11).

Torres Hochstetter, Francisco &amp; Lipo, Carl &amp; Hunt, Terry. (2014). <a href="https://www.researchgate.net/publication/260706815_moai-and-roads">moai-and-roads</a>. ResearchGate.net.

Elevation data: <a href="https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm-1-arc">SRTM 1 Arc-Second Global</a>