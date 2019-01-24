---
author: Zoran
categories:
- Spatial analysis &amp; GIS
date: 2018-05-25 16:57:53
guid: https://landscapearchaeology.org/?p=246
id: 246
layout: post
permalink: /2018/polar-diagram/
tags:
- qgis
title: Polar (circular) diagram
---

Orientation of geographic features can be an important piece of information, for instance when studying ancient field systems or analysing geological formations. The problem comes when we try to summarise such data graphically . Standard histograms are not ideal because they cut through the continuous distribution - one cannot easily understand the relationship between the beginning and the end of the diagram (which should stick together). Polar diagram is what we need, but it cannot be made without some fiddling around.

<a href="https://3.bp.blogspot.com/-L93oFU5wimQ/WgbxUnriF5I/AAAAAAAAA2A/9Odg-QlGj3o7X84AZlXDWaiV9La2ugElACLcBGAs/s1600/2017-11-Polar-graph.jpg"><img src="https://3.bp.blogspot.com/-L93oFU5wimQ/WgbxUnriF5I/AAAAAAAAA2A/9Odg-QlGj3o7X84AZlXDWaiV9La2ugElACLcBGAs/s400/2017-11-Polar-graph.jpg" alt="" /></a>

There already exists a plugin called <a href="https://plugins.qgis.org/plugins/LineDirectionHistogram/">Line direction histogram</a> that does the job quite fine. However, QGIS comes with great matplotlib python library for data visualisation (windows version at least) which can be tweaked in all imaginable ways (colours, offsets etc.). The following script is simply passing data to matplotlib, directions have to be pre-calculated beforehand.

<pre><code>##input_layer=vector
##azimuth_field=field input_layer
##bin_count=number 32
##hollow_radius=number 0

"""
This script is used for generating circular graphs 
using matplotlib

More details on: www.qgiswhisperer.com/2017/11/polar-diagram.html
"""

import numpy as np
import matplotlib.pyplot as plt

input = processing.getObject(input_layer)
provider = input.dataProvider()

fieldIdx = provider.fields().indexFromName(azimuth_field)

features = input.getFeatures()

out=[]

for f in features: 
    v = f[fieldIdx]
    if 0&lt;=v&lt;=360: out.append(f[fieldIdx])  

# the following code is mostly adapted from : 
# http://stackoverflow.com/questions/22562364/circular-histogram-for-python
N = int(bin_count)
theta = np.linspace(0,  2 * np.pi, N, endpoint=False)
         radii, labels = np.histogram (np.array(out),   
         bins=np.linspace(0, 360, N+1, endpoint=True)
width = 2*np.pi  / N

ax = plt.subplot(111, polar=True)
#put north to top , arrange clockwise, give geographic labels (instead of angles)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

bars = ax.bar(theta, radii, width=width,bottom=hollow_radius)# 

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.8)

plt.show()
</code></pre>

NB. QGIS may crash when saving the image in .png format - .jpeg works better (<a href="http://hub.qgis.org/issues/13982">http://hub.qgis.org/issues/13982</a>)