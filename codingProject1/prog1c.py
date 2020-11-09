#!/usr/bin/env python3
#
import argparse
import os,sys

#Dictionaries for storing each of the files being read in 
file1dic = {}
file2dic = {}

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
   avgPrecision, avgRecall, avgF1, totalLines = processFile(fullFileName, 1)
   processFile(fullFileName2, 2)
   printAv(avgPrecision, avgRecall, avgF1, totalLines)

   for x, y in file1dic.items():
       print(x,y)

   file1MinusFile2()
   

#fileName takes the name of the file and "file" tells it what file/dictonary to fill
def processFile(fileName, file):
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
      
      newHeader = "name " + ",Prec " +",Recall ", ",F1"
      
      #print('Headers = {!s}'.format(headers))

      write_file = "compare.csv"
      with open(write_file, "w") as output:
        for line in newHeader:
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
         
         if file == 1:
            file1dic[words[0]] = {'FP': words[1], 'TP': words[2], 'FN': words[3], "Total": words[4], "Prec": str(precisionRounded), "Recall": (recallRounded), "F1": (f1Rounded)}
         if file == 2:
            file2dic[words[0]] = {'FP': words[1], 'TP': words[2], 'FN': words[3], "Total": words[4], "Prec": str(precisionRounded), "Recall": (recallRounded), "F1": (f1Rounded)}

         thicciBoiLine = words[0] +","+words[1]+","+words[2]+","+words[3]+","+words[4]+","+str(precisionRounded)+","+str(recallRounded)+","+str(f1Rounded)
       
         with open(write_file, "a") as output:
            for line in thicciBoiLine:
                output.write(" ".join(line))
         with open(write_file, "a") as output:
                output.writelines("\n")  

      #for x, y in file1dic.items():
        #print(x,y)      

   return avgPrecision, avgRecall, avgF1, totalLines

def printAv(avgPrecision, avgRecall, avgF1, totalLines):
    precision = avgPrecision/totalLines
    recall = avgRecall/totalLines
    f1 = avgF1/totalLines
    print("Avg Precision: ", round(precision,2))
    print("Avg Recall: ", round(recall,2))
    print("Avg F1: ", round( f1,2))

def file1MinusFile2():
    precMinusPrec = 0
    recallMinusRecall = 0
    F1MinusF1 = 0

    for key in file1dic.keys():
        if key in file2dic:
            
            print(key)


      
    
if __name__ == "__main__":
    
    main()
