#FLM: Export oRight to Lowercase pairs to CSV

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

output = open(dir+'/my-oRight-toLower-Kerns.csv', 'w')

# Print nRight 
nRight = kerning.getRight('o')
LeftList = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z');

for pair in nRight:
  if pair[0][0] in LeftList:
  	output.write( str(pair[0][0])+', '+str(pair[0][1])+', '+str(pair[1]))
  	output.write( '\n')

output.close()
print "Done!"