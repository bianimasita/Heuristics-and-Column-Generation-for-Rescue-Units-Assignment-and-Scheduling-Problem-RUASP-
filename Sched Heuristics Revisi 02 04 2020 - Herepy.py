# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:53:35 2020

@author: Biani Masita
"""

#Input Data 1: Distance Table
import herepy
import numpy as np
import pandas as pd
herepy.here_enum.MatrixSummaryAttribute
routingApi = herepy.RoutingApi('iqR92YoaCji_Y8hsq_tcAYyPDIk576xNZ6njsPuq3KM')
X_coordinate = [15,	76,	76,	96,	8,	54,	85,	74,	63,	63,	71,	71,	93,	57,	57]
Y_coordinate = [88,	57,	57,	62,	63,	22,	33,	62,	54,	54,	86,	86,	79,	58,	58]

# Read Depots and Incidents Coordinates

response = routingApi.matrix(
    start_waypoints=[[-6.217384,106.932765], [-6.171159,106.786711]],
    destination_waypoints=[[-6.171716,106.800519], [-6.138936,106.693909]],
    departure='2013-07-04T17:00:00+02',
    modes=[herepy.RouteMode.fastest, herepy.RouteMode.car], summary_attributes = ['distance'])

Distance_table = np.zeros((15, 15))
list_incident = list(range(15))

for index1 in list_incident:
    for index2 in list_incident:
        Distance_table[index1, index2] = ((X_coordinate[index1] - X_coordinate[index2])**2 + (Y_coordinate[index1] - Y_coordinate[index2])**2) ** 0.5

#Input Data 2: Rescue Units & Incidents Capability Match Table
ProcessTimeFile = 'Data Input 10 Unit 10 Incidents.xlsx'
CapMatch = pd.read_excel(ProcessTimeFile, delimiter = ';', sheet_name = 'Units x Incidents Match')
CapMathArray = np.array(CapMatch)
				
#Input Data 3: Rescue Units Speed and Travel Time Matrix
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
Travel_Time_Unit1 = np.zeros((15,15))
Travel_Time_Unit2 = np.zeros((15,15))
Travel_Time_Unit3 = np.zeros((15,15))
Travel_Time_Unit4 = np.zeros((15,15))
Travel_Time_Unit5 = np.zeros((15,15))
Travel_Time_Unit6 = np.zeros((15,15))
Travel_Time_Unit7 = np.zeros((15,15))
Travel_Time_Unit8 = np.zeros((15,15))
Travel_Time_Unit9 = np.zeros((15,15))
Travel_Time_Unit10 = np.zeros((15,15))

for index1 in range(15):
    for index2 in range(15): 
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
        
#Append the index row
indexrow15 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
indexrow15 = np.reshape(indexrow15,(1,15))
indexrow14 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
indexrow14 = np.reshape(indexrow14,(1,14))
Travel_Time_Unit1 = np.append(Travel_Time_Unit1,indexrow15, axis = 0)
Travel_Time_Unit2 = np.append(Travel_Time_Unit2,indexrow15, axis = 0)
Travel_Time_Unit3 = np.append(Travel_Time_Unit3,indexrow15, axis = 0)
Travel_Time_Unit4 = np.append(Travel_Time_Unit4,indexrow15, axis = 0)
Travel_Time_Unit5 = np.append(Travel_Time_Unit5,indexrow15, axis = 0)
Travel_Time_Unit6 = np.append(Travel_Time_Unit6,indexrow15,axis = 0)
Travel_Time_Unit7 = np.append(Travel_Time_Unit7,indexrow15, axis = 0)
Travel_Time_Unit8 = np.append(Travel_Time_Unit8,indexrow15, axis = 0)
Travel_Time_Unit9 = np.append(Travel_Time_Unit9,indexrow15, axis = 0)
Travel_Time_Unit10 = np.append(Travel_Time_Unit10,indexrow15, axis = 0)
# Input Data 5: Incidents Severity
IncidentsSeverity = [5,	5, 2,	3,	5,	5,	1,	2, 2,	5,  5,	3,	2, 2]
CapMathArray = np.append(CapMathArray, indexrow14, axis = 0)
        
#Rescue Units Processing Time
ProcessTimeFile = 'Data Input 10 Unit 10 Incidents.xlsx'
ProcessTime = pd.read_excel(ProcessTimeFile, delimiter = ';', sheet_name = 'Process Time')
ProcessTimeArray = np.array(ProcessTime)
ProcessTimeArray = np.append(ProcessTimeArray, indexrow14, axis = 0)
#Sched Heuristics
# Generate Schedule
# Initiate
IncidentsProcessed1 = []
IncidentsSchedule = []
# Make (Pjk + Sijk)/wj Table (Weighted Time Table) for unit 1 --> Ini kayanya bisa di loop atau def function aja
WeightedTimeUnit1 = np.zeros((1,14))
WeightedTimeUnit2 = np.zeros((1,14))
WeightedTimeUnit3 = np.zeros((1,14))
WeightedTimeUnit4 = np.zeros((1,14))
WeightedTimeUnit5 = np.zeros((1,14))
WeightedTimeUnit6 = np.zeros((1,14))
WeightedTimeUnit7 = np.zeros((1,14))
WeightedTimeUnit8 = np.zeros((1,14))
WeightedTimeUnit9 = np.zeros((1,14))
WeightedTimeUnit10 = np.zeros((1,14))
# Put all functions here
def deleteincidents(x):
    return  np.delete(x,IncidentsRemove1[i],1)
def removeduplicate(x):
    return list(dict.fromkeys(x))
def mincompletiontime(x):
    return np.amin(x[x != 0])
def incidentprocessed(x,y):
    return np.argwhere(x == y)
def deleteincidentsagain(x):
    return  np.delete(x,IncidentsRemove1[i]-1,1)
# Bikin Index Keberangkatan Travel Time
Unit1Incident = 0
Unit2Incident = 0
Unit3Incident = 0
Unit4Incident = 0
Unit5Incident = 0
Unit6Incident = 0
Unit7Incident = 0
Unit8Incident = 0
Unit9Incident = 0
Unit10Incident = 0
# Iteration 1: From Depot --> Ini kayanya bisa di loop atau def function aja
# Pertanyaannya: kenapa saat diiterasi, yang keisi di WeightedTimeUnit itu tetap yang keisi yg index > len(list_incident)+1?
IndikatorBelumDipilih = np.ones(14)
# Bikin loop while untuk iterasi jika list_incident != []
list_incidentloop = list(range(14))
while list_incidentloop != []:
    for i in range(14):
        # pilih yg paling minimum --> cek juga sudah dipilih apa belum
        WeightedTimeUnit1[0,i] = ((ProcessTimeArray[0,i] + Travel_Time_Unit1[Unit1Incident,i+1])/IncidentsSeverity[i])*CapMathArray[0,i]*IndikatorBelumDipilih[i]
        WeightedTimeUnit2[0,i] = ((ProcessTimeArray[1,i] + Travel_Time_Unit2[Unit2Incident,i+1])/IncidentsSeverity[i])*CapMathArray[1,i]*IndikatorBelumDipilih[i]
        WeightedTimeUnit3[0,i] = ((ProcessTimeArray[2,i] + Travel_Time_Unit3[Unit3Incident,i+1])/IncidentsSeverity[i])*CapMathArray[2,i]*IndikatorBelumDipilih[i]
        WeightedTimeUnit4[0,i] = ((ProcessTimeArray[3,i] + Travel_Time_Unit4[Unit4Incident,i+1])/IncidentsSeverity[i])*CapMathArray[3,i]*IndikatorBelumDipilih[i]
        WeightedTimeUnit5[0,i] = ((ProcessTimeArray[4,i] + Travel_Time_Unit5[Unit5Incident,i+1])/IncidentsSeverity[i])*CapMathArray[4,i]*IndikatorBelumDipilih[i]
        WeightedTimeUnit6[0,i] = ((ProcessTimeArray[5,i] + Travel_Time_Unit6[Unit6Incident,i+1])/IncidentsSeverity[i])*CapMathArray[5,i]*IndikatorBelumDipilih[i]
        WeightedTimeUnit7[0,i] = ((ProcessTimeArray[6,i] + Travel_Time_Unit7[Unit7Incident,i+1])/IncidentsSeverity[i])*CapMathArray[6,i]*IndikatorBelumDipilih[i]
        WeightedTimeUnit8[0,i] = ((ProcessTimeArray[7,i] + Travel_Time_Unit8[Unit8Incident,i+1])/IncidentsSeverity[i])*CapMathArray[7,i]*IndikatorBelumDipilih[i]
        WeightedTimeUnit9[0,i] = ((ProcessTimeArray[8,i] + Travel_Time_Unit9[Unit9Incident,i+1])/IncidentsSeverity[i])*CapMathArray[8,i]*IndikatorBelumDipilih[i]
        WeightedTimeUnit10[0,i] = ((ProcessTimeArray[9,i] + Travel_Time_Unit10[Unit10Incident,i+1])/IncidentsSeverity[i])*CapMathArray[9,i]*IndikatorBelumDipilih[i]

# Find Arg min(Pjk + Sijk)/wj for each Rescue Units and corresponding incidents
# Debug 1: unit1time dllnya marah kalo weightedtimeunitnya isinya 0 semua jadi perlu code if sih kayaknya supaya kita ga manual hapus2in 
    #Unit 1
    if np.count_nonzero(WeightedTimeUnit1) > 0:
        Unit1Time = np.amin(WeightedTimeUnit1[WeightedTimeUnit1 != 0])
        Unit1Incident = np.argwhere(WeightedTimeUnit1 == Unit1Time)
        Unit1Incident = int(Travel_Time_Unit1[15,Unit1Incident[0,1]])
        IncidentsProcessed1.append(Unit1Incident)
        IncidentsSchedule.append(str(Unit1Incident) + " " + "Unit 1")
    #Unit 2
    if np.count_nonzero(WeightedTimeUnit2) > 0:
        Unit2Time = np.amin(WeightedTimeUnit2[WeightedTimeUnit2 != 0])
        Unit2Incident = np.argwhere(WeightedTimeUnit2 == Unit2Time)
        Unit2Incident = int(Travel_Time_Unit2[15,Unit2Incident[0,1]])
        IncidentsProcessed1.append(Unit2Incident)
        IncidentsSchedule.append(str(Unit2Incident) + " " + "Unit 2")
    #Unit 3
    if np.count_nonzero(WeightedTimeUnit3) > 0:
        Unit3Time = np.amin(WeightedTimeUnit3[WeightedTimeUnit3 != 0])
        Unit3Incident = np.argwhere(WeightedTimeUnit3 == Unit3Time)
        Unit3Incident = int(Travel_Time_Unit3[15,Unit3Incident[0,1]])
        IncidentsProcessed1.append(Unit3Incident)
        IncidentsSchedule.append(str(Unit3Incident) + " " + "Unit 3")
    #Unit 4
    if np.count_nonzero(WeightedTimeUnit4) > 0:
        Unit4Time = np.amin(WeightedTimeUnit4[WeightedTimeUnit4 != 0])
        Unit4Incident = np.argwhere(WeightedTimeUnit4 == Unit4Time)
        Unit4Incident = int(Travel_Time_Unit4[15,Unit4Incident[0,1]])
        IncidentsProcessed1.append(Unit4Incident)
        IncidentsSchedule.append(str(Unit4Incident) + " " + "Unit 4")
    #Unit5
    if np.count_nonzero(WeightedTimeUnit5) > 0:
        Unit5Time = np.amin(WeightedTimeUnit5[WeightedTimeUnit5 != 0])
        Unit5Incident = np.argwhere(WeightedTimeUnit5 == Unit5Time)
        Unit5Incident = int(Travel_Time_Unit5[15,Unit5Incident[0,1]])
        IncidentsProcessed1.append(Unit5Incident)
        IncidentsSchedule.append(str(Unit5Incident) + " " + "Unit 5")
    #Unit6
    if np.count_nonzero(WeightedTimeUnit6) > 0:
        Unit6Time = np.amin(WeightedTimeUnit6[WeightedTimeUnit6 != 0])
        Unit6Incident = np.argwhere(WeightedTimeUnit6 == Unit6Time)
        Unit6Incident = int(Travel_Time_Unit6[15,Unit6Incident[0,1]])
        IncidentsProcessed1.append(Unit6Incident)
        IncidentsSchedule.append(str(Unit6Incident) + " " + "Unit 6")
    #Unit7
    if np.count_nonzero(WeightedTimeUnit7) > 0:
        Unit7Time = np.amin(WeightedTimeUnit7[WeightedTimeUnit7 != 0])
        Unit7Incident = np.argwhere(WeightedTimeUnit7 == Unit7Time)
        Unit7Incident = int(Travel_Time_Unit7[15,Unit7Incident[0,1]])
        IncidentsProcessed1.append(Unit7Incident)
        IncidentsSchedule.append(str(Unit7Incident) + " " + "Unit 7")
    #Unit8
    if np.count_nonzero(WeightedTimeUnit8) > 0:
        Unit8Time = np.amin(WeightedTimeUnit8[WeightedTimeUnit8 != 0])
        Unit8Incident = np.argwhere(WeightedTimeUnit8 == Unit8Time)
        Unit8Incident = int(Travel_Time_Unit8[15,Unit8Incident[0,1]])
        IncidentsProcessed1.append(Unit8Incident)
        IncidentsSchedule.append(str(Unit8Incident) + " " + "Unit 8")
    #Unit9
    if np.count_nonzero(WeightedTimeUnit9) > 0:
        Unit9Time = np.amin(WeightedTimeUnit9[WeightedTimeUnit9 != 0])
        Unit9Incident = np.argwhere(WeightedTimeUnit9 == Unit9Time)
        Unit9Incident = int(Travel_Time_Unit9[15,Unit9Incident[0,1]])
        IncidentsProcessed1.append(Unit9Incident)
        IncidentsSchedule.append(str(Unit9Incident) + " " + "Unit 9")
    #Unit10
    if np.count_nonzero(WeightedTimeUnit10) > 0:
        Unit10Time = np.amin(WeightedTimeUnit10[WeightedTimeUnit10 != 0])
        Unit10Incident = np.argwhere(WeightedTimeUnit10 == Unit10Time)
        Unit10Incident = int(Travel_Time_Unit10[15,Unit10Incident[0,1]])
        IncidentsProcessed1.append(Unit10Incident)
        IncidentsSchedule.append(str(Unit10Incident) + " " + "Unit 10")
        
# Remove Incidents from List for Next Iteration
# Debug 2: kalo i di list incident udh gaada lagi dia marah --> kita update aja trus incidents remove1 nya jadi tiap iterasi jadi 0 lagi
    IncidentsRemove1 = removeduplicate(IncidentsProcessed1)
    for i in range(len(IncidentsRemove1)):
        if IncidentsRemove1[i] in list_incidentloop:
            list_incidentloop.remove(IncidentsRemove1[i])
        
 # ketika sudah dipilih, update IndikatorBelumDipilih(yd dipilih) = 0
    for i in IncidentsProcessed1:
        IndikatorBelumDipilih[i] = 0
        
# There's still some problems in this code:
# 1 : Kita gatau index incidentsprocessed1 = unit krn bsa jadi ada yg di skip
# --> Solusi kepikiran adalah coba bikin lagi list buat masukkin incident + string "Unit 1"
# 2 : Incident 14 kagak ada yang bsa proses padahal di capmatharray dia bisa diproses unit 4 dan 5
# --> coba cek indexrow14