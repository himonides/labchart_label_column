#--------------------------------------------------------------------------------------------------------------------------------#
# ADInstruments LabChart experiment data processor for adding the label string onto all individual records between marked labels #
# copyright (c) 2019 Dr Evangelos Himonides, e.himonides@ucl.ac.uk                                                               #
# UCL Institute of Education                                                                                                     #
#                                                                                                                                #
# NB: 1. make sure that you use Python 3.x or higher and 2. that you don't have empty lines at the bottom                        #
#--------------------------------------------------------------------------------------------------------------------------------#

import re #import regular expressions module
import datetime #import datetime module so that we can print the timestamp for beginning and end

label = 'no_label' #initialise the label variable

textfile = open('data.txt', 'r') #open the data file for reading change to the name of your source file
outputfile = open('output.txt','w') #open (or create if it doesn't exist) the output file for writing

print(datetime.datetime.now()) #print timestamp

for line in textfile: #process all lines in input file
  match = re.search('\w+\n', line) #find the RegEx which finds a label entered in LabChart
  if match: 
    label = match.group(0) #if you match the RegEx
    print(label) #print what that is
    outputfile.write(line) #and write the current line to the output file
  else:
    newline = line.replace('\n', label) #if you don't perform the match, replace the new line character with the label variable contents
    outputfile.write(newline) #and write the current line to the output file  

textfile.close() #close read file
outputfile.close() #close output file

print(datetime.datetime.now()) #print timestamp