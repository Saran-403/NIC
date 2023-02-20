import nic_func

#Input 
nic_no= input(" Enter The NIC Number :")

#Current NIC STATUS
print("YOUR NIC TYPE : ",nic_func.nic_sta(nic_no))

#Age
print("YOU WERE BORN ON : " ,nic_func.nic_db(nic_no))

#Gender
print("YOU ARE A",nic_func.nic_gen(nic_no))

#Voter
print("YOR ARE A",nic_func.nic_vot(nic_no))

