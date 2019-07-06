---
layout: post
published: true
title: DEM shading algorithm for QGIS
subtitle: 'Kickstarter campaign for a happier QGIS :)'
date: '2019-07-05'
tags:
  - QGIS
---
I've been seeing on the net more and more of beautiful maps made in 3D software, Blender mostly. The reason for venturing into 3D: shadows mostly. While we do have hillshading algorithms in most GIS packages, nothing can beat true ambient light for terrain visualisation. Shadows do not only give a natural feel to an image, they also provide important information on object shapes and depths (see examples below).

![schema.png]({{site.baseurl}}/figures/schema.png)
*The basic idea od natural shading: modelling light paths.*

How come we don't have proper shading algorithms for cartographic purposes? Don't know, but upon seeing all those ten-page tutorials for 3D software, I figured it wouldn't be more difficult to simply build the algorithm for QGIS. (Well, it turned out to be more difficult than I imagined, as usual with coding ...) Anyway, the algorithm is up an running in QGIS ([landscapearchaeology.org/2019/qgis-shadows/](https://landscapearchaeology.org/2019/qgis-shadows/)). But that's more of a proof of concept: I've started a [**Kickstarter campaign**](https://www.kickstarter.com/projects/archaeology/terrain-shading-plugin-for-qgis) to develop a more robust algorithm and to integrate it in QGIS architecture (Processing toolbox). Support it and QGIS will be happy :). 

What is the difference between "hillshading" and "natural shading"? (Neither of the terms is ideal...) **Hillshade algorithms**, as implemented in most GIS, model **light reflectance**, that is, the way light rays should bounce off a smooth surface. **Natural shading**, on the other hand, models **unreflected light path**, namely shadows which are produced in areas inaccessible to light from a particular light source. Therefore, true shading can be produced by **combining the two: hillshade + natural shadows**.     

## Shaded terrain examples

<iframe frameborder="0" class="juxtapose" width="100%" height="620" src="https://cdn.knightlab.com/libs/juxtapose/latest/embed/index.html?uid=455cca0e-9f05-11e9-b9b8-0edaf8f81e27"></iframe>
*Coast of Dalmatia, Croatia.*

<iframe frameborder="0" class="juxtapose" width="100%" height="566" src="https://cdn.knightlab.com/libs/juxtapose/latest/embed/index.html?uid=9c44cc92-9ffd-11e9-b9b8-0edaf8f81e27"></iframe>
*Gergovia stronghold (France): Caesar's army was defeated there (or at least retreated without seizing the Gaulish fortress...). Data: Lidar scan, www.craig.fr. Map: Elise Fovet, MSH Clermont-Ferrand.* 

<iframe frameborder="0" class="juxtapose" width="100%" height="694" src="https://cdn.knightlab.com/libs/juxtapose/latest/embed/index.html?uid=438272fe-a001-11e9-b9b8-0edaf8f81e27"></iframe>
*Gergovia : detail of suface structures (modern period drystone walls and cairns, which may sometimes cover archaeological remains). Data: Lidar scan, www.craig.fr. Map: Elise Fovet, MSH Clermont-Ferrand.* 

## Support the Kickstarter campaign
<iframe src="https://www.kickstarter.com/projects/archaeology/terrain-shading-plugin-for-qgis/widget/card.html?v=2" width="220" height="420" frameborder="0" scrolling="no"></iframe>
