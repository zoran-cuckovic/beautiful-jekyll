---
id: 331
title: Installing Python packages in QGIS 3 (for Windows)
date: 2018-10-11T18:02:55+00:00
author: Zoran
layout: post
guid: https://landscapearchaeology.org/?p=331
permalink: /2018/installing-python-packages-in-qgis-3-for-windows/
categories:
  - 'Spatial analysis &amp; GIS'
---
Python is in the heart of QGIS (or in the guts if you prefer), which enables us to use tons of third party Python libraries. In Linux systems, QGIS will use the main Python installation, but in Windows things get more complicated. QGIS has it's own Python, which means we end up with various Pythons on our machines...

This is how to proceed in QGIS 3.x in Windows (I work on Win. 7)
1. Open OSGeo4W shell (packed with QGIS in the start menu)
2. Type ```py3_env```. This should print paths of your QGIS Python installation.
3. Use Python's ```pip``` to install the library of your choice: ```python -m pip install {your library}```

<a href="https://landscapearchaeology.org/wp/wp-content/uploads/2018/10/Capture.png"><img src="https://landscapearchaeology.org/wp/wp-content/uploads/2018/10/Capture.png" alt="" width="677" height="342" class="aligncenter size-full wp-image-338" /></a>

Notes:
- I don't need to open the shell as administrator -- but this could solve some problems if the program starts complaining about permissions.  
