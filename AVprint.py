#!/usr/bin/env python
#Author: Daniel Sanchez Ambite

import wmi

wmiModule = wmi.WMI()

AV_Dictionary = {
    "MsMpEng.exe": "Defender",
    "AdAwareService.exe": "Adaware",
    "afwServ.exe": "Avast",
    "avguard.exe": "Avira", 
    "AVGSvc.exe": "AVG", 
    "bdagent.exe": "Bitdefender", 
    "BullGuardCore.exe": "BullGuard", 
    "ekrn.exe": "Eset", 
    "fshoster32.exe": "F-Secure", 
    "GDScan.exe":"G Data", 
    "avp.exe": "Kaspersky", 
    "K7CrvSvc.exe": "K7",
    "mfemms.exe": "McAffe", 
    "McAPExe.exe": "McAfee", 
    "NortonSecurity.exe": "Norton", 
    "PavFnSvr.exe": "Panda", 
    "SavService.exe": "Shopos", 
    "EnterpriseService.exe": "VIPRE", 
    "WRSA.exe": "Webroot", 
    "ZAPrivacyService.exe": "ZoneAlarm",
    "mbam.exe":"Malwarebytes"

} 

for process in wmiModule.Win32_Process():
    if process.Name in AV_Dictionary:
        print(f"[+] {AV_Dictionary[process.Name]} detected with processID: {process.ProcessID}")
