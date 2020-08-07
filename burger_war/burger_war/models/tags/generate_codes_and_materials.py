#!/usr/bin/env python
import os
for i in xrange(0,250):
    #os.system("rosrun ar_track_alvar createMarker %d" % i) #<1>
    #os.system("convert MarkerData_%d.png -bordercolor white -border 100x100 " +
    #          "MarkerData_%d.png" % (i, i)) #<2>
    with open("%04d.material" % i, 'w') as f: #<3>
      f.write("""
material %04d {
  receive_shadows on
  technique {
    pass {
      ambient 1.0 1.0 1.0 1.0
      diffuse 1.0 1.0 1.0 1.0
      specular 0.5 0.5 0.5 1.0
      lighting on
      shading gouraud
      texture_unit { texture %04d.png }
    }
  }
}
""" % (i, i))
