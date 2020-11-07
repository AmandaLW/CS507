#!/usr/bin/env python3
#
import argparse
import os,sys

totalFP = 0
totalTP = 0
totalFN  = 0
totalFunc = 0
precision = 0
recall = 0
f1  = 0

def main():

   formatter = argparse.ArgumentDefaultsHelpFormatter
   parser = argparse.ArgumentParser(description='CS 507 csv reader',
                                    formatter_class=formatter)

   required = parser.add_argument_group(title='required')
   required.add_argument('file1',  type=str, help='data file to read')
   
   
   args = parser.parse_args()
   fileName=args.file1
   

   fullFileName=os.path.abspath(fileName)
   

   precision1, recall1, f11 = processFile(fullFileName)
   

   #precisionAv = (precision1 + precision2)/2
   #recallAv = (precision1 + precision2) /2
   #f1Av = (f11 + f12)/2

   #printAv(precisionAv, recallAv, f1Av)
   
   



def processFile(fileName):
   totalFP = 0
   totalTP = 0
   totalFN  = 0
   totalFunc = 0
   precision = 0
   recall = 0
   f1  = 0

   with open(fileName,'r') as fn:
      headers=fn.readline().strip().split(',')
      print('Headers = {!s}'.format(headers))
      headers.append('Prec')
      headers.append('Recall')
      headers.append("F1")
      print('Headers = {!s}'.format(headers))
      

      lineCnt=0
      for line in fn:
         lineCnt+=1
         line = line.strip()  # to remove extra white space
         words = line.split(',')
         #print('{:4d}: {!s}'.format(lineCnt,words))

         #find and tally up the FP
         FPnumber = int(words[1])
         
         
         #find and tally up TP
         TPnumber = int(words[2])
         

         #find and tally up total FN
         FNnumber = int(words[3])
         

         #find and tally up all func
         FuncNumber = int(words[4])
         

   #print("For file: ", fileName)
   #print("Total FP: ", totalFP)
   #print("Total TP: ", totalTP)
   #print("Total FN: ", totalFN)
   #print("Total func: ", totalFunc, "\n")

         precision = TPnumber / (TPnumber + FPnumber)
         recall = TPnumber/(TPnumber + FNnumber)
         f1 = (precision * recall) / ((1/2) * (precision + recall))

         precisionRounded = round(precision,2)
         recallRounded = round(recall,2)
         f1Rounded = round(f1,2)

         #print("Precision: ", precisionRounded)
         #print("Recall: ", recallRounded)
         #print("F1: ", f1Rounded)

   return precisionRounded, recallRounded, f1Rounded

def printAv(precision, recall, f1):
    print("Avg Precision: ", precision)
    print("Avg Recall: ", recall)
    print("Avg F1: ", f1)


         
         




         
    
if __name__ == "__main__":
    main()
