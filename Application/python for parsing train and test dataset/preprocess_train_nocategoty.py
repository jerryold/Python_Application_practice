#!/usr/bin/env python
# coding: utf-8

# In[1]:


from os import listdir
from os.path import isdir, isfile
import pandas as pd
import json
import csv
import re


# In[2]:


all_data = []

folder = "./datasets/"
filename = "pb999-99a_nvmecore_log.txt"



function_to_index = {
            'ABORT': 1,
            'AEVRQ': 2,
            'ATA_SECURITY': 3,
            'BOOT_PARTITION': 4,
            'COMPARE': 5,
            'CREDEL_CQSQ': 6,
            'DATASET_MANAGEMENT': 7,
            'DEVICE_SELF_TEST': 8,
            'DIRECTIVES\SinglePort': 9,
            'DIRECTIVES\DualPort': 9,
            'DIRECTIVES_MULTINS\SinglePort': 10,
            'DIRECTIVES_MULTINS\DualPort': 10,
            'DOWNLOAD': 11,
            'DUAL_PORT': 12,
            'ERROR_PRIORITY_REPORT': 13,
            'FLUSH': 14,
            'FORMAT_NVM': 15,
            'FUSED': 16,
            'GET_FEATURES': 17,
            'GETLOGPAGE': 18,
            'HOST_CONTROLLED_THERMAL_MANAGEMENT': 19,
            'HOST_MEMORY_BUFFER': 20,
            'IDENTIFY': 21,
            'LOW_POWER_MODE': 22,
            'META_DATA': 23,
            'MULTI_NAMESPACE': 24,
            'MULTI_NAMESPACE_DUAL': 25,
            'NAMESPACE_ATTACHMENT': 26,
            'NAMESPACE_MANAGEMENT': 27,
            'PCIE_REGISTER': 28,
            'PI': 29,
            'READ': 30,
            'RESERVATION': 31,
            'RESET': 32,
            'RO_MODE': 33,
            'RPMB': 34,
            'SANITIZE': 35,
            'SET_FEATURES': 36,
            'SMBUS': 37,
            'SPECIAL_FLUSH': 38,
            'VERIFY': 39,
            'WRITE': 40,
            'WRITE_UNCORRECTABLE': 41,
            'WRITE_ZEROES': 42
}

for f1 in listdir(folder):
    
    if isdir(folder+f1) == False:
        continue
    
    for f2 in listdir(folder+f1):     
        
        if isdir(folder+f1+"/"+f2) == False:
            continue
            

        for f3 in listdir(folder+f1+"/"+f2):
            
            
            model = ""
            fw = ""
            fw_id=""
            function = ""
            op = ""
            status = ""
            opstaus=""
            cdw10_f = ""
            cdw11_f = ""
            cdw12_f = ""            
            cdw13_f = ""
            cdw14_f = ""
            cdw15_f = ""
            cdw10_b = ""
            cdw11_b = ""
            cdw12_b = ""
            cdw13_b = ""
            cdw14_b = ""
            cdw15_b = ""
            
            if isdir(folder+f1+"/"+f2+"/"+f3) == False or f3 == ".ipynb_checkpoints":
                continue

            
            with open(folder+f1+"/"+f2+"/"+f3+"/"+filename, 'r') as f:
                

                line = f.readlines()
                parts=re.split('(\d.*)',f3)
                print(parts[0])
                
                
                
           
            for i in range(0, len(line)):
                if "<<Command>>" in line[i].strip():
                    line1 = line[i].strip()
                    
                    if "AdOP=" in line1:
                        op += "0 "
                        opstaus += line1[line1.find("AdOP=")+5:line1.find("AdOP=")+7].strip()+ " "
                        cdw10_f += line1[line1.find("CDW10=")+6:line1.find("CDW10=")+10].strip()+ " "
                        cdw10_b += line1[line1.find("CDW10=")+10:line1.find("CDW11=")].strip()+ " "                        
                        cdw11_f += line1[line1.find("CDW11=")+6:line1.find("CDW11=")+10].strip()+ " "
                        cdw11_b += line1[line1.find("CDW11=")+10:line1.find("CDW12=")].strip()+ " "                        
                        cdw12_f += line1[line1.find("CDW12=")+6:line1.find("CDW12=")+10].strip()+ " "
                        cdw12_b += line1[line1.find("CDW12=")+10:line1.find("CDW13=")].strip()+ " "                        
                        cdw13_f += line1[line1.find("CDW13=")+6:line1.find("CDW13=")+10].strip()+ " "
                        cdw13_b += line1[line1.find("CDW13=")+10:line1.find("CDW14=")].strip()+ " "                        
                        cdw14_f += line1[line1.find("CDW14=")+6:line1.find("CDW14=")+10].strip()+ " "
                        cdw14_b += line1[line1.find("CDW14=")+10:line1.find("CDW15=")].strip()+ " "                        
                        cdw15_f += line1[line1.find("CDW15=")+6:line1.find("CDW15=")+10].strip()+ " "
                        cdw15_b += line1[line1.find("CDW15=")+10:line1.find("CDW15=")+14].strip()+ " "
                        
                    elif "NvOP" in line1:
                        op += "1 "
                        opstaus += line1[line1.find("NvOP=")+5:line1.find("NvOP=")+7].strip()+ " "
                        cdw10_f += line1[line1.find("CDW10=")+6:line1.find("CDW10=")+10].strip()+ " "
                        cdw10_b += line1[line1.find("CDW10=")+10:line1.find("CDW11=")].strip()+ " "                        
                        cdw11_f += line1[line1.find("CDW11=")+6:line1.find("CDW11=")+10].strip()+ " "
                        cdw11_b += line1[line1.find("CDW11=")+10:line1.find("CDW12=")].strip()+ " "                        
                        cdw12_f += line1[line1.find("CDW12=")+6:line1.find("CDW12=")+10].strip()+ " "
                        cdw12_b += line1[line1.find("CDW12=")+10:line1.find("CDW13=")].strip()+ " "                        
                        cdw13_f += line1[line1.find("CDW13=")+6:line1.find("CDW13=")+10].strip()+ " "
                        cdw13_b += line1[line1.find("CDW13=")+10:line1.find("CDW14=")].strip()+ " "                        
                        cdw14_f += line1[line1.find("CDW14=")+6:line1.find("CDW14=")+10].strip()+ " "
                        cdw14_b += line1[line1.find("CDW14=")+10:line1.find("CDW15=")].strip()+ " "                        
                        cdw15_f += line1[line1.find("CDW15=")+6:line1.find("CDW15=")+10].strip()+ " "
                        cdw15_b += line1[line1.find("CDW15=")+10:line1.find("CDW15=")+14].strip()+ " "

                    
                    
                if "Pass" in line[i].strip():
                    status = 'Pass'
                elif "Fail" in line[i].strip():
                    status = 'Fail'
                elif "Skip" in line[i].strip():
                    status = 'Skip'
                    
                if "ModelNumber" in line[i].strip():
                    model = line[i].split(":")[1].strip()
                
                if "FirmRevision" in line[i].strip():
                    fw = line[i].split(":")[1].strip()

            if model == "" or fw == "":
                continue
            
            
            
            if folder+f1 == "./datasets/train1":                              
                
                    function1 = f2
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index[function1],
                        "op": op.strip(),
                        "opstatus":opstaus.strip(),
                        "cdw10_f": cdw10_f.strip(),
                        "cdw10_b": cdw10_b.strip(),
                        "cdw11_f": cdw11_f.strip(),
                        "cdw11_b": cdw11_b.strip(),
                        "cdw12_f": cdw12_f.strip(),
                        "cdw12_b": cdw12_b.strip(),
                        "cdw13_f": cdw13_f.strip(),
                        "cdw13_b": cdw13_b.strip(),
                        "cdw14_f": cdw14_f.strip(),
                        "cdw14_b": cdw14_b.strip(),
                        "cdw15_f": cdw15_f.strip(),
                        "cdw15_b": cdw15_b.strip(),                
                        "status": status
                    }
                
            elif folder+f1 == "./datasets/train2":                              
                
                    function1 = f2
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index[function1],
                        "op": op.strip(),
                        "opstatus":opstaus.strip(),
                        "cdw10_f": cdw10_f.strip(),
                        "cdw10_b": cdw10_b.strip(),
                        "cdw11_f": cdw11_f.strip(),
                        "cdw11_b": cdw11_b.strip(),
                        "cdw12_f": cdw12_f.strip(),
                        "cdw12_b": cdw12_b.strip(),
                        "cdw13_f": cdw13_f.strip(),
                        "cdw13_b": cdw13_b.strip(),
                        "cdw14_f": cdw14_f.strip(),
                        "cdw14_b": cdw14_b.strip(),
                        "cdw15_f": cdw15_f.strip(),
                        "cdw15_b": cdw15_b.strip(),                
                        "status": status
                    }
           
            

           
            all_data.append(data)
           
            
json_string = json.dumps(all_data)





data = json.loads(json_string)
headers = data[0].keys()


with open('train_all(nocategory).csv', 'w',newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)






# In[ ]:




