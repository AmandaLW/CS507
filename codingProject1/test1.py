#!/usr/bin/env python3
#
import argparse
import os,sys


def main():

   formatter = argparse.ArgumentDefaultsHelpFormatter
   parser = argparse.ArgumentParser(description='CS 507 csv reader',
                                    formatter_class=formatter)

   required = parser.add_argument_group(title='required')
   required.add_argument('file1', type=str,
                         help='data file to read')

   args = parser.parse_args()
   fileName=args.file1
   fullFileName=os.path.abspath(fileName)
   processFile(fullFileName)   

def processFile(fileName):

   with open(fileName,'r') as fn:
      headers=fn.readline().strip().split(',')
      print('Headers = {!s}'.format(headers))
      lineCnt=0
      for line in fn:
         lineCnt+=1
         line = line.strip()  # to remove extra white space
         words = line.split(',')
         print('{:4d}: {!s}'.format(lineCnt,words))
         
    
if __name__ == "__main__":
    main()
