import frontmatter
from os import listdir
from os.path import isfile, join

import codecs #this is nasty...

"""
Bulk edit for tags in Jekyll posts. The script will attempt to
edit ALL FILES in the specified folder: you should place selected files
in a temporary folder. 
"""

# -------  INPUT PARAMETERS --------------

# TEMPORARY folder with selected files (do not specify the main _posts folder!)
folder = 'U:/Users/zcuckovi/Documents/GitHub/LandscapeArchaeology.org/_drafts/test/'

add_tag = 'qgis' #tag to be insereted

remove_tag= '' #tag to be removed

# ----------- ENGINE --------------------

for f in listdir(folder):

    file = join (folder, f)

    if not isfile(file): continue

    print (file)

    post = frontmatter.load (file)

    #print (post['title'])

    if add_tag:

        try:
            if add_tag not in post['tags'] :
                post['tags'] += [add_tag]
        except:
            #tags do not exist yet
            post.metadata['tags'] = [add_tag]

    if remove_tag :
        try:  post['tags'].remove(remove_tag)
        except: pass

    out = frontmatter.dumps(post)

    # https://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python/934203#934203
    o = codecs.open(file, 'w', 'utf-8')
    o.write(out)
    o.close()

