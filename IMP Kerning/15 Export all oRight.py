#FLM: Export all oRight pairs to CSV

# Credits:
# Pablo Impallari

import os.path
from robofab.world import CurrentFont

f = CurrentFont()
kerning = f.kerning

#Do some work
print "Working..."
path = f.path
dir, fileName = os.path.split(path)

output = open(dir+'/my-oRight-Kerns.csv', 'w')

# Print oRight 
nRight = kerning.getRight('o')
for pair in nRight:
  output.write( str(pair[0][0])+', '+str(pair[0][1])+', '+str(pair[1]))
  output.write( '\n')

output.close()
print "Done!"