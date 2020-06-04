# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:37:43 2020

@author: Biani Masita
"""

# Siapin Data Input dulu
X_coordinate = [15,	76,	96,	8,	54,	85,	74,	63,	71,	93,	57]
Y_coordinate = [88,	57,	62,	63,	22,	33,	62,	54,	86, 79,	58]

import numpy as np
import pandas as pd

Distance_table = np.zeros((11, 11))
list_incident = list(range(11))

for index1 in list_incident:
    for index2 in list_incident:
        Distance_table[index1, index2] = ((X_coordinate[index1] - X_coordinate[index2])**2 + (Y_coordinate[index1] - Y_coordinate[index2])**2) ** 0.5

#Input Data 2: Process Time
ProcessTimeFile = 'Data Input 10 Unit 10 Incidents.xlsx'
ProcessTime = pd.read_excel(ProcessTimeFile, delimiter = ';', sheet_name = 'Process Time untuk Solve')
ProcessTimeArray = np.array(ProcessTime)
				
#Input Data 3: Rescue Units Speed, Travel Time Matrix, Incidents Severity
RescueUnits_Speed = np.array([[15],
                [15],
				[10],
				[12],
				[9],
				[15],
				[12],
				[11],
				[16],
				[12]], dtype = float)
Travel_Time_Unit1 = np.zeros((11,11))
Travel_Time_Unit2 = np.zeros((11,11))
Travel_Time_Unit3 = np.zeros((11,11))
Travel_Time_Unit4 = np.zeros((11,11))
Travel_Time_Unit5 = np.zeros((11,11))
Travel_Time_Unit6 = np.zeros((11,11))
Travel_Time_Unit7 = np.zeros((11,11))
Travel_Time_Unit8 = np.zeros((11,11))
Travel_Time_Unit9 = np.zeros((11,11))
Travel_Time_Unit10 = np.zeros((11,11))

for index1 in range(11):
    for index2 in range(11): 
        Travel_Time_Unit1[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[0,0]
        Travel_Time_Unit2[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[1,0]
        Travel_Time_Unit3[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[2,0]
        Travel_Time_Unit4[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[3,0]
        Travel_Time_Unit5[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[4,0]
        Travel_Time_Unit6[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[5,0]
        Travel_Time_Unit7[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[6,0]
        Travel_Time_Unit8[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[7,0]
        Travel_Time_Unit9[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[8,0]
        Travel_Time_Unit10[index1,index2] = Distance_table[index1,index2]/RescueUnits_Speed[9,0]

# Incidents Severity
IncidentsSeverity = [5,	5, 2,	3,	5,	5,	1,	2, 2,	5,  5,	3,	2, 2]

# Input Data 4: Sum of wj(Pjk + Sijk) oleh unit k di SCHED w
# Import list of schedules
SchedulesFile = 'Hasil Run Sched Heuristics Code.xlsx'
Schedules = pd.read_excel(SchedulesFile, delimiter = ';', sheet_name = 'LP INPUT')
SchedulesArray = np.array(Schedules)
SchedulesArray = np.nan_to_num(SchedulesArray)
# Calculate Sum of wj(Pjk + Sijk) oleh unit k di SCHED w
WeightedCompletionTime1 = np.zeros((3,9))
WeightedCompletionTime2 = np.zeros((3,9))
WeightedCompletionTime3 = np.zeros((3,9))
WeightedCompletionTime4 = np.zeros((3,9))
WeightedCompletionTime5 = np.zeros((3,9))
WeightedCompletionTime6 = np.zeros((3,9))
WeightedCompletionTime7 = np.zeros((3,9))
WeightedCompletionTime8 = np.zeros((3,9))
WeightedCompletionTime9 = np.zeros((3,9))
WeightedCompletionTime10 = np.zeros((3,9))
for i in range(3):
     for w in range(9):
         WeightedCompletionTime1[i,w] = (ProcessTimeArray[0,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit1[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
         WeightedCompletionTime2[i,w] = (ProcessTimeArray[1,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit2[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
         WeightedCompletionTime3[i,w] = (ProcessTimeArray[2,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit3[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
         WeightedCompletionTime4[i,w] = (ProcessTimeArray[3,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit4[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
         WeightedCompletionTime5[i,w] = (ProcessTimeArray[4,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit5[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
         WeightedCompletionTime6[i,w] = (ProcessTimeArray[5,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit6[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
         WeightedCompletionTime7[i,w] = (ProcessTimeArray[6,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit7[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
         WeightedCompletionTime8[i,w] = (ProcessTimeArray[7,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit8[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
         WeightedCompletionTime9[i,w] = (ProcessTimeArray[8,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit9[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
         WeightedCompletionTime10[i,w] = (ProcessTimeArray[9,int(SchedulesArray[i+1,w])-1] + Travel_Time_Unit10[int(SchedulesArray[i,w]),int(SchedulesArray[i+1,w])])*IncidentsSeverity[int(SchedulesArray[i+1,w])-1]
# Buat last row untuk sched 1 - 8 jadi nilainya 0
for sched in range(8):
    WeightedCompletionTime1[2,sched] = 0
    WeightedCompletionTime2[2,sched] = 0
    WeightedCompletionTime3[2,sched] = 0
    WeightedCompletionTime4[2,sched] = 0
    WeightedCompletionTime5[2,sched] = 0
    WeightedCompletionTime6[2,sched] = 0
    WeightedCompletionTime7[2,sched] = 0
    WeightedCompletionTime8[2,sched] = 0
    WeightedCompletionTime9[2,sched] = 0
    WeightedCompletionTime10[2,sched] = 0
# Buat np.array 10 x 9 untuk setor Weighted Completion Time masing2 unit
WeightedCompletionTime = np.zeros((10,9))
for w in range(9):
    WeightedCompletionTime[0,w] = WeightedCompletionTime1[0,w] + WeightedCompletionTime1[1,w] + WeightedCompletionTime1[2,w]
    WeightedCompletionTime[1,w] = WeightedCompletionTime2[0,w] + WeightedCompletionTime2[1,w] + WeightedCompletionTime2[2,w]
    WeightedCompletionTime[2,w] = WeightedCompletionTime3[0,w] + WeightedCompletionTime3[1,w] + WeightedCompletionTime3[2,w]
    WeightedCompletionTime[3,w] = WeightedCompletionTime4[0,w] + WeightedCompletionTime4[1,w] + WeightedCompletionTime4[2,w]
    WeightedCompletionTime[4,w] = WeightedCompletionTime5[0,w] + WeightedCompletionTime5[1,w] + WeightedCompletionTime5[2,w]
    WeightedCompletionTime[5,w] = WeightedCompletionTime6[0,w] + WeightedCompletionTime6[1,w] + WeightedCompletionTime6[2,w]
    WeightedCompletionTime[6,w] = WeightedCompletionTime7[0,w] + WeightedCompletionTime7[1,w] + WeightedCompletionTime7[2,w]
    WeightedCompletionTime[7,w] = WeightedCompletionTime8[0,w] + WeightedCompletionTime8[1,w] + WeightedCompletionTime8[2,w]
    WeightedCompletionTime[8,w] = WeightedCompletionTime9[0,w] + WeightedCompletionTime9[1,w] + WeightedCompletionTime9[2,w]
    WeightedCompletionTime[9,w] = WeightedCompletionTime10[0,w] + WeightedCompletionTime10[1,w] + WeightedCompletionTime10[2,w]
# Weighted Completion Time needs to be integer
WeightedCompletionTime = WeightedCompletionTime.astype(int)
# Data Input for Parameters
# ajw (Does sched w contains incident j? yes = 1 no = 0)
ajw = pd.read_excel(SchedulesFile, delimiter = ';', sheet_name = 'ajw')
ajw = np.array(ajw)
# Incidents x Capability Matrix (Reqjq)     
Reqjq = pd.read_excel(SchedulesFile, delimiter = ';', sheet_name = 'Incidents Capability Matrix')
Reqjq = np.array(Reqjq)
# Units x Capability Matrix (Capkq)
Capkq = pd.read_excel(SchedulesFile, delimiter = ';', sheet_name = 'Units Capability Matrix')
Capkq = np.array(Capkq)
# Make Variables List
Sched = ['SCHED 1', 'SCHED 2',	'SCHED 3',	'SCHED 4'	,'SCHED 5'	,'SCHED 6'	,'SCHED 7'	,'SCHED 8',	'SCHED 9']
Units = ['Unit 1',	'Unit 2',	'Unit 3',	'Unit 4',	'Unit 5',	'Unit 6',	'Unit 7',	'Unit 8',	'Unit 9',	'Unit 10']
Capability = ['Cap 1',	'Cap 2',	'Cap 3',	'Cap 4',	'Cap 5',	'Cap 6',	'Cap 7',	'Cap 8']
# Gurobi Optimization
import gurobipy as gp
from gurobipy import GRB
m = gp.Model("mip1")
# Make Variables
x = m.addMVar((10,9), name="x", lb = 0.0, vtype = GRB.CONTINUOUS)
m.update()
# Objective Function
# WARNING: MASIH SALAH, BUKAN SUMPRODUCT, HARUSNYA SUMPRODUCT
for k in range(len(Units)):
    for w in range(len(Sched)):
        Objective = WeightedCompletionTime[k,w]*x[k,w]
m.setObjective((Objective), GRB.MINIMIZE)
# Constraints
# Constraint 1: Semua rescue units dipilih
m.addConstrs((sum(x[0,w]) == 1 for w in range(len(Sched))), name='c0')
m.addConstrs((sum(x[1,w]) == 1 for w in range(len(Sched))), name='c0')
m.addConstrs((sum(x[2,w]) == 1 for w in range(len(Sched))), name='c0')
m.addConstrs((sum(x[3,w]) == 1 for w in range(len(Sched))), name='c0')
m.addConstrs((sum(x[4,w]) == 1 for w in range(len(Sched))), name='c0')
m.addConstrs((sum(x[5,w]) == 1 for w in range(len(Sched))), name='c0')
m.addConstrs((sum(x[6,w]) == 1 for w in range(len(Sched))), name='c0')
m.addConstrs((sum(x[7,w]) == 1 for w in range(len(Sched))), name='c0')
m.addConstrs((sum(x[8,w]) == 1 for w in range(len(Sched))), name='c0')
m.addConstrs((sum(x[9,w]) == 1 for w in range(len(Sched))), name='c0')

# Constraint 2:  Schedule dikerjakan sama unit yang emang bisa ngerjain schedule itu
# Masih Error: 'TempConstr' object is not iterable
# Apa harus bikin constraint per insiden dan per capability kaya di Excel ya?
m.addConstrs((sum(Capkq[k,q]*ajw[0,w]*x[k,w] >= Reqjq[0,q]) for k in range(len(Units)) for q in range(len(Capability)) for w in range(len(Sched))), name='c0')