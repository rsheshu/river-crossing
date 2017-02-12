__author__ = 'cheetah'
import pandas as pd
from pandas import ExcelWriter

# Approach for the Problem
'''
1. The person  can leaps  max up to the Leap Size  only
i..e cap = 4 , person can make leaps of 1,2,3,4

2. Assuming if the peg size is more than Leap size , then he will
do the next leap depending on the remaining size of Total Leap
and the Leap Size
i..e cap = 4 , peg size = 10 person can make leaps of 4 ,4 ,2
the last leap of 2 will depend on the peg appeared on that second

3. The person will wait for another Peg even though it's covering the
X to Y distance

Pegs = [10,3,1,9,7,5,8]
Assume the first Peg was 10 and total was 10
Then 1 second leap size 4
then 2 second another 4 depending on the next peg size is 3
as compared to earlier peg size 10 <= total

In 3rd second another peg size of 1 emerges ,but it's of no use and since the remaining is 2
it will make a leap and reach at Y

'''

# getting the sum of pegs
# removing the pegs which already used

def bestLeapTime(totsize,leapsize,pegs):
    i = 1
    tillnow = 0
    newIndex = 0
    while totsize > 0:
        idxSum = max(pegs[newIndex:i]) # find the max till the latest pegs
        if idxSum >= leapsize and idxSum > tillnow: #check with latest peg  and covered till now
            nextleap = idxSum - tillnow
                # print(nextleap)
            if nextleap >= leapsize:            #Case for leap with max leap
                totsize = totsize - leapsize
                tillnow = tillnow + leapsize
                print("Next Hop->", leapsize)

            else:                               #Case for leap with less leap size
                totsize = totsize - nextleap
                tillnow = tillnow + nextleap
                print("Next Hop->", nextleap)
        else:
            print("Next Hop -> Wait for Peg")
        if totsize > leapsize:
            i += 1
            try:
                newPeg = max(pegs[:i])  # find the max next to the latest pegs
                if newPeg > idxSum:
                    newIndex = i - 1
            except:
                print("Out of range")

        else:
            i += 1

            if totsize < leapsize:
                print("Last Hop->", totsize)
            else:
                print("Last Hop->", leapsize)

            totsize = totsize - leapsize

    return i

'''
The below functions validates the Case of the inputs given
1. cutoffpeg: The remaining distance from the cap size
cap = 3
tot = 9
[2,1,4,6,8,3] in the pegs basket.

cutoffpeg = 9-3 = 6 ,there has to be one peg which
is of the cutoffpeg  else cross of the river is not possible
assume cap = 8 , tot = 8
if cutoffpeg  = 0 , which means  the person can make a leap in
max leap size and go to Y from X

'''

def checkPegsValidity(Tot_dist, Max_leap, No_of_pegs):

    cutoffpeg = Tot_dist - Max_leap
    if cutoffpeg == 0:  #'Case where crossing is done in 1 leap'
        return 1
    cutofflist = [peg for peg in No_of_pegs if peg >= cutoffpeg]

    ''' There must be least no  pegs to pave the path for the
    other end i..e Y from X.
    for 15 totsize
    leap size 5
    15 - 5 = 10
    atleast more than 1 entry of 10 should be there

    Works on the input Totsize 10
    max leap = 4
    pegs = [2,4,1,9,7,5,8]

       '''
    lastLeap = cutofflist
    if len(cutofflist) < 1:
        #print("Crossing  not possible as right size  of peg not present")
        return "Not able to cross"

    else:
        timer = bestLeapTime(Tot_dist, Max_leap, No_of_pegs)
        #print("The best possible time required would  -->")
        #print(timex)
        return timer
'''
This function converts the line of strings into integer
from the input file
'''
def makepegs(peglist):
    newlist = list()
    for vals in peglist:
        print vals
        newlist.append(int(str(vals)))
    return newlist

print("Welcome to the river crosser Guide")
readlines = pd.read_csv("test.csv")
type(readlines)
totalcases = readlines.shape[0]  # pandas shape function
val = list()
for cases in range(0,totalcases):
   totdist = readlines.iloc[cases][1]  #get the Total distance
   maxleap = readlines.iloc[cases][2]  #get the max leap
   print "printing raw pegs"
   peglist = readlines.iloc[cases][3]  # get the pegs list
   listofpegs = list(peglist.split(','))
   print listofpegs
   noofpegs = makepegs(listofpegs)      # Make proper integer list
   print noofpegs
   timex = checkPegsValidity(totdist, maxleap, noofpegs) # check and follow the algorithm
   val.append(timex)

readlines['Time-taken(Secs)'] = val  # Add the new list of output in the data frame
writer = ExcelWriter('output.xlsx')  # make the output list
readlines.to_excel(writer, 'Sheet1') #
writer.save()

