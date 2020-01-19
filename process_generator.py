import numpy as np
# Process generator
"""
Process Generator Module [30% of the Grade]
Each process has a set of parameters. Each parameter is generated randomly following a certain distribution as
indicated:
1. Arrival Time : follows Normaldistribution
2. Burst Time : follows Normaldistribution
3. Priority : follows Poissondistribution

Input:is a text file organized as follows:
 First lineshould include the number of processes.
 Second line should include μ and σ of arrival time distribution separated by a whitespace.
 Third line should include μ and σ of burst time distribution separated by a whitespace.
 Fourth line should include λ of prioritydistribution

"""
input_path = input("Enter File Path/Name : ")
file = open(input_path, "r")
data = []
for line in file:
    endl = line.find('\n')
    if endl != -1 :
        line = line[:endl]
    data.append(line)
file.close()
pnum = data[0]
mu_ariv , sig_ariv = data[1].split(' ')
mu_run , sig_run = data[2].split(' ')
lmda = data[3]
pnum = int(pnum)
mu_ariv , sig_ariv = float(mu_ariv) , float(sig_ariv)
mu_run , sig_run = float(mu_run ) , float(sig_run)
lmda = float(lmda)

"""
Output:is a text file organized as follows:
 First line should include the number ofprocesses.
 Each line contains the parameters for one process only, separated by a white space, in the following order:
process number, arrival time, burst time andpriority.
"""

arrival_time = np.random.normal(mu_ariv, sig_ariv, pnum)
run_time = np.random.normal(mu_run,sig_run, pnum)
priority = np.random.poisson(lmda, pnum)
file = open('output.txt', "w")
for i in range (pnum):
    file.write(str(i+1)+" "+str(arrival_time[i])+" "+str(run_time[i])+" "+str(priority[i])+'\n')
file.close()