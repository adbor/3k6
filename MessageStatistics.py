import codecs
import sys

def usage():
  print("Utility calculate message statistic from whatsapp chat")
  print("Usage: MessageStatistics.py <_chat.txt>")
  print("       _chat.txt - exported chat from whatsap(unzipped)\n")
  print("       Result will be in _chat.txt.sta")


if len(sys.argv) < 2:
  usage()
  exit ()  

f  = codecs.open(sys.argv[1],    encoding='utf-8')
f2 = open(sys.argv[1]+".sta"  , "w", encoding="utf-8") 

my_map = {}
for line in f:
    start = line.find(']')
    end   = line.find(':', start)
    if start < 0 or end <0:
      continue

    name=line[start+2:end]
    my_map[name] = my_map.get(name, 0) + 1    


s = sorted(my_map.items(), key=lambda x: x[1], reverse=True)
for k, v in s:
  f2.write(str(k))
  f2.write(' ')
  f2.write(str(v))
  f2.write('\n')
