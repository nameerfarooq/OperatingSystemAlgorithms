NumOfProcess = int(input("enter number of processes to be calculated", ))

listofprocess = []
CpuTime = 0
for i in range(NumOfProcess):
    print("enter ", i+1," process details !")
    processName = input("enter process Name")
    BurstTime = int(input("enter  process Burst time"))
    ArrivalTime = int(input("enter  process Arrival time"))
    print("-------------------------------------")
    process = [processName, BurstTime, ArrivalTime]
    listofprocess.append(process)
#sorting
for j in reversed(range(NumOfProcess-1)):
    if listofprocess[j][1] != listofprocess[j-1][1]:
        if listofprocess[j][1]>listofprocess[j-1][1]:
            temp = listofprocess[j]
            listofprocess[j] = listofprocess[j-1]
            listofprocess[j-1] = temp
    else:
        if listofprocess[j][2]>listofprocess[j-1][2]:
            temp = listofprocess[j]
            listofprocess[j] = listofprocess[j-1]
            listofprocess[j-1] = temp
print(listofprocess)
#calculating waiting times
for k in listofprocess:
    waitingtime = CpuTime
    k.append(waitingtime)
    CpuTime = CpuTime + k[1]
    completiontime = CpuTime
    k.append(completiontime)
    turnAroundTime = completiontime - k[2] 
    k.append(turnAroundTime)
print(listofprocess)
# pname, bt, at, wt, ct, tat

totalWaitingtime = 0
for l in range(3):
    totalWaitingtime = totalWaitingtime + listofprocess[l][3]
AvgWaitingtime = totalWaitingtime//NumOfProcess
print("AvgWaitingtime ",AvgWaitingtime)

totalTAT = 0
for l in range(3):
    totalTAT = totalTAT + listofprocess[l][5]
AvgTAT = totalTAT//NumOfProcess
print("AvgTAT ",AvgTAT)
