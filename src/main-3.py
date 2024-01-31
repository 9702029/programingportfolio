import random
import string
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.GREEN+"Welcome to the Random Word Genorator")
word=int(input(Fore.GREEN+"how many words do you want to generate?    "))
# create a list of 20 prefixes
prefixes = ["anti", "de", "dis", "fore", "fore", "inter", "mid","dict" , "pre" , "sub",]
# create a list of 20 suffixes
suffixes = ["able", "ed", "en", "er", "or", "emesis", "emia", "ic", "hexia", "fida", "lucent"]
# create a list with 20 word roots
roots = ["spect", "ambi", "aqua", "cent", "fac", "rupt", "struct", "voc", "bene", "fort"
,"fort"]
#create a definition for the 20 prefixes
PreDef = ["to be against","to remove","to be apart","before","between","the middle of","to say","before","under"]

#create a definition for the 20 suffixes
SufDef = ["capable of","in the past","within","one who","vometing","a blood condition","pertaining to","habit of","to split","to shine"]

#create a definition for the 20 roots
RootDef = ["spectats","death","water","center","made","break","build","voice",
"good","strength"]
for i in range(word):
  random_index_suff = random.randint(0, len(suffixes) - 1)
  random_index_pre = random.randint(0, len(prefixes) - 1)
  random_index_root = random.randint(0, len(roots) - 1)
  print(Fore.RED+prefixes[random_index_pre] + roots[random_index_root] + suffixes[random_index_suff])
  print("Definition: ", SufDef[random_index_suff], RootDef[random_index_root], PreDef[random_index_pre])
