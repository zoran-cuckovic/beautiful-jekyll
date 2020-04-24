---
layout: post
published: false
title: 'Visibility index for QGIS : finally there !'
---

Welcome visibility index algorithm, aka total viewshed, now available in [QGIS Visibility analysis plugin](http://www.zoran-cuckovic.from.hr/QGIS-visibility-analysis/). This metric informs us on the size of the visual field for any location across a given terrain, normally each pixel in a gridded digital elevation model (DEM). At first, visibility index resembles other terrain indices such as topographic position, terrain roughness, etc. However, the visual structure of the landscape is essentially a question of human (or animal) perception and has to be evaluated within a specific cognitive/perceptual framework. Rather than as a terrain quality, I like to think of visibility index as a model of visible scene quality.  

![20-05-01-window.jpg]({{site.baseurl}}/figures/20-05-01-window.jpg)


Visibility index is calculated as the ratio of positive visual connections: 1.0 or 100% implies that a point can be seen from all of its neighbours. In fact, we have two options when mapping these positive views. The first one is to assign the value to the locations seen, this can be termed as incoming views. The second option is to map positive views to observer locations, these are then outgoing views. This view direction parameter can be used to distinguish between visual exposition of terrain features and the visual coverage from each terrain location. 

![20-05-01-direction.png]({{site.baseurl}}/figures/20-05-01-direction.png)
*Visibility is not reciprocal: we can choose to model either the observer’s perspective or the perspective of the observed one. *

The thing with visibility index is that it takes *days and weeks of computing* (see for instance Gillings 2017 who reports 300 hours of heavy calculation). Using standard GIS algorithms, you’re lucky if it takes only overnight! The reason is in the complexity of visibility calculations. Suppose that it takes 1 second to produce a single viewshed (field of view surface): for a 5 million pixel DEM (which is not large at all) this amounts to 1300 *hours* of computing.

These are serious algorithmic problems that are not easy to solve. I’ve coded a solution which a) eliminates calculation redundancy and b) takes the maximum advantage of spatial correlation of geographic data. It works as follows.

![20-05-01-lines.png]({{site.baseurl}}/figures/20-05-01-lines.png)
*Untangling lines of sight for multiple viewshed calculation.*

Note that typical viewshed is calculated by projecting lines of sight form an observer point in all directions in such a way as to touch all pixels within the specified radius. Now, the procedure can be broken in two operations: tracing lines and evaluating heights of pixels. In case when observer points occupy the centre of individual pixels the set of radiating lines can be (and should be) exactly the same for each point. If a certain line of sight starting in a pixel of row 10, column 12 is finishing in a pixel row 45, column 46, then the one for the observer on (20, 22) will finish in pixel (55, 56). We translate the coordinates by 10. Now, when all possible lines of sight describe same translations for all other pixels in a grid, we can apply each line of sight to all pixels simultaneously (rather then to repeat the procedure for each observer point). We’ve halved (at least) the calculation complexity. 

![20-05-01-lines-sample.png]({{site.baseurl}}/figures/20-05-01-lines-sample.png)
*Sampling lines of sight: 16 lines.*

The second optimisation relies on spatial correlation of typical DEM elements. Think of two adjacent pixels in a DEM: their values will most likely be very similar. Only in the case of standing architecture or very steep cliffs can we expect abrupt changes. Therefore, we can safely sample only a fraction of pixels and still obtain realistic visibility index. However, sampling observer locations is not the ideal method since we cannot easily predict their optimal positions: how many should occupy high ground vs low ground etc. Much better approach is to sample lines of sight, for instance we can take 8 lines of sight from each DEM pixel. Even such low number obtains a surprisingly accurate result. As we raise the number of these lines, the outcome slowly converges to a model produced with full range viewshed analysis. I’ve implemented 8 to 64 lines samples, to satisfy all levels of precision. 

So, how long does it take? On my old and tired computer, with no CPU/GPU optimisation or whatever, it takes some 25 minutes for a 31.2 million pixel DEM (default parameters; 16 lines sample and 3 km radius). Not really a blink of an eye, but reasonable at least: these are viewsheds for 30 million observers. 

The algorithm is based on Numpy library which can itself be optimised, but I didn’t yet venture into these grounds: to be continued… Anyway, here it is, the first usable and reasonably efficient visibility index algorithm out there :).