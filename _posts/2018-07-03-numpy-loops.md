---
id: 143
title: Looping through numpy arrays (e.g. moving/rolling window)
date: 2018-07-03T17:34:56+00:00
author: Zoran
layout: post
guid: http://landscapearchaeology.org/?p=143
permalink: /2018/numpy-loops/
# image: /wp/wp-content/uploads/2018/06/2017-11-numpy3.png
categories:
  - Uncategorized
---
Numpy is the cornerstone of matrix based calculations in QGIS (and elsewhere). It does wonders with raster data (unless it hits the limit of available live memory...).  
  
A recurrent problem with Numpy is the implementation of various looping routines, such as the sliding window which is frequently used in image filtering and other approaches focused on cell neighbourhood. Below is the illustration of the problem: for each cell the window needs to query a specified neighbourhood (square, circular or other).  
  

![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/2017-11-numpy1b.png)

Now, there exists a solution in the form of "stride tricks" within the Numpy library. However it is really cryptic (the [SciPy cookbook](http://scipy-cookbook.readthedocs.io/items/GameOfLifeStrides.html) uses the "devious" epithet); after all the very name "tricks" implies it being ... tricky. Numpy documentation actually [discourages its use](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.lib.stride_tricks.as_strided.html). We can do it in a more understandable manner - which also means more configurable - and without any particular computational overhead.  
  
Let's first examine the problem. Without Numpy we would need four nested loops: two for traversing the matrix and two for the analysed window.  
  
``` 
#Level 1: traversing the matrix 
for y in range(rows):
    for x in range(columns):

        #Level 2: traversing the window (3x3 size) 
        for win_y in range(y-1,y+2):
            for  win_x in range(x-1, x+2):
                temp_sum += matrix[win_y, win_x]

       #Analysis inside the window is finished
       #Write result to a copy of the input matrix
       output[y, x] = calculate_something(temp_sum) 
```
We can immediately see that the level 2 loop can be easily replaced with a Numpy window: `win = matrix[y-1: y+2, x-1: x+2]`. Easy enough ... but this is not the ideal approach. The window has 9 cells, while the matrix would have millions: shouldn't we focus on the level 1 loop instead?  
  
To avoid the level 1 loop we need to move the entire matrix, as when overlapping two sheets of paper. We're now working on offsets between the two - which is the only tricky part. The (0,0) cell of the window now corresponds to all cells in the matrix that are on the upper left relative to analysed cells - which simply means shifting the entire matrix to the upper left. In order to move the matrix in that direction, we need to calculate offsets in relation to the central point. That would be `window_index - window_radius` , which for the upper left cell gives (-1, -1) (see below).  
  
![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/2017-11-numpy2.png)
  
The only problem resides in handling these offsets on the level of the entire matrix. We need to extract matrix views that do not spill over the borders AND that match each other in size and shape. The overlap issue is represented on the illustration below.  
  
![](http://landscapearchaeology.org/wp/wp-content/uploads/2018/06/2017-11-numpy3.png)
  
This problem can be avoided with padding: adding extra row(s) and column(s) around the edges. The depth of the padded area should correspond to the maximum possible offset. The solution is now as follows:  
  
```
import numpy as np

#a mock dataset
data=np.random.rand(5,5)

rows, columns = data.shape
temp_sum = np.zeros((rows, columns))

# create a padded copy
pad = 1 
matrix = np.pad(data, pad, 'edge')

# Level 2: traversing the window (3x3 size)
for y in range(3):
    for x in range(3):

        # Level 1: handling the matrix 
        # (rows, columns = data.shape !)
        temp_sum += matrix[y : rows + y,
                          x : columns + x]

#Analysis inside the window is finished
output = calculate_something(temp_sum) 
```
And we're fine!  

### Refinement: unpadded solution

It's kind of ugly to use pads. We are producing copies of the original data, which can be particularly problematic for large offsets. Furthermore, padding may influence the result in unexpected ways.  
  
Returning to the illustration above, we can see that the cropped window view cannot match the main view (the one pointing to the original and/or temporary data). The latter also needs to be cropped, but in the opposite direction. This is logical: the top row cannot have a neighbour to the north anyway.    
  
Therefore, we need to adjust both views at the same time. Note that these views are opposite to each other, which means that we can play with swapping: when the window is placed to the north-west (-1, -1), the main view is to the south-east (1,1), but when the window is on the south-east  (1,1), the main view will be on the north-west (-1, -1).  
  
To finish, let's throw in an additional parameter for steps - the range to be skipped between analysed cells (see [numpy docs](https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html) for steps). Let's now wrap all this to a function which will return matching views:  
  
```
import numpy as np

"""
Function returning two matching numpy views for moving window routines.
- offset_y and offset_x refer to the shift in relation to the analysed (central) cell 
- size_y and size_x refer to the size of the data matrix (not of the window!)
- view_in is the shifted view and view_out is the position of central cells

All comments are welcome at landscapearchaeology.org/2018/numpy-loops
"""

def view (offset_y, offset_x, size_y, size_x, step=1):
 
    x = abs(offset_x)
    y = abs(offset_y)
 
    x_in = slice(x , size_x, step) 
    x_out = slice(0, size_x - x, step)
 
    y_in = slice(y, size_y, step)
    y_out = slice(0, size_y - y, step)
 
    # the swapping trick    
    if offset_x < 0: x_in, x_out = x_out, x_in                                 
    if offset_y < 0: y_in, y_out = y_out, y_in
 
    # return window view (in) and main view (out)
    return np.s_[y_in, x_in], np.s_[y_out, x_out]
 
#a mock dataset
data=np.random.rand(5,5)
window = 3

radius = int(window/2)
 
rows, columns = data.shape
temp_sum = np.zeros((rows, columns))
 
# Our window loop  
for y in range(window):

    #we need offsets from centre !
    y_off = y - radius

    for x in range(window):
        x_off = x - radius
 
        view_in, view_out = view(y_off, x_off, rows, columns)
 
        temp_sum[view_out] += data[view_in]

#Analysis inside the window is finished
output = calculate_something(temp_sum) 
```
 
Perhaps we could do better, but the advantage of this approach is that we can adapt it to any imaginable shape of the moving window - because we conserve the loop over window cells. We are also working on views, as opposed to hard copies of the data, which is what Numpy likes a lot.  
  
Any suggestions are welcome!