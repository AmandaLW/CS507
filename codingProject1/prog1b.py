#!/usr/bin/env python3
#
import argparse
import os,sys

totalFP = 0
totalTP = 0
totalFN = 0
totalFunc = 0
precision = 0
recall = 0
f1 =0

def main():

   formatter = argparse.ArgumentDefaultsHelpFormatter
   parser = argparse.ArgumentParser(description='CS 507 csv reader',
                                    formatter_class=formatter)

   required = parser.add_argument_group(title='required')
   required.add_argument('file1',  type=str, help='data file to read')
   required.add_argument('file2',  type=str, help='data file to read')
   
   args = parser.parse_args()
   fileName=args.file1
   fileName2=args.file2
   fullFileName=os.path.abspath(fileName)
   fullFileName2=os.path.abspath(fileName2)
   print1(fileName,processFile(fullFileName))
   processFile(fullFileName2)  



def processFile(fileName):

   totalFP = 0
   totalTP = 0
   totalFN = 0
   totalFunc = 0
   precision = 0
   recall = 0
   f1 =0

   with open(fileName,'r') as fn:
      headers=fn.readline().strip().split(',')
      #Sprint('Headers = {!s}'.format(headers))
      lineCnt=0
      #hold =[]
      for line in fn:
         lineCnt+=1
         line = line.strip()  # to remove extra white space
         words = line.split(',')
         #print('{:4d}: {!s}'.format(lineCnt,words))

         #find and tally up the FP
         FPnumber = int(words[1])
         totalFP = totalFP + FPnumber
         
         #find and tally up TP
         TPnumber = int(words[2])
         totalTP = totalTP + TPnumber

         #find and tally up total FN
         FNnumber = int(words[3])
         totalFN = totalFN + FNnumber

         #find and tally up all func
         FuncNumber = int(words[4])
         totalFunc = totalFunc + FuncNumber

   precision = totalTP / (totalTP + totalFP)
   recall = totalTP/(totalTP + totalFN)
   f1 = (precision * recall) / ((1/2) * (precision + recall))

   #print("For file: ", fileName)
   #print("Total FP: ", totalFP)
   #print("Total TP: ", totalTP)
   #print("Total FN: ", totalFN)
   #print("Total func: ", totalFunc, "\n")

   print("Precision: ", round(precision,2))
   print("Recall: ", round(recall,2))
   print("F1: ", round(f1,2))

   return fileName, totalFP, totalTP, totalFN, totalFunc
         
         
def print1(fileName, function):
    print("For file: ", fileName)
    print("Total FP: ", totalFP)
    print("Total TP: ", totalTP)
    print("Total FN: ", totalFN)
    print("Total func: ", totalFunc, "\n")



         
    
if __name__ == "__main__":
    main()
