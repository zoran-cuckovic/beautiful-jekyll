---
author: Zoran
categories:
- Spatial analysis &amp; GIS
date: 2018-10-11 18:02:55
guid: https://landscapearchaeology.org/?p=331
id: 331
layout: post
permalink: /2018/installing-python-packages-in-qgis-3-for-windows/
tags:
- qgis
title: Installing Python packages in QGIS 3 (for Windows)
---

Python is in the heart of QGIS (or in the guts if you prefer), which enables us to use tons of third party Python libraries. In Linux systems, QGIS will use the main Python installation, but in Windows things get more complicated. QGIS has it's own Python, which means we end up with various Pythons on our machines...

This is how to proceed in QGIS 3.x in Windows (I work on Win. 7)
1. Open OSGeo4W shell (packed with QGIS in the start menu)
2. Type ```py3_env```. This should print paths of your QGIS Python installation.
3. Use Python's ```pip``` to install the library of your choice: ```python -m pip install {your library}```

[![](/wp/wp-content/uploads/2018/10/Capture.png)](/wp/wp-content/uploads/2018/10/Capture.png)

Remark: I don't need to open the shell as administrator -- but this could solve some problems if the program starts complaining about permissions.

**Option 2**

Packages can also be installed directly from within Python, but that is not the preferred approach. Open QGIS Python console (under Plugins >> Python Console) and type: 

```
>> import pip

>> pip.main(['install', 'my-package-name'])

```
Note that the arguments are given as a list [...] of 'strings'. 
