---
layout: post
published: false
title: Ambient occlusion and sky-view algorithm for QGIS.
---
Ambient occlusion is a concept developed in 3D modelling and visualisation, it measures the exposition to the ambient light of each model element. The idea is to simulate the diffuse, scattered light that bounces off various surfaces. Such light may not have an identifiable source, as for instance in foggy environments or in cases of large numbers of reflective surfaces. Ambient occlusion models produce very realistic renderings which capture the dim light in tight spaces and corners (Figure below).

![Gears]({{site.baseurl}}/figures/20-02-gears.jpg)
*Representing 3D volumes using ambient occlusion technique [pinterest.com](www.pinterest.fr/pin/599963981589528927/).*

![Diagram]({{site.baseurl}}/figures/20-02-diagram.png)
*Real life illustration of the sky-view principle (Palagruža island, Adriatic Sea [wikimedia.org](https://commons.wikimedia.org/wiki/File:Lighthouse_on_top_of_Palagru%C5%BEa.jpg).*


In the image above, water line approximates the horizontal plane for a sea level location (the photographer’s position). On the open sea, his/her sky view would be 100%, but here an island is blocking a small portion of the sky. The effect is inversely proportional to the distance from the island (the closer we get, the less light we receive). The terrain openness, however, will never surpass 50% on the open sea, as only half of the surrounding sphere will remain unblocked. If we specify short sphere radius, say 100 meters, we will obtain openness values well above 50% for the lighthouse position, as in this case the light-blocking sea level will be situated below the lighthouse. 

Openness and sky-view factor are now available in the [Terrain shading plugin for QGIS](https://zoran-cuckovic.github.io/QGIS-terrain-shading/). As in other common approaches, these metrics are estimated with a sample of lines of sight, projected from each terrain element (most often a pixel). As of writing, 8 lines are used. As a side-note, this plugin already features a shading algorithm inspired by the principle of ambient occlusion; the [shadow depth method](https://landscapearchaeology.org/2019/qgis-shadows/) models the depth-dependant shadow translucency. 

![Banks penninsula]({{site.baseurl}}/figures/20-02-banks_simple.jpg)

This simple sky-view factor shading of Banks peninsula (New Zealand) is ideally suited to rrender the intricate ridge network that developed through erosion of the volcanic terrain. We can also add some shadow effect (using QGIS Terrain shading plugin) to enhance the impression of depth (even if the example below may be a bit exaggerated).   

![20-02-banks_svf_shadows.jpg]({{site.baseurl}}/figures/20-02-banks_svf_shadows.jpg)

## Refinement – calculations on an inverted DEM
