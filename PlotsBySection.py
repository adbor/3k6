#import codecs
import sys
import matplotlib.pyplot as plt
import math

def usage():
  print("Utility read cashin strings and calculate some statistic for each section")
  print("Usage: sectionStat.py <cashin file>") #only cashin strings should be in file


#rooms from 400 - 420 are used for shops
last_room_in_section = [20,60,100,120,156,196,236,276,316,356,384,420]

if len(sys.argv) < 2:
  usage()
  exit ()  

f = open(sys.argv[1], "r")#, encoding="utf-8") 
rooms_payed = [0]*len(last_room_in_section)
sum_payed = [0]*len(last_room_in_section)
room_set = set()
payment_counts = 0

cashin_set  = set()
cashin1_set = set()
cashin5_set = set()

for line in f:
  ff = line.split(',')
  room = int(ff[1])
  cash = int(ff[2])
  payment_counts += 1
#  print(room, cash)
  for i in  range(len(last_room_in_section)):
    section = i+1
    if room < last_room_in_section[i] :
      break
  if room not in room_set:
    rooms_payed[section - 1] = rooms_payed[section -1] + 1

  room_set.add(room)

  if ff[0]   == "cashin":
    cashin_set.add(room)    
  elif ff[0] == "cashin1":
    cashin1_set.add(room)    
  elif ff[0] == "cashin5":
    cashin5_set.add(room)    

  sum_payed[section - 1] = sum_payed[section - 1] + cash

sections = [1,2,3,4,5,6,7,8,9,10,11,12]

print("Payment counts:", payment_counts)
print("Different flats:", len(room_set))
print(rooms_payed)  
print(sum_payed)  

print("cashin(A)=",      len(cashin_set),                   "cashin5(B)=", len(cashin5_set))
print("A | B=",          len(cashin_set.union(cashin5_set)),"A & B=",      len(cashin_set.intersection(cashin5_set)))
print("A - B=",          len(cashin_set - cashin5_set),     "B - A=",      len(cashin5_set - cashin_set))

plt.title('Количество сдавших')
plt.bar(sections, rooms_payed)
plt.show()

plt.title('Сумма')
plt.bar(sections, sum_payed)
plt.show()
