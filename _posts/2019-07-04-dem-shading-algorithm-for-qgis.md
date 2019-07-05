---
layout: post
published: false
title: DEM shading algorithm for QGIS
subtitle: 'Or, ditch that Blender manual for cartography :)'
date: '2019-07-04'
tags:
  - QGIS
---
I've been seeing on the net more and more beautiful maps being made in 3D software, Blender mostly. The reason: shadows mostly. While we do have hillshading algorithms in most GIS packages, nothing can beat true ambiental light for terrain visualisation. Shadows do not only give a natural feel to an image, they also provide important information on object shapes and depths (see below).

![schema.png]({{site.baseurl}}/figures/schema.png)
*The basic idea od natural shading: modelling light paths.  

How come we don't have proper shading algoritms for cartographic purposes? Don't know, but upon seeing all those ten-page tutorials for 3D software, I figured it wouldn't be more diffuclt to simply build the algorithm for QGIS. (Well, it turned out to be more difficult than I imagined, as usual with coding ...) Anyway, the algorithm works, check the previous post ([landscapearchaeology.org/2019/qgis-shadows/](https://landscapearchaeology.org/2019/qgis-shadows/)). But that's more of a proof of concept: I've started a [**Kickstarter campaign**](https://www.kickstarter.com/projects/archaeology/terrain-shading-plugin-for-qgis) to integrate the thing in QGS. Support it and QGIS will be happy :). 

What is the difference between "hillshading" and "natural shading"? (Neither of the terms is ideal...) **Hillshade algoritms**, as implemented in most GIS, model **light reflectance**, that is, the way light rays should bounce off a smooth surface. **Natural shading**, on the other hand, models **unreflected light path**, namely shadow which are produced in areas inaccessible to light from a particular light source. Therefore, true shading can be produced by **combining the two: hillshade + natural shadows**.     

## Shaded terrain examples


![shadows_dalmatia.jpg]({{site.baseurl}}/figures/shadows_dalmatia.jpg)

