#!/usr/bin/python3
# @null-talisman

import random

def main():
   x = random.randint(1,5)
   if x == 1:
       with open('meteor_pics/geminids.jpg', 'rb') as f:
      print("\t\tOrionids\n\tPeak night: October 20-21, 2020")
   elif x == 2:
       print("\t\tNorthern Taurids\n\tPeak night: November 11-12, 2020")

   print(x)


if __name__ == "__main__":
   main()


