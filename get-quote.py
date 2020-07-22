import random 
def primary():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, 6)
  rnd2 = random.randint(7, last)
  print(quotes[rnd],quotes[rnd2])
  #print(quotes[rnd2])

if __name__== "__main__":
  primary()
