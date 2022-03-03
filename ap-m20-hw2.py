#!/bin/python
import random
import time
import sys
import copy

# RAZI Univercity KERMASHAh
# AETHUR Information
# Proffesor : MARYAM TAGHIZADEH
# Student : SALAR MUHAMMADI ##
# BS. Student in COMPUTER SCIENCE at RAZI University
# ADVANCE PROGRAMMING (FUNCTIONS)
# Collection of Statistical Information (CSI) , Data received from households (DRH)
# CORONA TEST (CT) , Traffic of People (TP)
###
### TOP SUBJECT ###
###
# Given LISTs

Days = [1, 365]
# Days Range

Cities = []  # LIMIT 30
# Cities Representation

Households = []  # LIMIT 30
# HouseHolds Representation

Peoples = []  # LIMIT 100
# Person Representation

### Pure Lists ###

# Traffics = [['Person','Datetime','Household','Ttype','Status','Penalty']]
Traffics = []
# Traffic Events

# CoronaTests = [['Datetime','Person','Result']]
CoronaTests = []
# Corona Test Events

# Penalties = [['Datetime','Person','Traffic', Status , Type ,'Bill']]
Penalties = []
# Penalties Events

# Bills = [['Datetime','Penalty','Cost','Status']]
Bills = []
# Bills Events

# CTR = [['CTC', 'BLOCK'], ['ITC', 'FREE']]
CTR = []
# City Traffic Rules

# CTC = City to City
# ITC = InsideTheCity

# CTRUL = [['Datetime', 'City','CTR']]
CTRUL = []
# City Traffic Rules Update LOG

# CSUL = [['Datetime', 'City', 'Status']]
CSUL = []
# CityInfo = [[[CTRULID],["Household"],["Status"]]]
# City Status --> 0 = Clean , 1 = Probably , 2 = Infected , 3 = Yellow , 4 = Critical
CityInfo = []
# City Information

# HHSUL = [['Datetime','houseH','Status']]
# HouseHInfo Status --> 0 = Clean , 1 = Probably , 2 = Infected , 3 = Criticla
HHSUL = []
# HouseHoldStatusUpdateLog

# HouseHInfo = [['City'}, ['members'], ['relationHH'], ['Status']]]
HouseHInfo = []
# HouseHold Informations

# PISUL = [['Datetime','Person','Status']]
PISUL = []
# PersonInfoStatusUpdateLog

# PersonInfo = [[['HouseHold','LastLocation'], ['Status'], ['Relations'],['Tests'], ['Traffics'], ['Penalties'],['Bills']]]
PersonInfo = []
# Person Informations

Today = int(1)
PrintDelay = 0
PrintOn = 0


def today(tday: int):
    global Today
    Today = tday

##################################################################################################
##################################################################################################

### Print Functions ###

##################################################################################################

# City Population Counter


def CPC(city: list):
    cpc = 0
    for h in city[1]:
        cpc += len(HouseHInfo[h][1])
    return cpc

##################################################################################################

# Print CityInfo


def PCI(c: int):
    city = CityInfo[c]
    ctc = "BLOCK" if CTRUL[city[0][-1]][2][0] else "FREE "
    itc = "BLOCK" if CTRUL[city[0][-1]][2][1] else "FREE "
    cityN = Cities[c]
    popu = 0 if not len(city[1]) else CPC(city)
    sping = -1 if not len(city[2]) else CSUL[city[2][-1]][2]
    status = "Clean" if sping <= 0 else ("Probability" if sping == 1 else (
        "Infected" if sping == 2 else "Warning" if sping == 3 else ("Critical")))
    print('-'*111)
    print(
        f"\n\tCity: {cityN} - CTC : {ctc} - ITC : {itc} --> Population: {popu} ==> Status: {status}\n")
    print('-'*111)
    time.sleep(PrintDelay)
# Print CityInfo

##################################################################################################

# Print All City Informations


def PACI():
    for city in range(len(CityInfo)):
        PCI(city)

##################################################################################################

# Print Person Information


def PPI(p: int):
    personN = Peoples[p]
    Person = PersonInfo[p]
    HouseHold = Households[Person[0][0]]
    LStatus = -1 if not len(Person[1]) else PISUL[Person[1][-1]][2]
    status = "Clean" if LStatus <= 0 else ("Probability" if LStatus == 1 else (
        "Infected" if (Today - CoronaTests[Person[3][-1]][0]) < 8 else "Probability-Plus"))
    print(
        f"\n\t\t\tPerson: {personN} in House {HouseHold} Has Status: {status}\n")
    time.sleep(PrintDelay)

##################################################################################################

# Print All Person Information


def PAPI():
    for p in range(len(PersonInfo)):
        PPI(p)

##################################################################################################


# Print Household Information

def PHI(house: int):
    h = HouseHInfo[house]
    House = Households[house]
    Location = Cities[h[0][0]]
    Members = []
    if len(h[1]) > 0:
        for m in h[1]:
            Members.append(Peoples[m])
    RelationHH = []
    for hh in h[2]:
        RelationHH.append(Households[hh])
    LStatus = -1 if not len(h[3]) else HHSUL[h[3][-1]][2]
    status = "Clean" if LStatus <= 0 else (
        "Probability" if LStatus == 1 else ("Infected" if LStatus == 2 else "Critical"))
    print(
        f"\n\t\tHouse: {House} in City: {Location} with members: {Members} and Relations: {RelationHH} has Status: {status}\n")
    time.sleep(PrintDelay)

##################################################################################################

# Print All Household Information


def PAHI():
    for house in range(len(HouseHInfo)):
        PHI(house)

##################################################################################################

# Print Corona Test By id


def PCT(ctid: int):
    test = CoronaTests[ctid]
    print(
        f"\n\t\t\t\tCoronaTest : {ctid} :: Datetime: {test[0]} - Result: {test[2]} ")
    time.sleep(PrintDelay)

##################################################################################################

# Print  Traffic Record


def PTR(trid: int):
    traf = Traffics[trid]
    person = traf[0]
    if traf[3]:
        print(
            f"\n\t\t\t\tTrafficRecord : {trid} :: Datetime: {traf[1]} - Person : {Peoples[person]} tracked from House : {Households[PersonInfo[person][0][1]]} to {Households[traf[2]]} in City : {Cities[HouseHInfo[traf[2]][0][0]]}")
    else:
        print(
            f"\n\t\t\t\tTrafficRecord : {trid} :: Datetime: {traf[1]} - Person : {Peoples[person]} tracked from House : {Households[PersonInfo[person][0][1]]} in City: {Cities[HouseHInfo[PersonInfo[person][0][1]][0][0]]} to House : {Households[traf[2]]} in City : {Cities[HouseHInfo[traf[2]][0][0]]}")
    time.sleep(PrintDelay)

##################################################################################################

# Print Traffic Penalty
# Penalties = [['Datetime','Person','Traffic', Status , Type ,'Bill']]


def PTP(pen: int):
    Pen = Penalties[pen]
    penType = "Tresspass"
    billstat = [2, 3, 9, 10, 11]
    for pt in billstat:
        if pt == Pen[3]:
            penType = "Convict"
            break
    trType = "ITC" if Pen[4] else "CTC"
    print(
        f"\n\t\t\t\t\tPenalty Record : {pen} :: Datetime : {Pen[0]} - Person : {Pen[2]} => has {penType} {trType} With Bill : {Pen[5]}")
    time.sleep(PrintDelay)

##################################################################################################

# Print Penalty Bill
# Bills = [['Datetime','Penalty','Cost','Status']]


def PPB(bil: int):
    Bil = Bills[bil]
    status = "Paid" if not Bil[3] else "Not Paid"
    print(
        f"\n\t\t\t\t\t\t\tBill Record : {bil} :: Datetime : {Bil[0]} - at Penalty : {Bil[1]} with Cost : {Bil[2]} has {status}. ")
    time.sleep(PrintDelay)

##################################################################################################

# Print Large City Info


def PLCI():
    for City in range(len(Cities)):
        city = CityInfo[City]
        PCI(City)
        for House in city[1]:
            house = HouseHInfo[House]
            PHI(House)
            for Person in house[1]:
                person = PersonInfo[Person]
                PPI(Person)
                for ct in person[3]:
                    PCT(ct)
                for traffic in person[5]:
                    PTR(traffic)
                    if Traffics[traffic][5] > -1:
                        PTP(Traffics[traffic][5])
                        if Penalties[Traffics[traffic][5]][5] > -1:
                            PPB(Penalties[Traffics[traffic][5]][5])


##################################################################################################

# Print Corona Test (LastOne)


def CTP(person: int):
    t = PersonInfo[person][3][-1]
    PCT(t)

# Print Corona Test

##################################################################################################

# Print Person Traffic (LastOne)
# Traffics = [['Person','Datetime','Household','ttype','Status','Penalty']]


def PPT(person: int):
    tr = PersonInfo[person][4][-1]
    PTR(tr)


##################################################################################################
##################################################################################################

### Sync Functions ###

# Abstract Sync Information Index


def ASII(Lists: list, subStruct: int):
    lrl = len(Lists[0])
    lil = len(Lists[1])
    if lil < lrl:
        for x in range(lil, lrl):
            newStruct = list()
            for s in range(subStruct):
                newStruct.append(list())
            Lists[1].append(copy.deepcopy(newStruct))

##################################################################################################

# Sync Cities Information Index


def SyncCII():
    ASII([Cities, CityInfo], 3)
# Sync Cities Information Index

##################################################################################################

# Sync HouseHolds Information Index


def SyncHII():
    ASII([Households, HouseHInfo], 4)
# Sync HouseHolds Information Index

##################################################################################################

# Sync Peoples Information Index


def SyncPII():
    ASII([Peoples, PersonInfo], 7)
# Sync HouseHolds Information Index

##################################################################################################
##################################################################################################

### LOGS Functions ###

# City Traffic Rule Update Log


def CTRU(city: int, CTR: list, date: int, prt: int):
    CTRUL.append(copy.deepcopy([date, city, CTR[:]]))
    uid = len(CTRUL) - 1
    CityInfo[city][0].append(uid)
    if prt:
        print("\n \t\t\t\t\tCTRU:", [date, city, CTR][:])
        time.sleep(PrintDelay)

##################################################################################################

# City Status Update Log


def CSU(city: int, Status: int, date: int, prt: int):
    CSUL.append(copy.deepcopy([date, city, Status]))
    uid = len(CSUL)-1
    CityInfo[city][2].append(uid)
    if prt:
        print("\n \t\t\t\t\tCSU:", [date, city, Status])
        time.sleep(PrintDelay)

# City Status Refresh
# HouseHInfo = [['City'}, ['members'], ['relationHH'], ['Status']]]


def CSR(city: int, today: int, prt: int):
    cst = CSUL[CityInfo[city][2][-1]][2]
    status = 0
    allTests = 0
    AllNegTests = 0
    for h in CityInfo[city][1]:
        home = HouseHInfo[h]
        hst = 0 if not len(home[3]) else(
            HHSUL[home[3][-1]][2] if HHSUL[home[3][-1]][2] < 3 else 2)
        status = hst if status < hst else status
        for m in home[1]:
            if len(PersonInfo[m][3]):
                for test in PersonInfo[m][3]:
                    allTests += 1
                    AllNegTests += 1 if not CoronaTests[test][2] else 0
    if status > 1:
        status = 3 if ((AllNegTests*100)/allTests) > 75 else 4
    if not cst == status:
        CSU(city, status, today, prt)


##################################################################################################


# Household Status Update Log

def HSU(house: int, Status: int, date: int, recF: int, prt: int):
    if Status and len(HouseHInfo[house][3]) and HHSUL[HouseHInfo[house][3][-1]][2] > Status:
        for m in HouseHInfo[house][1]:
            if (PISUL[PersonInfo[m][1][-1]][2] < 2 or (PISUL[PersonInfo[m][1][-1]][2] >= 2 and (Today - PISUL[PersonInfo[m][1][-1]][0] > 7))) and m != recF:
                PSU(m, 1, date, -1, prt)
        return
    HHSUL.append(copy.deepcopy([date, house, Status]))
    uid = len(HHSUL)-1
    HouseHInfo[house][3].append(uid)
    if recF > -1 and Status:
        for m in HouseHInfo[house][1]:
            if (PISUL[PersonInfo[m][1][-1]][2] < 2 or (PISUL[PersonInfo[m][1][-1]][2] >= 2 and (Today - PISUL[PersonInfo[m][1][-1]][0] > 7))) and m != recF:
                PSU(m, 1, date, -1, prt)
    if recF > -1 and not Status:
        for m in HouseHInfo[house][1]:
            if (PISUL[PersonInfo[m][1][-1]][2] < 2 or (PISUL[PersonInfo[m][1][-1]][2] >= 2 and (Today - PISUL[PersonInfo[m][1][-1]][0] > 7))) and m != recF:
                PSU(m, 0, date, -1, prt)
    if prt:
        print("\n\t\t\t\t\tHSU:", [date, house, Status][:])
        time.sleep(PrintDelay)
    CSR(HouseHInfo[house][0][0], date, prt)

##################################################################################################

# Find Second Infected Person of House


def FSIPH(person: int):
    if len(HouseHInfo[PersonInfo[person][0][0]][1]) > 1:
        for m in HouseHInfo[PersonInfo[person][0][0]][1]:
            if m != person:
                if len(PersonInfo[m][3]) and CoronaTests[PersonInfo[m][3][-1]][2] and (Today - CoronaTests[PersonInfo[m][3][-1]][0]) < 8:
                    return True
    return False

##################################################################################################

# Person Status Update Log


def PSU(person: int, Status: int, date: int, recF: int, prt: int):
    PISUL.append(copy.deepcopy([date, person, Status]))
    uid = len(PISUL)-1
    PersonInfo[person][1].append(uid)
    if prt:
        print("\n\t\t\t\t\tPSU:", [date, person, Status][:])
        time.sleep(PrintDelay)
    if recF > -1 and Status:
        hStat = Status if Status < 2 else (3 if FSIPH(person) else 2)
        HSU(PersonInfo[person][0][0], hStat, date, person, prt)
    if not recF and not Status:
        Clean = True
        for m in HouseHInfo[PersonInfo[person][0][0]][1]:
            if m != person:
                sm = int(PISUL[PersonInfo[m][1][-1]][2])
                if sm:
                    if Today - PISUL[PersonInfo[m][1][-1]][0] > 7:
                        sm -= 1
                    if sm:
                        Clean = False
                        break
        if Clean:
            HSU(PersonInfo[person][0][0], 0, date, person, prt)
    CSR(HouseHInfo[PersonInfo[person][0][0]][0][0], date, prt)


##################################################################################################
# Corona Test Submit Log


def CTS(Person: int, Result: int, Date: int, prt):
    CoronaTests.append(copy.deepcopy([Date, Person, Result]))
    uid = len(CoronaTests) - 1
    PersonInfo[Person][3].append(uid)
    status = 2 if Result else 0
    PSU(Person, status, Date, Result, prt)
    if Result:
        for h in HouseHInfo[PersonInfo[Person][0][0]][2]:
            HSU(h, 1, Date, Person, prt)
    if prt:
        PCT(uid)
# Corona Test Submit

##################################################################################################

# Penalty Bills Submit


def PBS(penalty: int, date: int, cost: int, status: int, prt: int):
    Bills.append(copy.deepcopy([date, penalty, cost, status]))
    uid = len(Bills)-1
    if prt:
        PPB(uid)
    return uid

##################################################################################################

# Traffic Penalties Submit


def TPS(Person: int, Traffic: int, date: int, status: int, ttype: int, ptr: int):
    Penalties.append(copy.deepcopy([date, Person, Traffic, status, ttype, -1]))
    uid = len(Penalties) - 1
    PersonInfo[Person][5].append(uid)
    billstat = [2, 3, 9, 10, 11]
    for b in range(len(billstat)):
        if status == billstat[b]:
            billid = PBS(uid, date, b+1, 1, ptr)
            Penalties[uid][5] = billid
            PersonInfo[Person][6].append(billid)
            break
    if ptr:
        PTP(uid)
    return uid

##################################################################################################

# Traffic Penalty Officer


def TPO(Person, Househ, ttype):
    pllctr = list(
        CTRUL[CityInfo[HouseHInfo[PersonInfo[Person][0][1]][0][0]][0][-1]][2])
    # Person Last Status
    pls = int(PISUL[PersonInfo[Person][1][-1]][2])
    pls -= 1 if pls and (Today -
                         PISUL[PersonInfo[Person][1][-1]][0]) > 7 else 0
    if ttype:
        if pllctr[1]:
            if pls > 1:
                # Penalty 3 Double Convict ITC Block
                return 3
            else:
                # Penalty 1 TressPass ITC Block
                return 1
        else:
            if pls > 1:
                # Penalty 2 Convict ITC
                return 2
    else:
        platctr = list(CTRUL[CityInfo[HouseHInfo[Househ][0][0]][0][-1]][2])
        if pllctr[0] and platctr[0]:
            if pls > 1:
                # Penalty 11 Convict CTC Double Block
                return 11
            elif pls == 1:
                # Penalty 8 Tresspass CTC Double Block
                return 8
            else:
                # Penalty 6 Tresspass CTC Double Block
                return 6
        elif pllctr[0] or platctr[0]:
            if pls > 1:
                # Penalty 10 Convict CTC Block
                return 10
            elif pls == 1:
                # Penalty 7 Tresspass CTC Block
                return 7
            else:
                # Penalty 5 Tresspass CTC Block
                return 5
        else:
            if pls > 1:
                # Penalty 9 Convict CTC
                return 9
            elif pls == 1:
                # Penalty 4 Tresspass CTC
                return 4
    # Clean
    return 0

##################################################################################################

    # Traffic Event Submit Log


def TES(Person: int, Date: int, Househ: int, prt: int):
    Ttype = int(1 if HouseHInfo[PersonInfo[Person][0][1]][0][0] ==
                HouseHInfo[Househ][0][0] else 0)  # 0 = CTC , 1 = ITC
    status = int(TPO(Person, Househ, Ttype))
    Traffics.append([Person, Date, Househ, Ttype, status, -1])
    uid = len(Traffics) - 1
    PersonInfo[Person][4].append(uid)
    if not Househ in PersonInfo[Person][2]:
        PersonInfo[Person][2].append(Househ)
    if not PersonInfo[Person][0][0] in HouseHInfo[Househ][2]:
        HouseHInfo[Househ][2].append(PersonInfo[Person][0][0])
    if not Househ in HouseHInfo[PersonInfo[Person][0][0]][2]:
        HouseHInfo[PersonInfo[Person][0][0]][2].append(Househ)
    for m in HouseHInfo[Househ][1]:
        if not PersonInfo[Person][0][0] in PersonInfo[m][2]:
            PersonInfo[m][2].append(PersonInfo[Person][0][0])
    if status:
        penalty = TPS(Person, uid, Date, status, Ttype, prt)
        Traffics[uid][5] = penalty
    if prt:
        PPT(Person)
    PersonInfo[Person][0][1] = Househ
    if PISUL[PersonInfo[Person][1][-1]][2] > 0:
        HSU(Househ, 1, Date, Person, prt)
    if prt:
        PTR(uid)

##################################################################################################
##################################################################################################

### Relation Functions ###

# Relation House to City


def RHC(house, city):
    HouseHInfo[house][0].append(city)
    CityInfo[city][1].append(house)

##################################################################################################

# Relation Person to House


def RPH(person, house):
    HouseHInfo[house][1].append(person)
    PersonInfo[person][0].append(house)
    PersonInfo[person][0].append(house)


##################################################################################################
##################################################################################################

### Random Information Feed Functions ###

# City Traffic Rules RIF


def CTRRIF(city, prt):
    ITC = random.randint(0, 1)
    CTC = ITC if ITC else random.randint(0, 1)
    CTR = [CTC, ITC]
    ldate = CTRUL[-1][0] if len(CTRUL) else 1
    CTRU(city, CTR[:], ldate, prt)
    CSU(city, 0, ldate, prt)

##################################################################################################

# Random Relation Peoples to HouseHolds


def RRPH(house, pCount, prt):
    people = [p for p in range(len(PersonInfo)) if not len(PersonInfo[p][0])]
    for pc in range(pCount):
        person = people.pop(random.randrange(len(people)))
        RPH(person, house)
        PSU(person, 0, Today, -1, prt)
        PersonInfo[person][0][1] = house


##################################################################################################

# Random Relation HouseHolds to Cities


def RRHC(city, hCount, prt):
    houses = [h for h in range(len(HouseHInfo)) if not len(HouseHInfo[h][0])]
    remHH = 0
    for h in range(len(HouseHInfo)):
        if not len(HouseHInfo[h][1]):
            remHH += 1
    remPP = 0
    for p in range(len(PersonInfo)):
        if not len(PersonInfo[p][0]):
            remPP += 1
    for hc in range(hCount):
        house = houses.pop(random.randrange(len(houses)))
        RHC(house, city)
        HSU(house, 0, Today, -1, prt)
        rr = remPP - remHH
        pc = remPP if remHH == 1 else (random.randint(
            1, int(rr/3)) if rr > 1 else(1 if rr == 1 else 0))
        RRPH(house, pc, prt)
        remHH -= 1
        remPP -= pc

##################################################################################################

# City Random Information Feed


def CRIF(prt):
    # NoLink Cities
    remC = 0
    for cc in range(len(CityInfo)):
        if not len(CityInfo[cc][1]):
            remC += 1
    # NoLink House to City
    remH = 0
    for hh in range(len(HouseHInfo)):
        if not len(HouseHInfo[hh][0]):
            remH += 1
    for c in range(len(CityInfo)):
        CTRRIF(c, prt)
        rr = remH - remC
        hc = remH if remC == 1 else (
            random.randint(1, int(rr/2)) if rr > 1 else(1 if rr == 1 else 0))
        RRHC(c, hc, prt)
        remC -= 1
        remH -= hc

##################################################################################################

# Check if Last Corona test of a Person was positive and last at least 7 days after that


def CheckLastTest(person, date):
    if len(PersonInfo[person][3]) and CoronaTests[PersonInfo[person][3][-1]][2] and (date - CoronaTests[PersonInfo[person][3][-1]][0]) < 8:
        return False
    return True
# Check if Last Corona test of a Person was positive and last at least 7 days after that

##################################################################################################

# Find Person ID By Name


def FPIDBN(person):
    for p in Peoples:
        if p == person:
            return Peoples.index(p)
    return -1
# Find Person ID By Name

##################################################################################################

# Corona Test Random Information Feed


def CTRIF(counter, randT, prt):
    # Peoples not in the test range
    td = int(Today)
    pnittr = 0
    persons = copy.deepcopy(Peoples)
    for ct in range(counter):
        if pnittr < len(Peoples):
            randS = random.randrange(len(persons))
            person = persons[randS]
            pid = FPIDBN(person)
            while not CheckLastTest(pid, td):
                persons.pop(randS)
                randS = random.randrange(len(persons))
                person = persons[randS]
                pid = FPIDBN(person)
            randRes = random.randint(0, 1) if randT == 2 else randT
            CTS(pid, randRes, td, prt)
            persons.pop(randS)
            if randRes:
                pnittr += 1
            if not random.randint(0, 1):
                td += random.randint(3, 12)
                if not td == Today:
                    today(td)
        else:
            break


##################################################################################################

# Traffic Events Random Feed


def TERF(count, prt: int, boldDay: int):
    bflag = 0
    td = Today
    te = 0
    while te < count:
        randP = random.randrange(0, len(PersonInfo))
        person = PersonInfo[randP]
        Househ = person[0][1]
        while(Househ == person[0][1]):
            Househ = random.randrange(0, len(HouseHInfo))
        TES(randP, td, Househ, prt)
        te += 1
        td += random.randint(int((365-td)/(count-te+1)/2),
                             int((365-td)/(count-te+1))) if not random.randint(0, 1) else 0
        if boldDay != -1 and not bflag:
            if td >= boldDay:
                td = int(boldDay)
                for x in range(random.randint(1, 6)):
                    randP = random.randrange(0, len(PersonInfo))
                    person = PersonInfo[randP]
                    Househ = person[0][1]
                    while(Househ == person[0][1]):
                        Househ = random.randrange(0, len(HouseHInfo))
                    TES(randP, td, Househ, prt)
                    te += 1
                bflag = 1
        today(td)
# Traffic Events Random Feed

##################################################################################################
##################################################################################################

# Reverse Design

# Fill the Population Sample


def FTPS(pcount, hcount, ccount):
    for p in range(pcount):
        Peoples.append(p+1)
    for x in range(hcount):
        Households.append(x+1)
    for y in range(ccount):
        Cities.append(y+1)
    # Sync Structures
    SyncCII()
    SyncHII()
    SyncPII()

##################################################################################################

# FirstLittleRefresh


def FLR(prt):
    today(1)
    # Persons Size , Houses Size , Cities Size
    FTPS(100, 30, 30)
    # City Random Inforamtion Feed
    CRIF(prt)
    if prt:
        print('='*111)
    # Corona Test Random Submit #arg1 = Count , #arg2 = (0 --> Negative :: 1 --> Positive :: 2 --> Random)
    CTRIF(10, 2, prt)
    if prt:
        print('='*111)
    # Traffic Event Random Feed #arg1 = Count
    TERF(30, prt, -1)
    if prt:
        print('='*111)
        PLCI()
        print('='*111)
        print(Today)


##################################################################################################
##################################################################################################
# MAIN Function
def sysManual():
    print("./ap-m20-hw2.py [Arg1 = RequestCode:Required] [Arg(n) Options]")
    print("Request Code : Q1 ==> Options: [Counts]")
    print("Request Code : Q2 ==> Options: [Counts] [FromDay] [ToDay]")
    print("Request Code : Q3 ==> Options: [Counts][Day/From-Day][To-Day]")
    print("Request Code : Q4 ==> Options: [Counts]")
    print("Request Code : Q5 ==> Require: [Day]")
    print("Request Code : Q6 ==> Options: [Person]")
    print("Request Code : Q7 ==> Options: [Start Day] [Stop Day]")


##################################################################################################

# Request Code 0 (Q1) :: MostWantedPerson Decreasing

##################################################################################################


def plchk(pl, p):
    for pp in range(len(pl)):
        for ppp in range(len(pl[pp])):
            if pl[pp][ppp] == p:
                return [pp, ppp]
    return 0

##################################################################################################

# Find Most Wanted Person


def FMWP(PeopleList: list, limitHC: int):
    pl = copy.deepcopy(PeopleList)
    mostWantedPerson = list()
    for p in range(len(PersonInfo)):
        if not len(PersonInfo[p][5]):
            continue
        plchkk = plchk(pl, p)
        if plchkk:
            pl[plchkk[0]].pop(plchkk[1])
            if not len(pl[plchkk[0]]):
                pl.pop(plchkk[0])
            continue
        if not len(mostWantedPerson):
            mostWantedPerson.append(int(p))
            continue
        if len(PersonInfo[p][5]) > len(PersonInfo[mostWantedPerson[0]][5]):
            mostWantedPerson = list()
            mostWantedPerson.append(int(p))
            continue
        if len(PersonInfo[p][5]) == len(PersonInfo[mostWantedPerson[0]][5]):
            mostWantedPerson.append(int(p))
            continue
        if len(mostWantedPerson) == limitHC:
            break
    if not len(mostWantedPerson):
        return int(0)
    return list(mostWantedPerson)

##################################################################################################

# Find All Most Wanted Decreasing


def FAMWD(Count: int):
    mwc = len(Peoples) if Count == -1 else Count
    mostWantPers = list()
    mostwp = 0
    while mostwp < mwc:
        loopMw = FMWP(mostWantPers, mwc-mostwp)
        mostwp += 0 if not loopMw else len(loopMw)
        if loopMw:
            mostWantPers.append(list(loopMw))
        else:
            break
    print("%"*66)
    print("\nMost Penalty Person(s)\n")
    print("%"*66)
    pcount = 0
    for mw in range(len(mostWantPers)):
        print("*"*88)
        PenaltyNum = len(PersonInfo[mostWantPers[mw][0]][5])
        print(f"Position: {mw+1} :: Penalty: {PenaltyNum}")
        for p in mostWantPers[mw]:
            if pcount < mwc:
                PPI(p)
                pcount += 1
            else:
                break
        print("*"*88)
        if pcount >= mwc:
            break


##################################################################################################

# Request Code 1 (Q2) :: MostPositiveCoronaSubmitDay Decreasing

##################################################################################################


# Find Positive Corona Submit Count of a Day

def FPCSC(day):
    count = int(0)
    for x in range(len(CoronaTests)):
        if CoronaTests[x][2] and CoronaTests[x][0] == day:
            count += 1
        if CoronaTests[x][0] > day:
            break
    return int(count)

##################################################################################################


def mpcsChk(d: int, mpl: list):
    for dd in range(len(mpl)):
        for ddd in range(len(mpl[dd][1])):
            if mpl[dd][1][ddd] == d:
                return [dd, ddd]
    return 0

##################################################################################################

# Find Most Positive Corona Submit days


def FMPCSD(dayRange: list, mostPosCS: list, count: int):
    mpcs = copy.deepcopy(mostPosCS)
    mostPosDay = list()
    mostPosDayC = 0
    for day in range(dayRange[0], dayRange[1]+1):
        mpcschk = mpcsChk(day, mpcs)
        if mpcschk:
            mpcs[mpcschk[0]][1].pop(mpcschk[1])
            if not len(mpcs[mpcschk[0]][1]):
                mpcs.pop(mpcschk[0])
            continue
        dayPosSubC = FPCSC(day)
        if not dayPosSubC:
            continue
        if not len(mostPosDay):
            mostPosDayC = int(dayPosSubC)
            mostPosDay.append(day)
            continue
        if dayPosSubC > mostPosDayC:
            mostPosDayC = int(dayPosSubC)
            mostPosDay.clear()
            mostPosDay.append(day)
            continue
        if dayPosSubC == mostPosDayC:
            mostPosDay.append(day)
        if len(mostPosDay) == count:
            break
    return int(mostPosDayC), list(mostPosDay)


##################################################################################################


# Find All Most Positive Corona Submit in a day by a range


def FAMPCS(dayrange: list, count: int):
    mpc = len(CoronaTests) if count == -1 else count
    mostPosCorSub = list()
    mostCS = 0
    while mostCS < mpc:
        dc, loopMcs = FMPCSD(dayrange, mostPosCorSub, mpc - mostCS)
        mostCS += 0 if not len(loopMcs) else len(loopMcs)
        if len(loopMcs) and dc:
            newloop = list()
            newloop.append(int(dc))
            newloop.append(copy.deepcopy(loopMcs))
            mostPosCorSub.append(copy.deepcopy(newloop))
        else:
            break
    print("%"*66)
    print("\nMost Positive Corona Submit Day(s)\n")
    print("%"*66)
    for mp in range(len(mostPosCorSub)):
        print("*"*88)
        print(
            f"Position : {mp+1} : Positive Counts : {mostPosCorSub[mp][0]} ==> Day(s) : {mostPosCorSub[mp][1]}")
        print("*"*88)

##################################################################################################

# Request Code 2 (Q3) :: MostPositiveCoronaSubmitCity Decreasing

##################################################################################################


# Find Positive Corona Submit City Count


def FPCSCC(city: int, dayrange: list):
    cpcc = 0
    for ct in range(len(CoronaTests)):
        ctday = int(CoronaTests[ct][0])
        ctcity = int(HouseHInfo[PersonInfo[CoronaTests[ct][1]][0][0]][0][0])
        if ctcity == city and dayrange[0] <= ctday <= dayrange[1] and CoronaTests[ct][2]:
            cpcc += 1
    return int(cpcc)


##################################################################################################

# Find All Most Positive Corona Submit City


def FAMPCSC(Count: int, days):
    mpcc = len(CityInfo) if Count == -1 else Count
    print(
        f"In the range of Days: {days} ==> {mpcc} Counts of Most Positive City")
    mostPosCorCity = list()
    for city in range(len(CityInfo)):
        ctCount = FPCSCC(city, days)
        if not ctCount:
            continue
        if not len(mostPosCorCity):
            mostPosCorCity.append(list())
            mostPosCorCity[0].append(int(ctCount))
            mostPosCorCity[0].append(list())
            mostPosCorCity[0][1].append(int(city))
            continue
        position = -1
        lessPos = -1
        fflag = 0
        for mp in range(len(mostPosCorCity)):
            if mostPosCorCity[mp][0] == ctCount:
                mostPosCorCity[mp][1].append(city)
                fflag = 1
                break
            if mostPosCorCity[mp][0] > ctCount:
                position = int(mp)
        if fflag:
            continue
        if position == -1:
            mostPosCorCity.insert(0, list())
            mostPosCorCity[0].append(int(ctCount))
            mostPosCorCity[0].append(list())
            mostPosCorCity[0][1].append(int(city))
            continue
        for mmp in range(position, len(mostPosCorCity)):
            if mostPosCorCity[mmp][0] < ctCount:
                lessPos = int(mmp)
                break
        if lessPos == -1:
            mostPosCorCity.insert(position+1, list())
            mostPosCorCity[position+1].append(int(ctCount))
            mostPosCorCity[position+1].append(list())
            mostPosCorCity[position+1][1].append(int(city))
            continue
        else:
            mostPosCorCity.insert(lessPos, list())
            mostPosCorCity[lessPos].append(int(ctCount))
            mostPosCorCity[lessPos].append(list())
            mostPosCorCity[lessPos][1].append(int(city))
            continue
    mostCC = 0
    mflag = 0
    print("%"*66)
    print("\nMost Positive Corona Submit City(s)\n")
    print("%"*66)
    for m in range(len(mostPosCorCity)):
        if mflag:
            break
        print("*"*88)
        print(f"Position : {m+1} :: PositiveCount = {mostPosCorCity[m][0]}")
        for c in range(len(mostPosCorCity[m][1])):
            if not mflag:
                if mostCC < mpcc:
                    PCI(mostPosCorCity[m][1][c])
                    mostCC += 1
                else:
                    mflag = 1
                    break


##################################################################################################

# Request Code 3 (Q4) :: MostInfectedDayofYear Decreasing

##################################################################################################

# Find Day Infected Count

def FIDC(day: int):
    dic = 0
    daystart = day - 7 if day > 7 else 1
    for ct in range(len(CoronaTests)):
        if CoronaTests[ct][0] < daystart:
            continue
        if CoronaTests[ct][0] > day:
            break
        if CoronaTests[ct][2] and daystart <= CoronaTests[ct][0] <= day:
            dic += 1
    return int(dic)


##################################################################################################

# Find All Most Infected Days of the Year


def FAMIDY(Count: int):
    midCount = 30 if Count == -1 else Count
    mostInfectedDays = list()
    for day in range(1, 366):
        diCount = FIDC(day)
        if not diCount:
            continue
        if not len(mostInfectedDays):
            mostInfectedDays.append(list())
            mostInfectedDays[0].append(int(diCount))
            mostInfectedDays[0].append(list())
            mostInfectedDays[0][1].append(int(day))
            continue
        position = -1
        lessPos = -1
        fflag = 0
        for mi in range(len(mostInfectedDays)):
            if mostInfectedDays[mi][0] == diCount:
                mostInfectedDays[mi][1].append(int(day))
                fflag = 1
                break
            if mostInfectedDays[mi][0] > diCount:
                position = int(mi)
        if fflag:
            continue
        if position == -1:
            mostInfectedDays.insert(0, list())
            mostInfectedDays[0].append(diCount)
            mostInfectedDays[0].append(list())
            mostInfectedDays[0][1].append(day)
            continue
        for mmi in range(position, len(mostInfectedDays)):
            if mostInfectedDays[mmi][0] < diCount:
                lessPos = int(mmi)
                break
        if lessPos == -1:
            mostInfectedDays.insert(position+1, list())
            mostInfectedDays[position+1].append(diCount)
            mostInfectedDays[position+1].append(list())
            mostInfectedDays[position+1][1].append(day)
            continue
        else:
            mostInfectedDays.insert(lessPos, list())
            mostInfectedDays[lessPos].append(diCount)
            mostInfectedDays[lessPos].append(list())
            mostInfectedDays[lessPos][1].append(day)
            continue
    mostIDC = 0
    print("%"*66)
    print("\nMost Infected Days Of Year\n")
    print("%"*66)
    for d in range(len(mostInfectedDays)):
        print("*"*88)
        days = list()
        if len(mostInfectedDays[d][1]) > (midCount - mostIDC):
            days = mostInfectedDays[d][1][:midCount-mostIDC]
        else:
            days = copy.deepcopy(mostInfectedDays[d][1])
        print(
            f"Position : {d+1} :: Infected Count = {mostInfectedDays[d][0]} at Day(s): {days}")
        mostIDC += len(days)
        if mostIDC >= midCount:
            break


##################################################################################################

# Request Code 4 (Q5) :: BountyCounterOftheDay

##################################################################################################

# Reverse Function Bounty

def RFB(day: int, prt: int):
    today(1)
    # Persons Size , Houses Size , Cities Size
    FTPS(100, 30, 30)
    # City Random Inforamtion Feed
    CRIF(prt)
    if prt:
        print('='*111)
    # Corona Test Random Submit #arg1 = Count , #arg2 = (0 --> Negative :: 1 --> Positive :: 2 --> Random)
    CTRIF(30, 2, prt)
    if prt:
        print('='*111)
    # Traffic Event Random Feed #arg1 = Count , #arg2 = print , #arg3 = boldDay
    TERF(30, prt, day)

##################################################################################################


# Find BountyCounterOftheDay

def FBCOD(day: int):
    Tresspassers = list()
    penCount = 0
    for pen in range(len(Penalties)):
        if Penalties[pen][0] == day:
            if Penalties[pen][1] in Tresspassers:
                continue
            Tresspassers.append(Penalties[pen][1])
            penCount += 1
        else:
            if Penalties[pen][0] < day:
                continue
            else:
                break
    print("%"*66)
    print("\nBounty Of the Day\n")
    print("%"*66)
    print(f"The Bounty Of Day : {day} is {penCount} Person(s).")


##################################################################################################

# Request Code 5 (Q6) :: BillBountyofaPerson

##################################################################################################

# Find Bill Bounty of a Infected

def FBBI(person: int):
    return len(PersonInfo[person][6])

# Find All Bill Bounty Persons


def FABBP(Person: int):
    print("%"*66)
    print("\nBill Counts Of An Infected\n")
    print("%"*66)
    if Person == -1:
        for p in range(len(PersonInfo)):
            billen = FBBI(p)
            if billen:
                print(f"\nPerson : {Peoples[p]} has {billen} Submit Bill!")
    else:
        billen = FBBI(Person)
        print(f"Person : {Peoples[Person]} has {billen} Submit Bill!")


##################################################################################################

# Request Code 6 (Q7) :: SumOfAllTresspassersInADateRange

##################################################################################################

# Find Tresspasser Counts in a date range

def FTCIDR(days: list):
    Tresspassers = list()
    tpCount = 0
    for pen in range(len(Penalties)):
        if days[0] <= Penalties[pen][0] <= days[1]:
            if Penalties[pen][1] in Tresspassers:
                continue
            Tresspassers.append(Penalties[pen][1])
            tpCount += 1
        else:
            if Penalties[pen][0] < days[0]:
                continue
            if Penalties[pen][0 > days[1]]:
                break
    print("%"*66)
    print(f"\nTresspassers of a Date range.\n")
    print("%"*66)
    print(
        f"The Tresspassers Of the Day : {days[0]} to {days[1]} is {tpCount} Person(s).")


##################################################################################################

requestRepo = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9']


def reqRepChk(subject: str):
    for req in range(len(requestRepo)):
        if str(subject) == str(requestRepo[req]):
            return req
    return -1

##################################################################################################


def main():
    ReqCode = -1
    sysArgLen = len(sys.argv)
    if sysArgLen == 1:
        sysManual()
        sys.exit(0)
    if sysArgLen > 1:
        ReqCode = reqRepChk(str(sys.argv[1]))
        if ReqCode == -1:
            print('First Argument must be a VALID Request Code!')
            sys.exit(0)
        else:
            if ReqCode == 0:
                FLR(PrintOn)
                if sysArgLen > 2:
                    arg2 = sys.argv[2]
                    if str(arg2).isdigit():
                        if 0 < int(sys.argv[2]) <= 30:
                            pass
                        else:
                            print("Request Count must be between 1 and 30!")
                            sys.exit(0)
                    else:
                        print("Request Count Must be a Digit Number!")
                        sys.exit(0)
                    if sysArgLen > 3:
                        print("Command Not Valid!")
                        sys.exit(0)
                    else:
                        FAMWD(int(arg2))
                else:
                    FAMWD(-1)
            elif ReqCode == 1:
                FLR(PrintOn)
                if sysArgLen > 2:
                    arg2 = sys.argv[2]
                    if arg2.isdigit():
                        if 0 < int(arg2) <= 30:
                            pass
                        else:
                            print(
                                "Request Count Must be a Positive number between 1 and 30!")
                            sys.exit(0)
                    else:
                        print("Request Count Must be a Digit Number!")
                        sys.exit(0)
                    if sysArgLen > 3:
                        arg3 = sys.argv[3]
                        if arg3.isdigit():
                            if 0 < int(arg3) <= 365:
                                pass
                            else:
                                print(
                                    "Request Start Day must be between 1 and 365!")
                                sys.exit(0)
                        else:
                            print("Request Day(s) must be a Digit Number!")
                            sys.exit(0)
                        if sysArgLen > 4:
                            arg4 = sys.argv[4]
                            if arg4.isdigit():
                                if int(arg3) < int(arg4) <= 365:
                                    pass
                                else:
                                    print(
                                        "Request Stop Day must equal or larger than Start Day and Between 1 and 365!")
                                    sys.exit(0)
                            else:
                                print("Request Day(s) must be a Digit Number!")
                                sys.exit(0)
                            if sysArgLen > 5:
                                print("Command Not Valid!")
                                sys.exit(0)
                            else:
                                FAMPCS([int(arg3), int(arg4)],
                                       int(arg2))
                        else:
                            FAMPCS([int(arg3), Days[1]], int(arg2))
                    else:
                        FAMPCS(Days, int(arg2))
                else:
                    FAMPCS(Days, -1)
            elif ReqCode == 2:
                FLR(PrintOn)
                if sysArgLen > 2:
                    arg2 = sys.argv[2]
                    if arg2.isdigit():
                        if 0 < int(arg2) <= 30:
                            pass
                        else:
                            print("Request Count Must be in range 1 and 30 !")
                            sys.exit(0)
                    else:
                        print("Request Count Must be a Digit number!")
                        sys.exit(0)
                    if sysArgLen > 3:
                        arg3 = sys.argv[3]
                        if arg3.isdigit():
                            if 0 < int(arg3) <= 365:
                                pass
                            else:
                                print("Request Day(s) Must be in range 1 and 365 !")
                                sys.exit(0)
                        else:
                            print("Request Day(s) must be a Digit Number!")
                            sys.exit(0)
                        if sysArgLen > 4:
                            arg4 = sys.argv[4]
                            if arg4.isdigit():
                                if int(arg3) < int(arg4) <= 365:
                                    pass
                                else:
                                    print(
                                        "Request Stop Day must be equal or larger than Start Day in range 1 and 365!")
                                    sys.exit(0)
                            else:
                                print("Request Day(s) must be a Digit Number!")
                                sys.exit(0)
                            if sysArgLen > 5:
                                print("Command Not Valid!")
                                sys.exit(0)
                            else:
                                FAMPCSC(int(arg2), [int(arg3), int(arg4)])
                        else:
                            FAMPCSC(int(arg2), [int(arg3), int(arg3)])
                    else:
                        FAMPCSC(int(arg2), Days)
                else:
                    FAMPCSC(-1, Days)
            elif ReqCode == 3:
                FLR(PrintOn)
                if sysArgLen > 2:
                    arg2 = sys.argv[2]
                    if arg2.isdigit():
                        if 0 < int(arg2) <= 30:
                            pass
                        else:
                            print("Request Count must be in range 1 and 30 !")
                            sys.exit(0)
                    else:
                        print("Request Count Must be a Digit Number!")
                        sys.exit(0)
                    if sysArgLen > 3:
                        print("Command Not Valid!")
                        sys.exit(0)
                    else:
                        FAMIDY(int(arg2))
                else:
                    FAMIDY(-1)
            elif ReqCode == 4:
                if sysArgLen > 2:
                    arg2 = sys.argv[2]
                    if arg2.isdigit():
                        if 0 < int(arg2) <= 365:
                            RFB(int(arg2), PrintOn)
                            FBCOD(int(arg2))
                        else:
                            print("The Request Day Must be in range 1 and 365!")
                            sys.exit(0)
                    else:
                        print("The Request Day must be a Digit Number!")
                        sys.exit(0)
                else:
                    print("This Request Require Second Arguments!")
                    sys.exit(0)
            elif ReqCode == 5:
                FLR(PrintOn)
                if sysArgLen > 2:
                    arg2 = sys.argv[2]
                    if arg2.isdigit():
                        if 0 <= int(arg2) < len(Peoples):
                            pass
                        else:
                            print("Person ID out of range!")
                            sys.exit(0)
                    else:
                        print("Person ID must be a Digit Number!")
                        sys.exit(0)
                    if sysArgLen > 3:
                        print("Commad Not Valid!")
                        sys.exit(0)
                    else:
                        FABBP(int(arg2))
                else:
                    FABBP(-1)
            elif ReqCode == 6:
                FLR(PrintOn)
                if sysArgLen > 2:
                    arg2 = sys.argv[2]
                    if arg2.isdigit():
                        if 1 <= int(arg2) <= 365:
                            pass
                        else:
                            print("Resquet Start Day Must be in range 1 and 365!")
                            sys.exit(0)
                    else:
                        print("The Request Start Day Must be a Digit Number!")
                        sys.exit(0)
                    if sysArgLen > 3:
                        arg3 = sys.argv[3]
                        if arg3.isdigit():
                            if int(arg2) <= int(arg3) <= 365:
                                pass
                            else:
                                print(
                                    "The Request Stop Day Must be number in range the Start Day and 365!")
                                sys.exit(0)
                        else:
                            print("The Request Stop Day Must be a Digit Number!")
                            sys.exit(0)
                        if sysArgLen > 4:
                            print("Command Not Valid!")
                            sys.exit(0)
                        else:
                            FTCIDR([int(arg2), int(arg3)])
                    else:
                        FTCIDR([int(arg2), Days[1]])
                else:
                    FTCIDR(Days)
            elif ReqCode == 7:
                pass
            elif ReqCode == 8:
                pass
            else:
                sys.exit(0)


# MAIN Function
# Initial main()
if __name__ == "__main__":
    main()
