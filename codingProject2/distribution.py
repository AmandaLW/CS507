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

    for i in range(1000):
     data.append(random.uniform(0,100))

    for i in range(1000):
     data2.append(random.normalvariate(50,10))

    for i in range(1000):
     data3.append(random.expovariate(1/50))

    for i in range(1000):
     data4.append(random.betavariate(0.5,0.5))



    maxY=max(data4)
    plt.figure(figsize=(8,8))
    plt.subplot(2,1,1)
    plt.plot(data4,'ro')
    plt.axis([0,250,0.0,maxY])
    plt.title('Random Numbers')

    numBins=100
    plt.subplot(2,1,2)
    plt.hist(data4,numBins)
    plt.title('Histogram of Random Numbers')
    plt.show()
         

     
if __name__ == "__main__":
   main()            



