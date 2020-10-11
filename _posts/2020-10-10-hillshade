---
layout: post
published: false
title: 'Hillshade in QGIS: a new implementation in Terrain Shading module.'
tags:
  - QGIS Terrain Shading
---

 

Hillshade model of Požega valley (Croatia) 

Hillshade modelling is a standard form of terrain representation in cartography. The idea is to simulate lighting of a terrain from a certain direction (or multiple directions). The method is well known and constantly improved in GIS as a means of terrain visualisation. The basic principles of the hillshade method are quite simple (see below), but understanding and handling the outputs produced is less so. -- ? This is the first part of a series of posts on hillshade models that take an in-depth perspective on their geometric properties and aesthetic qualities. 
## The basics
In a nutshell, hillshade algorithm assigns a theoretical reflectance value to each terrain element (a pixel of a digital terrain model in most cases). Given a defined light source, such reflectance will depend on the inclination of each terrain element: those that are perpendicular to the light source will receive and thus reflect more light than those that are facing other directions (see Fig. 2). In GIS, hillshade algorithms normally do not aim to model truly realistic scenes; factors such as surface texture or various light qualities are not taken into account. For this reason the immediate output is rather artificial and usually needs additional treatment in order to provide a pleasing terrain representation. 
The formula commonly used is the one devised by the mathematician Johan Heinrich Lambert, which postulates that the reflectance value will vary according to the difference between illumination angle and surface angle (FIG ____). More specifically the amount of the reflected light will be proportional to the cosine of such angular difference (https://en.wikipedia.org/wiki/Lambert%27s_cosine_law). Imagine putting a piece of paper in front of a table lamp. The shadow of the paper on the table below will contract as you rotate or incline it, because you’re increase the angular difference between the surface orientation and the light source. Now, the size of the shadow corresponds to the amount of light received by the paper, it will therefore appear darker when capturing diminishing amounts of light. 
## Hillshade implementation in Terrain Shading module for QGIS
Such simple approach has proven to be useful in GIS, but it certainly has its drawbacks, namely a rather artificial output and poor flexibility for modelling different lighting scenarios. (Ambient occlusion is one of those: see [the post on ambient occlusion](____). 
Fig ___ angles
The [Terrain Shading module](______) that I developed for QGIS features a lambertian hillshade algorithm, but with an important modification. It enables to artificially exaggerate the angles of surface elements, and that in two directions, along the axis of illumination (longitudinal axis) and perpendicular to the illumination axis (lateral axis : Figure ____). These parameters enable to adjust light quality, and to render more detail than with standard cosine-law formula. 
FIG Terrain shading module for hillshade analysis. Note two settings for angular exaggeration (CIRCLE)  
Such two directional angular exaggeration is very useful for the detection and visualisation of faint terrain features that become visible only when illuminated form a specific angle. Lateral exaggeration in particular, will accentuate slopes that are often poorly rendered with standard lambertian hillshade. This may prevent the appearance of highly illuminated slopes that become washed out when directly illuminated, a frequent, undesired effect (see the comparison of images below).

FIG : parameters, etx   
