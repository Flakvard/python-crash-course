"""
Monte Carlo Simlulation n sample
Random sample of 30 from total population 100.000 
96.09% confidence that the sample population in average is -2% below total population. Min -7% og Max 3%

Random sample of 10 from total population 100.000 
70.51% confidence that the sample population in average is -3,0% below total population. Min -9% og Max 3%
81.20% confidence that the sample population in average is -5,5% below total population. Min -14% og Max 3%
90.34% confidence that the sample population in average is -9,5% below total population. Min -22% og Max 3%
95.17% confidence that the sample population in average is -14% below total population. Min -30% og Max 3%

Random sample of 7 from total population 100.000 
71.11% confidence that the sample population in average is -6,0% below total population. Min -16% og Max 3%
80.64% confidence that the sample population in average is -10.0% below total population. Min -25% og Max 3%
90.42% confidence that the sample population in average is -16.0% below total population. Min -39% og Max 3%
95,11% confidence that the sample population in average is -23.0% below total population. Min -49% og Max 3%

Random sample of 5 from total population 100.000 
70,97% confidence that the sample population in average is -10.1% below total population. Min -25% og Max 3%
80,70% confidence that the sample population in average is -15.6% below total population. Min -35% og Max 3%
90.11% confidence that the sample population in average is -25.2% below total population. Min -52% og Max 3%
95.02% confidence that the sample population in average is -36.5% below total population. Min -82% og Max 3%

Monte Carlo Simlulation n sample
rate >= -0.01 and rate <= 0.01
3.55% confidence that the sample population is within 1% from total population with 30 samples
20.44% confidence that the sample population is within 1% from total population with 72 samples
40.92% confidence that the sample population is within 1% from total population with 100 samples
50.51% confidence that the sample population is within 1% from total population with 111 samples
70.09% confidence that the sample population is within 1% from total population with 133 samples
95.69% confidence that the sample population is within 1% from total population with 162 samples

"""
import numpy as np

rndNums = 10000
def mainLoop(rand_num):
    for i in range(200):
        slice_of_rand_num = rand_num[:i+1]  
        maxNum = max(slice_of_rand_num)
        k = i+1
        totalPopulation = (maxNum-1+maxNum/k)
        rate = 1-(rndNums/totalPopulation)
        if rate >= -0.01 and rate <= 0.01:
            yield k, rate
            
def nLoop(rand_num, nLoop):
        slice_of_rand_num = rand_num[:nLoop]  
        maxNum = max(slice_of_rand_num)
        k = 30
        totalPopulation = (maxNum-1+maxNum/k)
        rate = 1-(rndNums/totalPopulation)
        return rate
            
def maxTest(rand_num, totalMCS):
    val = mainLoop(rand_num)
    for k, rate in val:
        totalMCS[str(k)] = totalMCS.get(str(k), 0) + 1
        #print("Number: ",k," ", f'{rate:0.2f}')
    
def printTotalMCS(totalMCS):
    for x,y in totalMCS.items():
        print(x," ",y)
        
def n30dict(totalMCS,rand_num):
    rate = nLoop(rand_num,10)
    rounded_rate  = round(rate * 100) / 100  # Round to the nearest tenth
    totalMCS[str(rounded_rate)] = totalMCS.get(str(rounded_rate),0)+1
        

print("----")
#rangeList = list(range(1,101)) 
#totalMCS = dict(rangeList=0)
totalMCS = dict()
print(totalMCS)
print("----")

for i in range(100000):
    # Generate an array of 1000 random numbers between 1 and 100
    rand_num = np.random.randint(1, rndNums+1, size=200)
    #print(rand_num)
    #n30dict(totalMCS,rand_num)
    maxTest(rand_num,totalMCS)
print("----")
printTotalMCS(totalMCS)  
print("----")

