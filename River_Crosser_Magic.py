#Approach Assumption
'''
1. Assuming that the person  always leaps  a Leap Size  only
2. Assuming if the peg size is more than Leap size , then he will
do the next leap depending on the remaining size of Total Leap
and the Leap Size
3. The person will wait for another Peg even though it's covering the
X to Y distance
Pegs = [10,3,1,9,7,5,8]
Assume the first Peg was 10 and total was 10
Then 0 second 4
then 1 second another 4 depending on the next peg Size
in the default  case 3rd Second peg of  9 is what we wait

then 4 second remaining 2 , but he makes a leap of 4 always
so make 2 pegs more to reach the other Side Y

'''
# getting the sum of pegs
# removing the pegs which already used

def bestLeapTime(totsize,leapsize,pegs):
    i = 1
    tillnow = 0
    newIndex = 0
    while totsize > 0:
        idxSum = max(pegs[newIndex:i])
        if idxSum >= leapsize and idxSum > tillnow:
            nextleap = idxSum - tillnow
           # print(nextleap)
            if nextleap >= leapsize:
                totsize = totsize - leapsize
                tillnow = tillnow + leapsize
                print("Next Hop->", leapsize)

            else:
                totsize = totsize - nextleap
                tillnow = tillnow + nextleap
                print("Next Hop->", nextleap)
        if totsize > leapsize:
            i += 1
            try:
                newPeg = max(pegs[:i])
                if newPeg > idxSum:
                    newIndex = i - 1
                   # for x in range(0, i-1):
                       # pegs.pop(x)
            except:
                print("Out of range")

        else:
            i += 1
            print("Last Hop->", leapsize)
            totsize = totsize - leapsize

    return i

print("Welcome to the river crosser Guide")
print('Enter the Distance between 2 points X and Y')
Tot_dist = int(input())
print(Tot_dist)

print('Enter the Max Leap Size of the crossing')

Max_leap = int(input())
print(Max_leap)


print("\n Enter the pegs input with space")
No_of_pegs = [int(x) for x in input().split()]
print("Peg sizes are -->")
print(No_of_pegs)

cutoffpeg = Tot_dist - Max_leap
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
    print("Crossing  not possible as right size  of peg not present")
else:
    timex = bestLeapTime(Tot_dist,Max_leap,No_of_pegs)
    print("The best possible time required would  -->")
    print(timex)

