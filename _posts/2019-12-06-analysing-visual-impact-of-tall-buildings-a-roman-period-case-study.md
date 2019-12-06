---
layout: post
published: false
title: 'Analysing visual impact of tall buildings: a Roman period case study'
tags:
  - qgis visibility analysis
---
# Introduction
A common problem in visibility analysis is to determine the visual impact of a tall building, for instance a skyscraper or a wind turbine. Now, there is a variety of approaches to measure such impact: how tall does the building stand above the horizon, against which background is it placed, does it cast shadows on certain places, etc. This tutorial will cover the basic measure of the apparent height of tall buildings. My example will be an extraordinary Roman tower, built high and deep in the northern flanks of the Pyrenees.   

<iframe width="560" height="315" src="https://www.youtube.com/embed/WXKPAJQhFOc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The tower of Urkulu was built by the Romans on top of a hill some 1400 metres above the sea level, close to a major Roman road. What can be seen today is only its round base, 19.5 meters in diameter, constructed of massive, well-shaped limestone blocks and filled with rubble and construction debris. Archaeologists and historians believe that the tower had a symbolic function, as a so-called trophy tower ([tropaeum](https://en.wikipedia.org/wiki/Tropaeum_Traiani)) which boasted Roman supremacy over the region. However, the building is ideally placed for visual surveillance and signalling, as we shall see later on; its original function may not be fully clear. In order to understand better the reasons for the construction of this strange, massive tower, let’s do some visibility modelling. 

The problem is following: which height should the tower attain in order to be visually dominant? Or, if it was used for surveillance/signalling, which height would allow for good visual control of the surrounding area? 

Standard visibility analysis produces models for single, fixed observer/target height, so we shall make a series of viewsheds for a range of hypothetical heights, and combine them in a cumulative visibility model. 

I will be using [QGIS Visibility analysis plugin](http://www.zoran-cuckovic.from.hr/QGIS-visibility-analysis/), which can be installed from the official QGIS Plugins repository. My data is SRTM digital elevation model of 1 arc-second precision, which yields 27 meters resolution when projected.  

# Tutorial

First, the analysed building has to be represented as a series of observer/target points. Since QGIS Visibility plugin operates on a pixel-to-pixel basis, these points do not have to overlap perfectly. The only requirement is that they be contained within the same pixel of the elevation model used for the analysis. Here, I will draw a polygon within a pixel coverage and create 5 random points inside it. 

![2019-12-1.jpg]({{site.baseurl}}/figures/2019-12-1.jpg)
*Polygon (green) within the observer’s pixel of the elevation model (greyscale).*

![2019-12-2.jpg]({{site.baseurl}}/figures/2019-12-2.jpg)
*Random points within the polygon.* 

**NB** If you play with different elevation models, it is advisable to be as precise as possible and to duplicate points instead of generating random points. 

Next, we create viewpoints from these multiple locations. The analysis radius is set to 30 kilometres. 

![2019-12-4.jpg]({{site.baseurl}}/figures/2019-12-4.jpg)

Each observer point will be assigned a specific height. Here, I’m using increments of 5 for a range of 0 to 20 metres. 

![2019-12-5.jpg]({{site.baseurl}}/figures/2019-12-5.jpg)

*NB For the lazy ones, or those that have dozens of observation points, the observer heights can be entered through QGIS field calculator with expression `(@row_number – 1) * 5`, where 5 is the increment used here.  

We can now perform the viewshed calculation. Note that the algorithm will always combine outputs when multiple points are present. I’m using the Earth curvature correction as it may have some impact over longer distances. 

![2019-12-6.jpg]({{site.baseurl}}/figures/2019-12-6.jpg)

Let’s finish by styling the output. I will set the invisible areas to transparency, in order to drape the model over the terrain.

![2019-12-7.jpg]({{site.baseurl}}/figures/2019-12-7.jpg)

We can think of our result as a series of nested boxes: the largest area is visible from the top level and the smallest one from the ground level. For a common 2.5D elevation model, it is not possible that a patch seen from a lower level would not be visible from the top level (this is not valid for true 3D models…). These viewshed overlaps are registered in the algorithm output (0 = not visible, 1 overlap = visible from the top level exclusively, 5 overlaps = visible from all floors down to the ground level).

![2019-12-8.jpg]({{site.baseurl}}/figures/2019-12-8.jpg)

# Discussion

And here is our visibility model: 

[![2019-12-viewshed.jpg]({{site.baseurl}}/figures/2019-12-viewshed.jpg)][{{site.baseurl}}/figures/2019-12-viewshed.jpg]

Our viewshed model is quite interesting. First of all, it is very fragmented for a building destined to impress travellers from afar. The building would often go out of sight and then reappear in front of a passenger. Surely, there are better locations from which the impressive tower would be an unavoidable sight. 
Note the pale tones to the north of the tower: these are the areas where only the top portion of the building would be visible. Most of these locations are more than 10 kilometres away, so the level of “impressiveness” of the building would be quite low. Indeed, the building is placed some 5 metres or so below the actual hilltop, which is effectively hiding the building from the north.   

![2019-12-Urkulu map]({{site.baseurl}}/figures/2019-12-Urkulu-topo.jpg)
*The Urkulu tower is represented by the orange circle.

We can, then, conclude that the Roman trophy tower was constructed to be visible at relatively close distance, perhaps from the road that passed nearby. 

We can, however, also imagine a practical purpose of the building. If the height of the tower compensated for some 5 metres difference from the mountaintop, it could have been used for surveillance of the passage across the mountain. In principle, our analysis can be used to estimate which areas would be visible from each height level, but we should bear in mind that the SRTM terrain model is imprecise and not suitable for a precision calculation.  

This short example should introduce some basic concepts of the analysis of visual impact. The same principles can be used to analyse skyscrapers, wind turbines, or other types of tall buildings. Note, however, that precise elevation model is primordial for such an analysis, I repeat that the STRM model used here should only serve as “proof of concept”.
