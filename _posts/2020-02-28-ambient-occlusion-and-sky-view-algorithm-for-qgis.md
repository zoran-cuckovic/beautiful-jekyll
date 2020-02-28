---
layout: post
published: false
title: Ambient occlusion and sky-view algorithm for QGIS.
---
Ambient occlusion is a concept developed in 3D modelling and visualisation, it measures the exposition to the ambient light of each model element. The idea is to simulate the diffuse, scattered light that bounces off various surfaces. Such light may not have an identifiable source, as for instance in foggy environments or in cases of large numbers of reflective surfaces. Ambient occlusion models produce very realistic renderings which capture the dim light in tight spaces and corners (Figure below).

![Gears]({{site.baseurl}}/figures/20-02-gears.jpg)
*Representing 3D volumes using ambient occlusion technique ([pinterest.com](www.pinterest.fr/pin/599963981589528927/)).*

![Diagram]({{site.baseurl}}/figures/20-02-diagram.png)
*Real life illustration of the sky-view principle (Palagruža island, Adriatic Sea, [wikimedia.org](https://commons.wikimedia.org/wiki/File:Lighthouse_on_top_of_Palagru%C5%BEa.jpg)).*


In the image above, water line approximates the horizontal plane for a sea level location (the photographer’s position). On the open sea, his/her sky view would be 100%, but here an island is blocking a small portion of the sky. The effect is inversely proportional to the distance from the island (the closer we get, the less light we receive). The terrain openness, however, will never surpass 50% on the open sea, as only half of the surrounding sphere will remain unblocked. If we specify short sphere radius, say 100 meters, we will obtain openness values well above 50% for the lighthouse position, as in this case the light-blocking sea level will be situated below the lighthouse. 

Openness and sky-view factor are now available in the [Terrain shading plugin for QGIS](https://zoran-cuckovic.github.io/QGIS-terrain-shading/). As in other common approaches, these metrics are estimated with a sample of lines of sight, projected from each terrain element (most often a pixel). As of writing, 8 lines are used. As a side-note, this plugin already features a shading algorithm inspired by the principle of ambient occlusion; the [shadow depth method](https://landscapearchaeology.org/2019/qgis-shadows/) models the depth-dependant shadow translucency. 

![Banks penninsula]({{site.baseurl}}/figures/20-02-banks_simple.jpg)

This simple sky-view factor shading of Banks peninsula (New Zealand) is ideally suited to rrender the intricate ridge network that developed through erosion of the volcanic terrain. We can also add some shadow effect (using QGIS Terrain shading plugin) to enhance the impression of depth (even if the example below may be a bit exaggerated).   

![20-02-banks_svf_shadows.jpg]({{site.baseurl}}/figures/20-02-banks_svf_shadows.jpg)

## Refinement – calculations on an inverted DEM

If we observe carefully the images above, we may notice that the sky-view factor is more efficient for rendering ridgelines than valley bottoms and drainage channels. This is probably not a major issue, but let’s try to compensate for this effect. 

In order to provide a better impression of valley bottoms, we need to invert the DEM, as a glove, so that valleys become ridgelines and vice versa. That’s elementary, Sherlock would say, just multiply the elevation model by -1 (use QGIS raster calculator `my_dem * -1`). We can now do all our analyses as usual. 

Metrics obtained using this technique are called negative openness and, by analogy, negative sky-view factor. However, it’s just a hack which has no intuitive explanation, the result is not related to a real-world phenomenon.  

![20-02-banks_inverted.jpg]({{site.baseurl}}/figures/20-02-banks_inverted.jpg)

This image represents the result of sky-view algorithm over an inverted DEM. Note the superior rendering of deep drainage channels, which now appear as fine black lines. The overall sharpness is also significantly improved. Unfortunately, the model doesn’t convey the feeling of depth, the terrain seems flattened and schematic. 

To obtain the best from the both worlds, we can combine the usual sky-view factor with the negative one, as on the figure above. Here, the negative svf is overlaid as semi-transparent layer using the “Overlay” blending mode (see screenshot below). Our previous svf models is now sharper and more detailed in low lying areas, while still preserving the ambient occlusion effect that produces the 3D feeling. 

![20-02-banks_combined.jpg]({{site.baseurl}}/figures/20-02-banks_combined.jpg)
*Combined positive and negative sky-view factor.*

![20-02-layer_style.jpg]({{site.baseurl}}/figures/20-02-layer_style.jpg)
*QGIS stlye used for the negative sky-view factor overlay. Valleys are represented with an inverse scale (white to black) and superposed as semi-transparent layer over the usual sky-view model.

Happy mapping!
