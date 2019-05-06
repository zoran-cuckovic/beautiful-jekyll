---
layout: post
author: Zoran
categories:
  - Spatial analysis &amp; GIS
date: 'Wed Sep 26 2018 19:08:22 GMT+0200 (heure d’été d’Europe centrale)'
guid: 'https://landscapearchaeology.org/?p=296'
id: 296
permalink: /2018/mediterranean-land-visibility/
tags:
  - QGIS visibility plugin
  - qgis
title: 'Land visibility in the Mediterranean: a large scale model'
published: true
---

Visibility of land was a major consideration for ancient seafaring, for reasons of navigation and security. Even if the open sea travel must have been practised already by the Neolithic period, judging by the colonisation of remote islands and by the exchange of artefacts across the Mediterranean, the sight of the land remained a much desired navigational aid at least until the medieval period. The earliest evidence of seafaring date to astonishing 100 000 years before present (artefacts from <a href="https://www.peabody.harvard.edu/files/17_Ruunels_et.al_start.pdf">Preveli on Crete</a>).

Archaeologists frequently discuss the importance of land visibility for ancient seafaring, but without a useful geographical model. There is a map which is constantly reappearing in publications but the origin of which I couldn’t determine (<a href="https://books.google.fr/books?id=sZbqAAAAQBAJ">Tartaron 2103</a>, Fig 4.9, citing <a href="https://books.google.fr/books?id=qbYiW13TJ6UC">Broodbank 2000</a>, Fig 4, citing <a href="https://books.google.fr/books?id=yD49AAAAIAAJ">Chapman 1990</a>, Fig 59, citing a 1980’s publication I cannot access…). I suspect that these are derived from the model published by <a href="https://books.google.fr/books?id=B7SLWT2vpNcC">Aubet 2001</a>, below. However, hers is a type of book which doesn’t cite its sources (but still …).

![](/wp/wp-content/uploads/2018/09/Aubet-Phoenicians-Land-visibility.jpg)
*After Aubet 2001, Fig 35*

Anyway, the model that is being widely used was made by hand long time ago (that’s my guess at least) – and is quite problematic. It seems to represent the maximum theoretical visibility of land <em>without accounting for the atmosphere</em>. Yes, you can see Mount Etna some 200 km off the Sicilian coast … during five days in a year. Visibility at such distances is normally much affected by atmospheric conditions and aerosols produced at sea surface. Measurements of visibility distance in Athens rarely surpassed 50 kilometres (in the pre-pollution era: <a href="https://www.researchgate.net/publication/308039259_Long-term_visibility_variation_in_Athens_1931-2013_A_proxy_for_local_and_regional_atmospheric_aerosol_loads">see here</a>). I would consider 50 kilometres as more realistic figure for maximum visibility of the land. At least, I wouldn’t plan a travel relying on greater visibility ranges (without modern equipment).

Let’s, then tackle the issue with modern technology. All we need is an elevation model, GIS software, and … enough time to calculate visibility. Mediterranean is large, and the calculation is by no means a simple one. The procedure, however, is not that complicated – this is how I did it :

<h3>Dataset</h3>

We need a decent elevation model, but not too detailed in order to reduce the calculation overhead. I’ve chosen the <a href="https://www.usgs.gov/land-resources/eros/coastal-changes-and-impacts/gmted2010">GMTED2010</a> of 7.5 arc-second resolution, produced by USGS. On the equator, this amounts to 230 metres of horizontal resolution, but when re-projected to more northern latitudes the figure will decrease (in my case to 188 metres). This should be enough for large-scale analysis, I suppose, but is not ideal (imagine a terrain composed of blocks 200 metres large).

<h3>Isolating mountaintops</h3>

We need to make a smart choice of viewable terrain features (otherwise I would still be waiting for the calculation to finish). I’ve isolated all mountaintops surrounding the Mediterranean basin, where a mountain top is the highest elevation in a 5 km radius. Close to 70 000 such features were found, knowing that the vast majority of « mountaintops » are insignificant (dunes in Sahara produced quite a number of these). I didn’t have patience to clean all that.

<h3>Calculation</h3>

The <a href="http://www.zoran-cuckovic.from.hr/QGIS-visibility-analysis/">QGIS viewshed plugin</a> was used (no surprise, it's my baby); the latest version is <a href="/2018/visibility-analysis-0-6-4/">tuned to handle large rasters</a>. For the 150 km radius it took me some 14 hours or so, while for the 50 km model some 3 hours. The calculation time would obviously be much reduced by cleaning up the « mountaintops ». However, the algorithm didn’t take up too much live memory (less than 1 GB), so I just left it grinding in the background.

<h2>Results</h2>

[![](/wp/wp-content/uploads/2018/09/Model-150-km.jpg)](/wp/wp-content/uploads/2018/09/Model-150-km.jpg)
*Visibility of land up to 150 km*

.

[![](/wp/wp-content/uploads/2018/09/Model-50-km.jpg)](/wp/wp-content/uploads/2018/09/Model-50-km.jpg)
*Visibility of land up to 50 km*


The 150 km model resembles the historical one, cited in archaeological publications. However, such long distance is definitely an overestimation for real world atmospheric conditions. The 50 km model is much more interesting as it indicates important “visibility bridges” between opposing coasts. One such is situated between Sicily and Tunis (ancient Carthage) and another in the middle of the Adriatic Sea (the “spur” of the Italian boot). These have very interesting prehistoric record, no doubt related to seafaring.  The “invisibility” of much of the African coast is also interesting: we can imagine the importance of the enormous <a href="https://www.ancient.eu/Lighthouse_of_Alexandria/">lighthouse in Alexandria</a> (Egypt).

The cartography is not exemplary : the map needs some make-up to be publishable (to be continued...).
