import matplotlib.pyplot as plt

import random
     
def main():
    

    random.seed(4567)        

# For the exmaple in class, but  not the programming assignment
    #values=[1,2,3,5,7,11,13,17,19,23]
    #weights=[2,4,6,8,10,2,4,6,8,10]
    #data=random.choices(values,weights=weights,k=100000)
    data = []
    data2 = []
    data3 = []
    data4 = []

    random.seed(4567)
    for i in range(1000):
     data.append(random.uniform(0,100))

    random.seed(34567)
    for i in range(1000):
     data2.append(random.normalvariate(50,10))

    random.seed(98765)
    for i in range(1000):
     data3.append(random.expovariate(1/50))

    random.seed(65432)
    for i in range(1000):
     data4.append(random.betavariate(0.5,0.5))

#first 
      write_file = "random.csv"
      with open(write_file, "w") as output:
        for line in builtUpHeader:
            output.write(" ".join(line))

      with open(write_file, "a") as output:
            output.writelines("\n")

#second

          write_file = "normal.csv"
      with open(write_file, "w") as output:
        for line in builtUpHeader:
            output.write(" ".join(line))

      with open(write_file, "a") as output:
            output.writelines("\n")

#third
      write_file = "expo.csv"
      with open(write_file, "w") as output:
        for line in builtUpHeader:
            output.write(" ".join(line))

      with open(write_file, "a") as output:
            output.writelines("\n")

#fourth

      write_file = "beta.csv"
      with open(write_file, "w") as output:
        for line in builtUpHeader:
            output.write(" ".join(line))

      with open(write_file, "a") as output:
            output.writelines("\n")


    maxY=max(data)
    plt.figure(figsize=(8,8))
    plt.subplot(2,1,1)
    plt.plot(data,'ro')
    plt.axis([0,250,0.0,maxY])
    plt.title('Random Distribution')

    numBins=100
    plt.subplot(2,1,2)
    plt.hist(data,numBins)
    plt.title('Histogram of Random Distribution')
    plt.savefig('random.png')

    maxY=max(data2)
    plt.figure(figsize=(8,8))
    plt.subplot(2,1,1)
    plt.plot(data2,'ro')
    plt.axis([0,250,0.0,maxY])
    plt.title('Uniform Distrobution')

    numBins=100
    plt.subplot(2,1,2)
    plt.hist(data,numBins)
    plt.title('Histogram of Uniform Distribution')
    plt.savefig('normal.png')
         

     
if __name__ == "__main__":
   main()            



