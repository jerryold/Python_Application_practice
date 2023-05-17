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
            'COMPARE': 17,
            'DATASET_MANAGEMENT': 18,
            'DEVICE_SELF_TEST': 19,
            'FLUSH': 20,
            'FORMAT_NVM': 21,
            'FUSED': 22,
            'GET_FEATURES': 23,
            'GETLOGPAGE': 24,
            'HOST_MEMORY_BUFFER': 30,
            'META_DATA': 53,
            'READ': 54,
            'RESET': 62,
            'RO_MODE': 63,
            'RPMB': 64,
            'SANITIZE': 65,
            'SPECIAL_FLUSH': 85,
            'VERIFY': 86,
            'WRITE': 87,
            'WRITE_UNCORRECTABLE': 88,
            'WRITE_ZEROES': 89,
            'IDENTIFY': 90,
            'DOWNLOAD': 91,
            'BOOT_PARTITION': 92,
            'CREDEL_CQSQ': 93,
            
}

function_to_index_divide = {
            'AEVRQ_CM': 2,
            'AEVRQ_ID': 3,
            'AEVRQ_SF': 4,
            'SEC_DBM': 5,
            'SEC_DPA': 6,
            'SEC_EPR': 7,
            'SEC_ERU': 8,
            'SEC_FZL': 9,
            'SEC_FZM': 10,
            'SEC_KAKO': 11,
            'SEC_LKM': 12,
            'SEC_SPA': 13,
            'SEC_STS': 14,
            'SEC_ULK': 15,
            'SEC_ULM': 16,
            'HCTM_GLP_': 25,
            'HCTM_POR_': 26,
            'HCTM_SET_': 27,
            'HCTM_THR_': 28,
            'HCTM_XG': 29,
            'CTRLREG_': 31,
            'PCICAPER': 32,
            'PCICAPEX': 33,
            'PCICAPMS': 34,
            'PCICAPPM': 35,
            'PCICAPSX': 36,
            'PCICAPVP': 37,
            'PCICAPXX': 38,
            'PCIE': 40,
            'PCIEDLINKEXT': 41,
            'PCIEDSN': 42,
            'PCIELINK': 43,
            'PCIELMR': 44,
            'PCIELTR': 45,
            'PCIEMSI': 46,
            'PCIETPH': 47,
            'PCIE_VPD': 48,
            'PCIHEAD': 49,
            'LPMNVMe_': 50,
            'LPMNVMe_SMART': 51,
            'LPMPCIe_': 52,
            'RSVN_ACQR': 55,
            'RSVN_HOST': 56,
            'RSVN_LP': 57,
            'RSVN_MUNS': 58,
            'RSVN_REGI': 59,
            'RSVN_REL_': 60,
            'RSVN_RPRT': 61,
            'SETFAPST': 66,
            'SETFARBT': 67,
            'SETFAWUN': 68,
            'SETFERRE': 69,
            'SETFILLG': 70,
            'SETFINCL': 71,
            'SETFINVC': 72,
            'SETFLRTP': 73,
            'SETFNOQ': 74,
            'SETFNPSC': 75,
            'SETFNSID': 76,
            'SETFPWMT': 77,
            'SETFSAVE': 78,
            'SETFSNTZ': 79,
            'SETFSPMK': 80,
            'SETFSRDC': 81,
            'SETFTEMP': 82,
            'SETFTSTP': 83,
            'SETFVWTC': 84,            

}



# function_to_index = {
#             'ABORT': 1,
#             'AEVRQ': 2,
#             'ATA_SECURITY': 3,
#             'BOOT_PARTITION': 4,
#             'COMPARE': 5,
#             'CREDEL_CQSQ': 6,
#             'DATASET_MANAGEMENT': 7,
#             'DEVICE_SELF_TEST': 8,
#             'DIRECTIVES\SinglePort': 9,
#             'DIRECTIVES\DualPort': 9,
#             'DIRECTIVES_MULTINS\SinglePort': 10,
#             'DIRECTIVES_MULTINS\DualPort': 10,
#             'DOWNLOAD': 11,
#             'DUAL_PORT': 12,
#             'ERROR_PRIORITY_REPORT': 13,
#             'FLUSH': 14,
#             'FORMAT_NVM': 15,
#             'FUSED': 16,
#             'GET_FEATURES': 17,
#             'GETLOGPAGE': 18,
#             'HOST_CONTROLLED_THERMAL_MANAGEMENT': 19,
#             'HOST_MEMORY_BUFFER': 20,
#             'IDENTIFY': 21,
#             'LOW_POWER_MODE': 22,
#             'META_DATA': 23,
#             'MULTI_NAMESPACE': 24,
#             'MULTI_NAMESPACE_DUAL': 25,
#             'NAMESPACE_ATTACHMENT': 26,
#             'NAMESPACE_MANAGEMENT': 27,
#             'PCIE_REGISTER': 28,
#             'PI': 29,
#             'READ': 30,
#             'RESERVATION': 31,
#             'RESET': 32,
#             'RO_MODE': 33,
#             'RPMB': 34,
#             'SANITIZE': 35,
#             'SET_FEATURES': 36,
#             'SMBUS': 37,
#             'SPECIAL_FLUSH': 38,
#             'VERIFY': 39,
#             'WRITE': 40,
#             'WRITE_UNCORRECTABLE': 41,
#             'WRITE_ZEROES': 42
# }

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
              
                if folder+f1+"/"+f2=="./datasets/train1/AEVRQ":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                
                elif folder+f1+"/"+f2=="./datasets/train1/ATA_SECURITY":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                elif folder+f1+"/"+f2=="./datasets/train1/HOST_CONTROLLED_THERMAL_MANAGEMENT":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train1/PCIE_REGISTER":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                elif folder+f1+"/"+f2=="./datasets/train1/LOW_POWER_MODE":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train1/RESERVATION":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train1/SET_FEATURES":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                
                
                else :
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
                if folder+f1+"/"+f2=="./datasets/train2/AEVRQ":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                
                elif folder+f1+"/"+f2=="./datasets/train2/ATA_SECURITY":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                elif folder+f1+"/"+f2=="./datasets/train2/HOST_CONTROLLED_THERMAL_MANAGEMENT":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train2/PCIE_REGISTER":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                elif folder+f1+"/"+f2=="./datasets/train2/LOW_POWER_MODE":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train2/RESERVATION":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train2/SET_FEATURES":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                
                
                else :
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
           
           
            if folder+f1 == "./datasets/train_21":
              
                if folder+f1+"/"+f2=="./datasets/train_21/AEVRQ":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                
                elif folder+f1+"/"+f2=="./datasets/train_21/ATA_SECURITY":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                elif folder+f1+"/"+f2=="./datasets/train_21/HOST_CONTROLLED_THERMAL_MANAGEMENT":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train_21/PCIE_REGISTER":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                elif folder+f1+"/"+f2=="./datasets/train_21/LOW_POWER_MODE":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train_21/RESERVATION":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train_21/SET_FEATURES":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                
                
                else :
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
            elif folder+f1 == "./datasets/train_23":

              
                if folder+f1+"/"+f2=="./datasets/train_23/AEVRQ":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                
                elif folder+f1+"/"+f2=="./datasets/train_23/ATA_SECURITY":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                elif folder+f1+"/"+f2=="./datasets/train_23/HOST_CONTROLLED_THERMAL_MANAGEMENT":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train_23/PCIE_REGISTER":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                elif folder+f1+"/"+f2=="./datasets/train_23/LOW_POWER_MODE":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train_23/RESERVATION":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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

                elif folder+f1+"/"+f2=="./datasets/train_23/SET_FEATURES":                       
                
                    
                    function = re.split('(\d.*)',f3)
                    
                    data = {
                        "model": model,
                        "fw": fw,
                        "function":function_to_index_divide[function[0]],
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
                
                
                else :
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


with open('train_all(category).csv', 'w',newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)






# In[ ]:




