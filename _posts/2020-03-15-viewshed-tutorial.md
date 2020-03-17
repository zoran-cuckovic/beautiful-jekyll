---
layout: post
published: true
title: 'Viewshed analysis in QGIS 3: a tutorial'
---

Viewshed analysis denotes field of vision modelling in GIS jargon. The term is quite awkwardly borrowing its suffix from watershed, even if there is nothing being “shed”. Anyway, the term viewshed has become commonplace in GIS terminology and is here to stay. 

![2018-03-15-viewshed.jpg]({{site.baseurl}}/figures/2020-03-15-viewshed.jpg)
*Viewshed output: visible area in white and hidden space in black. Observer location is marked by the red diamond.* 

A basic viewshed analysis output is a visibility map, in raster format, which classifies the terrain surrounding an observation point into visible and not visible (true/false or 1/0). Other, more complex visibility indices may be available in common GIS software, such as the depth below visible horizon or view angle. For the purpose of this tutorial, we will take into account only the basic true/false output. We will use [QGIS Visibility analysis plugin]( http://www.zoran-cuckovic.from.hr/QGIS-visibility-analysis/), available in the official QGIS plugin repository. 

Our dataset consists of ancient Greek towers of the island of Siphnos. For some reason, the ancient inhabitants of the small island constructed a large number of circular and rectangular towers in the period between the 6th and 3rd century BC (approximately). Some 70 tower locations are known today, but none of these structures has survived in its original height; at maximum a couple of metres can still be seen. Considering the terrain model, I’m using the fresh NASA DEM which should be good enough for the purpose of this tutorial (data sources are listed below). 

![2020-03-15-views.png]({{site.baseurl}}/figures/2020-03-15-tower.jpg)
*Cheimarros Tower, island of Naxos ([kastra.eu](https://www.kastra.eu/castleen.php?kastro=xeimaros)).*

Ancient Greek towers probably had a strategic function (even if all historians/archaeologists may not agree about that); one would invest in such a structure in order to keep things safe and, additionally, to keep an eye over the surrounding land. Using viewshed analysis we can evaluate the visual coverage from these structures: which areas were most keenly observed by tower dwellers? 

Our question can be answered by creating a so-called cumulative visiblity map, which is simply a stack of viewsheds from all observer points, placed one upon the other. In other words, cumulative visibility map is summing up all viewsheds, where visible value is 1 and not visible 0. 

To begin, we have to create our viewpoints: use the "Create viewpoints" module and choose desired parameters. Here, the viewing height is set to 10 metres, for a hypothetical tower-based observer. His/her maximum view radius is set to 5km, supposing that further away he/she would not be able to discern a potential threat (these are just mock parameters, no science here…). 

![2020-03-15-create.jpg]({{site.baseurl}}/figures/2020-03-15-create.jpg)

Now we can create our cumulative viewshed. We have to choose the "Addition" option, which is also set as the default. We can also tick the box for earth curvature correction, even if high precision is not really needed in our case.  

![2020-03-15-analysis.jpg]({{site.baseurl}}/figures/2020-03-15-analysis.jpg)

![2020-03-15-raw.jpg]({{site.baseurl}}/figures/2020-03-15-raw.jpg)
*Cumulative viewshed: raw output.*

We can now classify our cumulative viewshed model in order to isolate areas that receive particular attention. I will only use raster visualisation here, without producing a separate reclassified raster. We simply adjust the colour ramp to extract three arbitrary classes: low visibility, medium visibility, high visibility. Our first model seems to indicate that a particualr attention was paid to the surrounding sea, even if dense view overlaps appear inland as well.  

![2020-03-15-style.jpg]({{site.baseurl}}/figures/2020-03-15-style.jpg)

![2020-03-15-visibility_from.png]({{site.baseurl}}/figures/2020-03-15-visibility_from.png)

## Reverse viewshed 

Let us now ask another question, concerning the visual impact of ancient towers. From which areas a random passer-by would feel observed? Or, to put things into contemporary perspective, from which areas would a tourist have a particularly good sight of ancient towers (setting aside their poor state of conservation). 

Our previous model was not parametrised for this problem. We have modelled a situation where an observer, placed atop a tower, is looking to the bare ground. However, now we need to simulate potential observers anywhere in the landscape. This can be achieved by tweaking the target height parameter which, normally, determines the height above the bare terrain that the observer is looking to. 

![2020-03-15-views.png]({{site.baseurl}}/figures/2020-03-15-views.png)
*Views from vs views towards a central point.*

Note that a single line of sight is valid in both directions: the path of a light ray from A to B is the same as from B to A. Of course, human visual capacities do not work that way, if I can see A, it doesn’t imply that A sees me – but if it were the case, our views would be nourished by the same light channel. Therefore, if we reverse viewshed parameters and set the target height to human eyelevel while the observer's height is zero, we will effectively model a situation where a large number of potential observers is looking to a single point, the one that was previously occupied by the tower.

Remember: observer height and target height parameters are interchangeable, they are named this way for simplicity reasons. The “observer point” is just a central point from or to which the visibility is calculated. So, if our previous observer position, a tower, has now become the object seen, we should consider its apparent height above the horizon. Let’s suppose that at least top 5 meters have to be in view on order for it to be perceived: the “observer height” will now be 10 - 5 = 5 metres. We can, of course, set parameters to any desired value, in order to simulate a wide range of potential situations, such as an observer in a car and target occupied by a wind turbine… 

![2020-03-15-targets.jpg]({{site.baseurl}}/figures/2020-03-15-targets.jpg)

All we need to do now is to change the parameters. We can do that a) by editing values in the previously created file, or b) creating a new observation points file. The second option is clearer in my view, that way we can easily keep track of different models. 

![2020-03-15-visibility_to.png]({{site.baseurl}}/figures/2020-03-15-visibility_to.png)
*Visibility of towers from the surrounding landscape.*

Now we have our model of tower visibility for a random passer-by. It is quite similar to the previous one since the parameters were only slightly changed. We could go on and check the difference between two models by subtracting them. That way, we may find areas which were “covertly observed”, where a passer-by wouldn’t have a tower in clear sight, while still being observed. But that’s for another tutorial…  
 
## Data sources

Greek towers dataset: Ashton, N. G. and Pantazoglou, E. Th. (1991): Siphnos: ancient towers BC. Athens. 

Elevation model: [NASADEM](https://earthdata.nasa.gov/esds/competitive-programs/measures/nasadem) with 30m resolution.

## Software

QGIS Visibiliy analysis: [zoran-cuckovic.github.io/QGIS-visibility-analysis/](https://zoran-cuckovic.github.io/QGIS-visibility-analysis/).

Happy mapping!
