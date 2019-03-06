---
layout: post
published: true
title: 'Enhancing terrain cartography with natural shadows  '
subtitle: 'Or, how to produce beauty in QGIS without 3D software.'
date: '2019-03-10'
tags:
  - qgis
---

![Algo-window.JPG]({{site.baseurl}}/figures/Algo-window.JPG)
*QGIS algorithm for modelling natural shadows.* 

## Introduction
Modelling natural illumination is quite difficult in software for digital cartography. Yes, we do have hillshading algorithms, but despite the name they do not produce true shade. Hillshade routines colour the terrain according to exposition towards the sun (white for directly exposed and black for unexposed areas),  *but they do not model light path*. There are no shadows in hillshades. As a result, a canyon floor will be rendered the same way as a wide valley, which impedes the perception of depth. Hillshades often have a feeling of "elephant skin", as if the Earth surface were wrinkled by long term cosmetic abuse.

![hillshade-test.jpg]({{site.baseurl}}/figures/hillshade-test.jpg)
*Simple hillshade model ...*

![shade-test.jpg]({{site.baseurl}}/figures/shade-test.jpg)
*... and the same combined with natural shadows.*

Compare these two images: shadows are not just nice, they enable better understanding of the terrain. Today, cartographers typically turn to 3D software, such as Blender, to obtain the effect of natural lighting ([see for example scottreinhardmaps.com](https://www.scottreinhardmaps.com/shop)). Historically the effect was achieved by hand (figure below).

![jungfraugruppe.jpg]({{site.baseurl}}/figures/jungfraugruppe.jpg)

*Jungfrau range (European Alps) by E. Imhof (see on [reliefshading.com]( http://www.reliefshading.com/examples/jungfrau/).*

But, why should we drop all benefits of georeferenced environment and revert to software which can't handle geographical data? It is not that difficult to simulate natural light, provided that we do not expect the same level of quality as in dedicated 3D doftware. 

I have developed a short algorithm to simulate incident light over the terrain, namely the shadows it should produce. Rather than simple yes/no format, *shadows are represented as depth values*. In natural environment, there is a considerable difference between two metres deep shadow, as behind a small mound and hundreds of metres deep shadow, behind a cliff. Taking care of such nuances can help as to get closer to the refined effect of handmade hillshades.

![Puy-de-Dome.jpg]({{site.baseurl}}/figures/Puy-de-Dome.jpg)
*Deep shadow below Puy de Dôme, France ([© baladomes.com](http://www.baladomes.com))*

## Algorithm

For those interested in the code behind my solution, these are the two crucial lines: 

```
shadows = elevations - numpy.maximum.accumulate(elevations)
``` 

The accumulate function takes care that values in a (numpy) array which stores the elevation model would only increase, from the beginning of the array to its end. Imagine that you walk over a mountain, and the path is constantly winding upwards and downwards. If you would like to move only upwards, you would need to fill all valleys with soil or water. The accumulate function does that, it simulates a cascading terrain profile where we can travel either upwards or over a flat terrain. Filled portions of the terrain become shadows if you imagine the sun shining into a flank of a mountain. Shadow depth is calculated by subtracting the cascading model from the actual terrain height.    

```
tilt = distances_x + distances_y * (sun_angle / 90 )  
```

To simulate the vertical angle from which the sun is shining over the terrain, we rather tilt the entire elevation model. That is, we construct a sloping surface and the drape the terrain over it. Distance values in the line above are calculated for each pixel from the corner (or the border) closest to the sun position. Note that we decompose distances on x axis and on y axis components: let's say these are vector components (see the previous post on [vectors and hillshades]( https://landscapearchaeology.org/2018/lidar-hillshade/)). 

The rest of the algorithm is rotating the elevation model in different directions to simulate the entire 360 degree orbit. I’ve also included a smoothing function as the raw result tends to be very pixelated. The function is adapted from the [Topographic position index algorithm]( https://landscapearchaeology.org/2019/tpi/).

You can see the algo in GitHub repository: [QGIS-raster-sahding](https://github.com/zoran-cuckovic/QGIS-raster-shading).

## Using the algorithm and styling the output

The shading algorithm is used as a Processing script for QGIS 3 and is installed as usual (figure below). It will appear under **Scripts >> Raster terrain analysis >> Natural shading** in the Processing toolbox.

![processing-add-script.jpg]({{site.baseurl}}/figures/processing-add-script.jpg)

The input for the algorithm is a digital elevation model and the output is a "shadow map". The result will be smoothed by default (otherwise there is a nasty pixelisation effect). Other parameters should be self-explanatory (sun direction and vertical angle).

The most important issue is **limited handling of large datasets**, because of numpy raster processing library, which is limited by the available live computer memory. Large rasters, if opened, will saturate live memory (raster size at which this effect may be noticed depends on your machine...). (The algorithm is in the "proof of concept" stage, technical problems will be handled in the future.)

The output will provide information on the **depth below the closest sun ray for each pixel in a raster DEM.** These values can be used to produce gradients of shadow tones, as opposed to uniformly dark surfaces. The best effect is made, as for usual hillshade models, when superimposing several layers in transparency mode. 

Natural shadows work best where hillshades tend to produce "elephant skin" effect; the first example is errored and gullied relief in Istria, Croatia. Here, I'm using an elevation model styled with hypsometric colours, overlaid with a hillshade model and a shadow model.  

![Istra-hillshade.jpg]({{site.baseurl}}/figures/Istra-hillshade.jpg)
*Hillshade draped over elevation model.*

![Istra-shadow.jpg]({{site.baseurl}}/figures/Istra-shadow.jpg)
*Natural shadows combined with hillshade and elevation model.*

See how shadows introduce a feeling of depth? Now, simple black/grey shadows would be problematic as they could easily occlude detail in valleys. Or, if too transparent, they would just add some mist, without introducing much perceptual improvement. Hopefully, my algorithm provides information on shadow depth, which enables to fine tune the effect. Shallow shadows should be less strong, as we can suppose a stronger impact of light dispersal in such areas. Here, I've set different intensities of grey and different levels of opacity for five classes between zero and minus 400 metres.  Typically you would also need to completely eliminate shadows less than 2 or 3 metres in depth (opacity = 0%), as they tend to encroach ridgelines and hilltops.

![Style.JPG]({{site.baseurl}}/figures/Style.JPG)
*Shadow intensities are controlled by both colour and transparency for each depth class.*

One last example, Požega valley in Croatian part of Pannonia:

![Pozega-hillshade.jpg]({{site.baseurl}}/figures/Pozega-hillshade.jpg)


And with natural shadows:

![Pozega-shade.jpg]({{site.baseurl}}/figures/Pozega-shade.jpg)


## Download

The script can be [downloaded directly](https://github.com/zoran-cuckovic/QGIS-raster-shading/archive/master.zip) or from [GitHub repository](https://github.com/zoran-cuckovic/QGIS-raster-shading/).

Happy mapping!

