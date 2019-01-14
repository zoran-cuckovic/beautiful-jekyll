---
id: 244
title: Sorting a table to order lables from north to south
date: 2018-04-23T16:54:40+00:00
author: Zoran
layout: post
guid: https://landscapearchaeology.org/?p=244
permalink: /2018/table-sorting/
categories:
  - 'Spatial analysis &amp; GIS'
---
Numerical labels are very handy for relating data in a table catalogue to a map, especially when the amount of data is too large for a simple eyeball scan (more than 10 to 15 labels). Imagine having some 50 sites stored alphabetically in a catalogue: how do you find the site n° 32 on the map? The simplest approach is to order site labels on the map in some meaningful manner, typically in ascending order from north to south.  
    

[![](https://4.bp.blogspot.com/-8IMj8yhVYoA/WgR-S2vdH7I/AAAAAAAAAzw/0SQ5Xg2n-uYsfSbUQcLGmrqbN_Qrpc-9QCLcBGAs/s1600/2017-10-order2.PNG)](https://4.bp.blogspot.com/-8IMj8yhVYoA/WgR-S2vdH7I/AAAAAAAAAzw/0SQ5Xg2n-uYsfSbUQcLGmrqbN_Qrpc-9QCLcBGAs/s1600/2017-10-order2.PNG)

To obtain this we can use the Query builder which can talk SQL (sort of).    
  
1) Create fields for x and y coordinates using **Field calculator** (_$x_ returns the x coordinate and _$y_ the other one).  
  

[![](https://2.bp.blogspot.com/-LiqKs43MuT0/WgWHexIBd_I/AAAAAAAAA0k/2WNxNG8m4W8qzD8KOqXNw9zdRD5eLPv3ACLcBGAs/s1600/2017-11-fieldcalc1.PNG)](https://2.bp.blogspot.com/-LiqKs43MuT0/WgWHexIBd_I/AAAAAAAAA0k/2WNxNG8m4W8qzD8KOqXNw9zdRD5eLPv3ACLcBGAs/s1600/2017-11-fieldcalc1.PNG)

2) Open the query builder under **Layer Properties > General**, and enter an expression with ORDER BY clause. We need to make a mock query before that, so if you do not want any exclusions enter a condition that all elements would satisfy (e.g. ID >= 0 or x_coordinate > 0 etc ...).  
  
Attention: textual criteria are denoted by single quotes ( ' ) .  
  
For ordering north to south we need to use the field containing the y coordinate, and that in a reverse order (for typical coordinate systems of the northern hemisphere, at least): this is what the DESC clause means (descending order). If there are points with same y coordinates, we can add ordering on x axis, as below. Test and click **Apply**, when finished.  
  
  

[![](https://3.bp.blogspot.com/-nCMCRkCb__k/WgWH6fn6fII/AAAAAAAAA0o/1nBYwTueNEMeh1siVot5_KumKBuqi4K7wCLcBGAs/s1600/2017-11-order-by.PNG)](https://3.bp.blogspot.com/-nCMCRkCb__k/WgWH6fn6fII/AAAAAAAAA0o/1nBYwTueNEMeh1siVot5_KumKBuqi4K7wCLcBGAs/s1600/2017-11-order-by.PNG)

3) Now return to the field calculator and add a new field for ordered labels. The expression to return the row number is ... _$rownum_ or _@row_number_ for QGIS 3. And voila!  
  
  

[![](https://4.bp.blogspot.com/-RkyGbM7K2mU/WgWJjVmmwTI/AAAAAAAAA00/m0z_jFCvKREsh8SRQKsbDn0ihl0BsLBhACLcBGAs/s1600/2017-11-fieldcalc.PNG)](https://4.bp.blogspot.com/-RkyGbM7K2mU/WgWJjVmmwTI/AAAAAAAAA00/m0z_jFCvKREsh8SRQKsbDn0ihl0BsLBhACLcBGAs/s1600/2017-11-fieldcalc.PNG)

  
  

### Problems

I had some problems, namely when assigning the row number to a "virtual field" or to the label expression (?) It would certainly be cleaner to use virtual fields... Also, be sure to click all options for refreshing the query builder output (Test Query, Apply etc.).  

### Tricks

Usually the x or y coordinate are precise enough to be unique, which means that the ordering will be only on the first specified axis. This may produce unpleasing results, forcing the reader to scan the map in horizontal lines. We can experiment with relaxing the coordinates to, say, 10 kilometres precision (on the first axis!) to relax the criteria and use the second axis as well \[e.g. `round(y, 10000)`\]  
  
**PS.** There is also a sorting function integrated in the table view (upon a right click on a column name), but it just didn't work for me (?) .