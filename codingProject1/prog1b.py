#!/usr/bin/env python3
#
import argparse
import os,sys

outputFileName = "parsedName"

def main():
   global outputFileName
   formatter = argparse.ArgumentDefaultsHelpFormatter
   parser = argparse.ArgumentParser(description='CS 507 csv reader',
                                    formatter_class=formatter)

   required = parser.add_argument_group(title='required')
   required.add_argument('file1',  type=str, help='data file to read')
   args = parser.parse_args()
   fileName=args.file1
   fullFileName=os.path.abspath(fileName)
   fileNameSplit = fileName.split(".")
   outputFileName = fileNameSplit[0]
   print(outputFileName)
   avgPrecision, avgRecall, avgF1, totalLines = processFile(fullFileName)
   printAv(avgPrecision, avgRecall, avgF1, totalLines)

   

def processFile(fileName):
   totalFP = 0
   totalTP = 0
   totalFN  = 0
   totalFunc = 0
   precision = 0
   recall = 0
   f1  = 0
   avgPrecision = 0
   avgRecall = 0
   avgF1 = 0
   totalLines = 0

   with open(fileName,'r') as fn:
      #headers=fn.readline().strip().split(',')
      headers=fn.readline().strip()
      
      
      addPrec = headers + ",Prec"
      addRecall = addPrec + ",Recall"
      builtUpHeader = addRecall + ",F1"
      
      #print('Headers = {!s}'.format(headers))

      write_file = outputFileName + "new.csv"
      with open(write_file, "w") as output:
        for line in builtUpHeader:
            output.write(" ".join(line))

      with open(write_file, "a") as output:
            output.writelines("\n")
    

      lineCnt=0
      for line in fn:
         lineCnt+=1
         line = line.strip()  # to remove extra white space
         words = line.split(',')
         #print('{:4d}: {!s}'.format(lineCnt,words))\

         name =words[0]

         #find and tally up the FP
         FPnumber = int(words[1])
         
         #find and tally up TP
         TPnumber = int(words[2])
         
         #find and tally up total FN
         FNnumber = int(words[3])
         
         #find and tally up all func
         FuncNumber = int(words[4])
         
         precision = TPnumber / (TPnumber + FPnumber)
         recall = TPnumber/(TPnumber + FNnumber)
         f1 = (precision * recall) / ((1/2) * (precision + recall))

         precisionRounded = round(precision,4)
         recallRounded = round(recall,4)
         f1Rounded = round(f1,4)

         avgPrecision = avgPrecision + precisionRounded
         avgRecall = avgRecall + recallRounded
         avgF1 = avgF1 + f1Rounded
         totalLines = lineCnt -1

         thicciBoiLine = words[0] +","+words[1]+","+words[2]+","+words[3]+","+words[4]+","+str(precisionRounded)+","+str(recallRounded)+","+str(f1Rounded)
       
         with open(write_file, "a") as output:
            for line in thicciBoiLine:
                output.write(" ".join(line))
         with open(write_file, "a") as output:
                output.writelines("\n")        

   return avgPrecision, avgRecall, avgF1, totalLines

def printAv(avgPrecision, avgRecall, avgF1, totalLines):
    precision = avgPrecision/totalLines
    recall = avgRecall/totalLines
    f1 = avgF1/totalLines
    print("Avg Precision: ", round(precision,2))
    print("Avg Recall: ", round(recall,2))
    print("Avg F1: ", round( f1,2))
      
    
if __name__ == "__main__":
    
    main()
