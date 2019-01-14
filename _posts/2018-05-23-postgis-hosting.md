---
id: 239
title: 'Postgis database: free online hosting'
date: 2018-05-23T16:41:01+00:00
author: Zoran
layout: post
guid: https://landscapearchaeology.org/?p=239
permalink: /2018/postgis-hosting/
categories:
  - 'Spatial analysis &amp; GIS'
---
Postgis is _the_ database software for collaborative work in the GIS environment. Multiple users can connect to the database and edit the data without the fear of breaking down the system (except messing with each others edits - which is another type of issue).  
  
Assuming that the interaction between the database and the user is made through internet, we need to set up a hosted database - which complicates the affair.   
  
Hosting can be expensive, which is a problem for all those that would like to have a taste of collaborative GIS, but do not work on serious (read, funded) projects. Worry no more, there are solutions that can give us the taste of PostGIS for free - and without rather technical procedure of database setup.  

##  1) QGIS Cloud

The simplest solution is to use the [QGIS Cloud](https://qgiscloud.com/) and its [dedicated plugin](https://plugins.qgis.org/plugins/qgiscloud/). All you need is to open an account at the website, install the plugin and follow a couple of steps in the [tutorial](https://qgiscloud.com/en/pages/quickstart).   
  

![](https://1.bp.blogspot.com/-QFUepNen0g0/WgRfbfYn7WI/AAAAAAAAAzg/ltRQpiPPjOsSzswQ0C0xWIwPSf2RUgDeQCLcBGAs/s1600/2017-11-1.PNG)

  
However, all the data will be publicly available on their site, which may be a problem to some. The number of concurrent users is limited to 10 and the database size to 50 mb, which seems to be OK; teams of more than ten people working simultaneously sound like a serious project.  

## 2) Alwaysdata.com

Another solution, much less restrictive, is to set up a PosGIS database at the French hosting site [Alwaysdata](https://www.alwaysdata.com/). In this case we can fully explore the architecture of PostGIS - without a line of code. Here are the steps required to set up an on-line PostGIS database:  
  
1. Open an account and choose **PostgreSQL** under **Databases** in the main admin panel. (you can always opt for English in the upper right corner if the language of love is not your favourite).  
![](https://3.bp.blogspot.com/-JsDN5-TZYAU/WgMZA3Tyj4I/AAAAAAAAAwI/QFeXW8nUr3Yp5_GXWWuSu44bPUOm2Yj9ACK4BGAYYCw/s1600/alwaysdata%2B1.png)

2. Add a database, go to **Edit** and check **PostGIS**.    
![](https://3.bp.blogspot.com/-1WXgj5agtHA/WgMZMRoMjwI/AAAAAAAAAwQ/GVDmVX1cwbA9nXVBoF6zJFoRt3CqGcjbQCK4BGAYYCw/s1600/alwaysdata%2B2.png)
  
3. [optional] The account administrator will be the only user of the database. You can create more users through the **Add user** button, under **User management**. You can choose individual permissions, which is cool.   
![](https://2.bp.blogspot.com/-nb3R2khxwCc/WgMZZcuLDpI/AAAAAAAAAwY/QBThi0vC698uBBFC0bonArwNwsB1x7sggCK4BGAYYCw/s1600/alwaysdata%2B3.png)

4. Now, when you click on **PostgreSQL** you will obtain the data you need for an online connection. We have, then:  

*    address of the database (the host)
*    name of the database
*    user(s) name(s)
*    password(s)

We pass now to QGIS and connect to the database. The process does not differ from a connection to any shared database. The preferred procedure is through the QGIS Browser.  
  

![](https://2.bp.blogspot.com/-BP60yCMS9i0/Wgc4hC94feI/AAAAAAAAA3o/KZGVLrhc9I8KggtMTpKA5psmZ8rA3OLQACPcBGAYYCw/s1600/QGIS2.jpg)

  
Create a new connection, fill in the data (leaving the field _Services_ empty) and hit _Test connection_. The same module for online connection can be accessed directly from QGIS: when adding a new vector layer choose new PostGIS connection and fill in the same data.     
  

## Problems..

Are there some issues with this approach? Compared to QGIS Cloud environment, we have certainly much more freedom. What is more, we bypass the rather technical database set-up procedure (read: typing commands in a terminal). However, this is a free solution, provided by the benevolence of the hosting company. We have 100 Mb at our disposal and the account will get shut down upon longer inactivity (a couple of months or so). A serious project should come with a suitable hosting plan, anyway.