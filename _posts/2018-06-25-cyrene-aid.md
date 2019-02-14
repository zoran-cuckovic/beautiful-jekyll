---
layout: post
author: Zoran
categories:
  - Spatial analysis &amp; GIS
date: 'Mon Jun 25 2018 14:00:47 GMT+0200 (heure d’été d’Europe centrale)'
guid: 'http://landscapearchaeology.org/?p=23'
id: 23
permalink: /2018/cyrene-aid/
tags:
  - qgis
  - tutorial
title: 'My first QGIS map: the aid from Cyrene'
published: true
subtitle: Learn how to make a basic map in QGIS
---

![Cyrene, Lybia](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/Cyrene.png)
*Cyrene, Lybia*



Sometime during the reign of Alexander of Macedon a famine broke out in Greece. We don't have many documents reporting the gravity of situation; apparently Greece was suffering much during the tumultuous years just before and after the Macedonian conquest.


The prosperous city of Cyrene, on the coast of today's Libya, came to rescue and sent an extraordinary quantity of  grain, all in all some 40 to 50 thousand tons. Our main source of information is an inscription graved in marble and boastfully displayed in one of main public areas in the city centre.


The inscription details quantities of the shipped grain: it is basically a shipping list mentioning 43 recipient communities and two women, mother and sister of Alexander himself. Such data just begs for a map. I didn't find a nice map of the Cyrenian shipments, so I made it myself, after the data in  Garnsey (1998). The process of map design makes a perfect introduction to basic GIS cartography.


![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/Garnsey.jpg) 
*Data used for the map (one Aeginetan medimnos equals 60 kg; Garnsey 1988, 160)*

## 1. Placing the points

Let's first load some geographical data, to get started. We will use Google Maps:

- Go to **Web >> Open Layers Plugin**, and choose Google Maps (other proposed maps will do, as well) [! you need an internet connection to pull the data !]

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/EPSG.png)

What we have now is a map with its proper coordinate system, which is displayed at the bottom right corner (it should be EPSG: 3857).

Now we need to pinpoint ancient cities on the map - which is not that simple. The direct approach would be to eye-ball between historical maps and the data that is now visible in QGIS. However, finding locations for some forty historical places, most of which do not exist any more, or have their names altered beyond recognition, is a quite a chore. It is much more convenient to import a historical map in GIS and place it in correct position.

Our next step will, then, be to geo-reference a scanned document. Note that geo-referencing is always done in a specific system of geographic coordinates. Your scanned image will be assigned coordinates that match coordinates of *another map* and not some perfect, universal system (that we wish existed...). (QGIS can work with files in different systems simultaneously, but you should not use that before understanding the basics of geographic projections.)

- We now open Raster >> Goreferencer and load the scanned map.
- Add reference points (Edit >> Add point), first to the scanned document and then find matches on the loaded web map.
 
![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/Georeferencer-settings.png)

- After you've found 4 or 5 points (we would need more for precise referencing) we can project our document to geographical space (**Settings >> Transformation settings**).
- Most important is that the definition of the projection system (**Target CRS**) match the one of the base map: in our case it should be EPSG: 3857. If these two do not match, you need to select the appropriate system. 
- Check that *Load to QGIS when done* is on and then go to **File >> Start georeferencing** (or hit the green arrow). The map should now appear in its place in QGIS! 

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/Georeferencer.png)

Our next task is to enter data in a GIS file. These, again, inhabit the same geo-referenced habitat as our maps.

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/New-Shapefile.png)

-  Push the "New Shapefile" button or go to **Layer >> Create Layer >> New Shapefile**.
-  First, let us keep track of our geographic reference systems: choose the one that matches the project system (for Google maps it's EPSG: 3857).
- We will, then, define and add data fields (**Add to fields list**). In our case let it be one for place names and another for quantities of shipped grain. Take care to define the appropriate data type (numeric, textual) and the maxim length - 80 characters, proposed by default, might not be enough.
- All that is left now is to enter the data. Toggle the edit button and add points...

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/Editing.png)

## 2. Creating a map

The next step is to produce an informative map which will show the quantity of the grain, besides geographic locations of recipients. To achieve that will will vary the size of cartographic symbols.

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/Style.png)

 - Right click the point layer, choose **Properties >> Style**
 - We need *Graduated symbols* that vary according to quantities of shipped grain, stored in the numerical data field (labelled as "Column" in QGIS window)
- Set the desired colour and size range (mine is 2 to 7 millimetres).
- QGIS actually classifies the continuous values in distinct ranges (bins). The type of classification is chosen under Mode (mine is *Natural breaks*).
(... play with these settings to achieve something that might be considered as "nice"...)

Let's add labels (if needed...):

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/Labels.png)

- Labels are accessible from the Layer properties window (just under the style).
- First two options are similar to style settings. First select *Show labels for this layer*. Note that the first option (No labels) will hide labels, rather than delete them, thus conserving all label settings. Then choose the data field to be displayed, which is here labelled as "Label with".
- Play with Text formatting and other settings. I'm using here **Buffer** (*Draw text buffer*) and custom **Placement** set to *Offset from point*. 

Last, but not least, we can add a more "historical" feeling to the map:

- Let's use the amazing watercolor background by Stamen : go to **Web >> Open Layers >> OSM/Stamen >> Watercolor**

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/Screen-QGIS-capture.png) 

Finally, we can pass to map design!

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/Composer.png)

- Map making is done in a separate module which is accessed through Project >> New print composer (we don't care about the composer title that QGIS will be asking) 
- The canvas will appear blank : the actual map has to be added through Layout >> Add Map.
- You will notice that you cannot zoom in or out the predefined window: we are now dealing with a static piece of (digital) paper! In order to adjust the view you need to toggle the Layers >> Move content option. Now the inside of the map will behave like the main GIS window. To revert to the "paper view" toggle the Move item option.
- Add a scale through Layers >> Add scalebar.
- Legend is added through Layout >> Add legend. It probably won't be ideal, displaying project layers that we wish to hide. Click on the legend and it will appear under Item Properties to the right. Un-check the Auto update option and then remove unwanted items with the minus sign. There are many other options there (text font, colour, symbol size etc...): play with them!
- When finished, go to Composer >> Export as image (or as .pdf, or as .svg file).

And there we have it: a map that speaks a thousand words! 

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/map.png)

Indeed, the map has some stories to tell. First, how come that the southern part of the Greek mainland, the Peloponnese, escaped the famine? Well, quite likely it didn't, the reason for the lack of shipments to that area is probably of political nature. The city-state of Sparta, situated in this southern region, showed particular resistance to the new-coming Macedonian rule. Another hint of possible political underpinnings of the shipment can be found in large quantities sent to otherwise marginal region of Epirus in the north. The recipients there were, as a matter of fact, the mother and the sister of Alexander himself.

Happy mapping (and story-telling)!

### Bibliography

Berthelot, H. 2012, [La « stèle des céréales » de Cyrène](http://lettres.sorbonne-universite.fr/IMG/pdf/BerthelotBAT.pdf)
Bresson, A. 2011, Grain from Cyrene [DOI:10.1093/acprof:osobl/9780199587926.003.0004](http://www.oxfordscholarship.com/view/10.1093/acprof:osobl/9780199587926.001.0001/acprof-9780199587926-chapter-4)

Garnsey, P. 1988, *Famine and Food-Supply in the Graeco-Roman World, Responses to Risk and Crisis*, Cambridge.
