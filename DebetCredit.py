#import codecs
import sys
import codecs
import re

def usage():
  print("Utility that calculate income outcome based on cashin/cashout strings")
  print("Usage: debetcredit.py <_chat.txt>")
  print("       _chat.txt - exported chat from whatsap(unzipped)\n")
  print("       Result will be in _chat.txt.money")


if len(sys.argv) < 2:
  usage()
  exit ()  

cashin_search  = re.compile(".*cashin,")  #cashin,  strings
cashin_search1 = re.compile(".*cashin.,") #cashinX, strings X - any number
sender_search  = re.compile(".*Борискин Лёшенька:")
cashout_search = re.compile(".*cashout.,")
cashout_search1= re.compile(".*cashout,")

#incorrectly outputted into chat string
exceptions=["cashin1,3500,возмещение половины расходов на юриста со стороны 3.2",
           "cashin,1200,213"]

#[10.12.2018, 12:28:35] Борискин Лёшенька: На счету осталось 77665 руб
add = 77665 + 3500 + 1200 #77665 - изначальная сумма на счете
                          #3500 и 1200 - суммы не правильно указанные в чате

income   = add
outcome  = 0

f  = codecs.open(sys.argv[1],              encoding='utf-8')
f2 = codecs.open(sys.argv[1]+'.money',  "w"  ,encoding='utf-8') 
for line in f:
  isCashin  = bool(cashin_search.match(line))  or bool(cashin_search1.match(line))
  isCashout = bool(cashout_search.match(line)) or bool(cashout_search1.match(line))

  doskip = False
  for exp in exceptions:
    if line.find(exp) != -1:
      doskip = True
  if doskip:
    continue

  doprocess = (isCashout or isCashin) and bool(sender_search.match(line))
  if False == doprocess :
    continue
  start = line.rfind(':')
  if start < 0:
    continue
  tmp = line[start+2:]
  f2.write(tmp)


  tmplist = tmp.split(',')
  if isCashin:
    income += int(tmplist[2])
  if isCashout:  
    outcome += int(tmplist[1])
    
print("Income=", income, "Outcome=",outcome, "Balance=",income-outcome)

