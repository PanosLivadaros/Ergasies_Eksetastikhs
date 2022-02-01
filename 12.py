from urllib.request import Request, urlopen
import json
from time import sleep

def max_consecutive(input_str, w):
    return max(map(len, input_str.split(w)))

rand_list = []
print("Calculating...")
# In the code below, I opted to not use the "https://drand.cloudflare.com/public/{round}" method indicated in instructions, in order to save up on lines of code, computing resources and program execution time.
for i in range(100):      # to test you can change the range to a smaller number, e.g. 2
    req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = json.loads(urlopen(req).read().decode())
    rand_list.append(data["randomness"])
    sleep(30)
for i in range(len(rand_list)):
    rand_list[i] = bin(int.from_bytes(rand_list[i].encode(), "big")).strip("0b")
print(rand_list)
max0 = -1
max1 = -1
for i in range(len(rand_list)):
    z = max_consecutive(rand_list[i], "1")
    y = max_consecutive(rand_list[i], "0")
    if max0 < z:
        max0 = z
    if max1 < y:
        max1 = y
print("The longest consecutive row of 0's is of length:", max0, "and the longest consecutive row of 1's is of length:", max1, ".")
