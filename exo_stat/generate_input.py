#! /usr/bin/env python
from __future__ import print_function, unicode_literals
import os
import numpy as np
import random
global r_power_E
global r_deployed
global r_flow
global c_inv
global wr_inv


fco_sheet = ['Data-Front End', 'Data-Reactor', 'Data-Recycle', 'Data-Inventories', 'Data-Economics', 'Data-Wildcard', 'Graph_Data', 'Settings', 'Pres_Graphs', 'Graphs (C1-4)', 'Version Notes']

#Half-life > 1h
nucs_Pu_list = [ "238pu", "239pu", "240pu", "241pu", "242pu"]

nucs_U = "230U,231U,232U,233U,234U,235U,236U,237U,238U,240U"
nucs_Pu = "234Pu,235Pu,236Pu,237Pu,238Pu,239Pu,240Pu,241Pu,242Pu,243Pu,244Pu,245Pu,246Pu,247Pu"
nucs_Am = "239Am,240Am,241Am,242Am,243Am,244Am,245Am"
nucs_Cm = "238Cm,240Cm,241Cm,242Cm,243Am,244Cm,245Cm,246Cm,247Cm,248Cm,250Cm"
nucs_Np = "234Np,235Np,236Np,237Np,238Np,239Np"
nucs_FP = "H3,GE74,AS75,GE76,SE77,SE78,SE79,SE80,BR81,SE82,KR82,KR83,KR84,KR85,RB85,KR86,SR86,RB87,SR88,SR89,Y89,SR90,ZR90,SR91,Y91,ZR91,ZR92,Y93,ZR93,ZR94,ZR95,NB95,MO95,ZR96,MO96,ZR97,MO97,MO98,MO99,TC99,TC99M,MO100,RU100,RU101,RU102,RU103,RH103,RU104,PD104,RU105,RH105,PD105,RU106,PD106,PD107,PD108,PD109,AG109,PD110,AG110,CD110,AG111,CD111,CD112,CD113,CD113,CD114,IN115,SN115,CD116,SN116,SN117,SN118,SN119,SN120,SB121,SN122,TE122,SN123,SB123,SN124,SB124,TE124,SN125,SB125,TE125,TE125,SN126,TE126,SB127,TE127,I127,TE128,XE128,TE129,I129,TE130,XE130,TE131,I131,XE131,XE131,TE132,I132,XE132,I133,XE133,XE133,CS133,XE134,CS134,BA134,I135,XE135,CS135,BA135,XE136,CS136,BA136,CS137,BA137,BA138,LA138,LA139,BA140,LA140,CE140,LA141,CE141,PR141,CE142,ND142,CE143,PR143,ND143,CE144,ND144,PR145,ND145,ND146,ND147,PM147,SM147,ND148,PM148,SM148,PM149,SM149,ND150,SM150,PM151,SM151,SM152,SM153,EU153,SM154,EU154,GD154,EU155,GD155,EU156,GD156,GD157,GD158,TB159,GD160,TB160,DY160,DY161,DY162,DY163,DY164,HO165,ER166"
nucs_MA = nucs_Am + "," + nucs_Cm + "," + nucs_Np



def generate(file_number, u5_enrich, bu, power, cycle):
    os.system("cp sample.xml tmp.xml")
    
    cmd = "sed 's/U5_ENRICH/" + str(u5_enrich) + "/' tmp.xml > tmp_.xml"
    os.system(cmd)
    os.system("mv tmp_.xml tmp.xml")
    
    cmd = "sed 's/U8_ENRICH/" + str(1.-u5_enrich) + "/' tmp.xml > tmp_.xml"
    os.system(cmd)
    os.system("mv tmp_.xml tmp.xml")
    
    cmd = "sed 's/PWR_BU/" + str(bu) + "/' tmp.xml > tmp_.xml"
    os.system(cmd)
    os.system("mv tmp_.xml tmp.xml")
    
    power_cap = 0.3*power
    cmd = "sed 's/PWR_POWER_CAP/" + str(power_cap) + "/' tmp.xml > tmp_.xml"
    os.system(cmd)
    os.system("mv tmp_.xml tmp.xml")
    
    cmd = "sed 's/PWR_POWER/" + str(power) + "/' tmp.xml > tmp_.xml"
    os.system(cmd)
    os.system("mv tmp_.xml tmp.xml")
    
    cmd = "sed 's/PWR_CYCLE/" + str(cycle) + "/' tmp.xml > tmp_.xml"
    os.system(cmd)
    os.system("mv tmp_.xml input/" + str(file_number) + ".xml"  )







def main():
    iteration = 1000
    u5_min = 0.03
    u5_max = 0.05
    bu_min = 25
    bu_max = 75
    p_min = 20
    p_max = 40
    for i in range(iteration):
        u5_enrich = random.uniform(u5_min, u5_max)
        bu = random.uniform(bu_min, bu_max)
        power = random.uniform(p_min, p_max)
        cycle = int(round( bu/(power*1.e-3)/30))
        power = power*90
        print(i, " ", u5_enrich, " ", bu, " ", power, " ", cycle)
        generate(i, u5_enrich, bu, power, cycle)






main()
