#CHECK NIC TYPE
def nic_sta(nic_no):
    if len(nic_no)==10:
        stat="OLD NIC"                
    elif len(nic_no)==12:
        stat="NEW NIC"                    
    else:
        stat="INVALID NIC"
    return stat
#DISPLAY THE DATE OF BIRTH
def nic_db(nic_no):
    if len(nic_no)==10:
        db=nic_no[0:2]
    elif len(nic_no)==12:
        db=nic_no[0:4]
    else:
        db="THERE IS A PROBLEM WITH YOUR NIC DATE OF BIRTH NO PLEASE CHECK"
    return db
#DISPLAY THE GENDER
def nic_gen(nic_no):
    if len(nic_no)==10 and int(nic_no[2:5])>=1 and int(nic_no[2:5])<=366:
        gen="MALE"
    elif len(nic_no)==10and int(nic_no[2:5])>=501 and int(nic_no[2:5])<=866:
        gen="FEMALE"
    elif len(nic_no)==12 and int(nic_no[4:7])>=1 and int(nic_no[4:7])<=366:
        gen="MALE"
    elif len(nic_no)==12 and int(nic_no[4:7])>=501 and int(nic_no[4:7])<=866:
        gen="FEMALE"
    else:
        gen="THERE IS A PROBLEM WITH YOUR NIC GENDER NO PLEASE CHECK"
    return gen
#CHECK VOTING STATUS
def nic_vot(nic_no):
    if len(nic_no)==10 and (nic_no[-1])=="V" or (nic_no[-1])=="v":
        vot="VOTER"
    elif len(nic_no)==10 and (nic_no[-1])=="X" or (nic_no[-1])=="x":
        vot="NON-VOTER"
    else:
        vot="THERE IS A PROBLEM WITH YOUR NIC VOTER NO PLEASE CHECK"
    return vot
        

        
        
        
    
        
    
    
        
