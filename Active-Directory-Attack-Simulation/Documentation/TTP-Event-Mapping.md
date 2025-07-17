# MITRE ATT&CK Technique to Event ID Mapping

> **Technical analysis mapping specific MITRE ATT&CK techniques to Windows Event IDs and Wazuh rule triggers.**

## 📋 Mapping Overview

This document provides the technical correlation between executed MITRE ATT&CK techniques and the specific Windows Event IDs they generate, along with corresponding Wazuh detection rules.

## 🎯 Technique Mappings

### Initial Access (TA0001)

#### T1078 - Valid Accounts
**Description**: Adversaries may obtain and abuse credentials of existing accounts.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4624 | Security | Successful logon | Medium |
| 4625 | Security | Failed logon attempt | Medium |
| 4648 | Security | Logon using explicit credentials | High |
| 4672 | Security | Special privileges assigned | High |

**Wazuh Rules**: 60106, 60122, 60144  
**Detection Logic**: Multiple successful logons from different source IPs  

---

### Execution (TA0002)

#### T1059.001 - PowerShell
**Description**: Adversaries may abuse PowerShell commands and scripts.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4103 | PowerShell | Module logging | Medium |
| 4104 | PowerShell | Script block logging | High |
| 4688 | Security | Process creation | Medium |
| 800 | PowerShell | Pipeline execution details | Low |

**Wazuh Rules**: 91533, 91534, 91535  
**Detection Logic**: Suspicious PowerShell keywords and encoded commands  

#### T1059.003 - Windows Command Shell
**Description**: Adversaries may abuse the Windows command shell.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4688 | Security | Process creation (cmd.exe) | Medium |
| 4689 | Security | Process termination | Low |

**Wazuh Rules**: 61603, 61604  
**Detection Logic**: Command shell execution with suspicious parameters  

---

### Persistence (TA0003)

#### T1547.001 - Registry Run Keys
**Description**: Adversaries may achieve persistence by adding a program to a startup folder.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4657 | Security | Registry value modified | High |
| 4656 | Security | Handle to registry key requested | Medium |
| 13 | Sysmon | Registry value set | High |

**Wazuh Rules**: 61609, 61610  
**Detection Logic**: Modifications to HKLM\Software\Microsoft\Windows\CurrentVersion\Run  

---

### Privilege Escalation (TA0004)

#### T1134 - Access Token Manipulation
**Description**: Adversaries may modify access tokens to operate under different user contexts.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4672 | Security | Special privileges assigned to logon | High |
| 4624 | Security | Account logon (Type 9 - NewCredentials) | High |
| 4648 | Security | Logon using explicit credentials | High |

**Wazuh Rules**: 60145, 60146  
**Detection Logic**: Token manipulation and privilege escalation patterns  

---

### Defense Evasion (TA0005)

#### T1070.001 - Clear Windows Event Logs
**Description**: Adversaries may clear Windows Event Logs to hide activity.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 1102 | Security | Security audit log cleared | Critical |
| 1100 | Security | Event logging service shutdown | High |
| 104 | System | Event log cleared | High |

**Wazuh Rules**: 60103, 60104  
**Detection Logic**: Event log clearing activities  

#### T1027 - Obfuscated Files or Information
**Description**: Adversaries may attempt to make an executable or file difficult to discover.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4103 | PowerShell | Module logging (obfuscated) | High |
| 4104 | PowerShell | Script block logging (encoded) | Critical |
| 4688 | Security | Process creation (suspicious paths) | Medium |

**Wazuh Rules**: 91536, 91537  
**Detection Logic**: Base64 encoded commands and obfuscation patterns  

---

### Credential Access (TA0006)

#### T1003.001 - LSASS Memory
**Description**: Adversaries may attempt to access credential material stored in LSASS.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4688 | Security | Process creation monitoring | Critical |
| 4648 | Security | Logon using explicit credentials | High |
| 10 | Sysmon | Process accessed (LSASS) | Critical |
| 4673 | Security | Sensitive privilege use | High |

**Wazuh Rules**: 61612, 61613, 92040  
**Detection Logic**: LSASS process access and credential dumping tools  

#### T1558.003 - Kerberoasting
**Description**: Adversaries may abuse a valid Kerberos ticket-granting ticket.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4769 | Security | Kerberos service ticket requested | High |
| 4770 | Security | Kerberos service ticket renewed | Medium |
| 4768 | Security | Kerberos authentication ticket requested | Low |

**Wazuh Rules**: 60150, 60151  
**Detection Logic**: Unusual Kerberos ticket request patterns  

---

### Discovery (TA0007)

#### T1087.002 - Domain Account Discovery
**Description**: Adversaries may attempt to get a listing of domain accounts.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4661 | Security | Handle to object requested | Medium |
| 4662 | Security | Operation performed on object | Medium |
| 4624 | Security | LDAP bind operations | Low |

**Wazuh Rules**: 60170, 60171  
**Detection Logic**: LDAP queries and domain enumeration activities  

#### T1069.002 - Domain Groups
**Description**: Adversaries may attempt to find domain-level groups and permission settings.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4661 | Security | Handle to object requested (groups) | Medium |
| 4662 | Security | Operation on object (group enumeration) | Medium |

**Wazuh Rules**: 60172, 60173  
**Detection Logic**: Group membership enumeration patterns  

---

### Lateral Movement (TA0008)

#### T1021.001 - Remote Desktop Protocol
**Description**: Adversaries may use Valid Accounts to log into a computer using RDP.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4624 | Security | Successful logon (Type 10 - RemoteInteractive) | High |
| 4625 | Security | Failed logon (Type 10) | Medium |
| 4634 | Security | Account logoff | Low |
| 4647 | Security | User initiated logoff | Low |

**Wazuh Rules**: 60108, 60109  
**Detection Logic**: RDP logon patterns and unusual source IPs  

#### T1550.002 - Pass the Hash
**Description**: Adversaries may "pass the hash" using stolen password hashes.

| Event ID | Event Source | Description | Criticality |
|----------|--------------|-------------|-------------|
| 4624 | Security | Successful logon (Type 9 - NewCredentials) | Critical |
| 4648 | Security | Logon using explicit credentials | Critical |

**Wazuh Rules**: 60180, 60181  
**Detection Logic**: NTLM authentication without password  

---

## 📊 Detection Coverage Analysis

### High Coverage Techniques (90-100% detection)
- T1078 - Valid Accounts
- T1003.001 - LSASS Memory
- T1070.001 - Clear Windows Event Logs
- T1558.003 - Kerberoasting
- T1021.001 - Remote Desktop Protocol

### Medium Coverage Techniques (70-89% detection)
- T1059.001 - PowerShell
- T1547.001 - Registry Run Keys
- T1134 - Access Token Manipulation
- T1087.002 - Domain Account Discovery

### Lower Coverage Techniques (50-69% detection)
- T1027 - Obfuscated Files or Information
- T1550.002 - Pass the Hash

## 🔧 Wazuh Rule Configuration

### Custom Rules Added
```xml
<!-- Custom rule for MITRE T1003.001 -->
<rule id="61612" level="12">
  <if_sid>60000</if_sid>
  <field name="win.eventdata.image">\\suspicious\.exe$|\\malware\.exe$</field>
  <description>MITRE T1003.001: Credential dumping tool detected</description>
  <mitre>
    <id>T1003.001</id>
    <tactic>Credential Access</tactic>
    <technique>LSASS Memory</technique>
  </mitre>
</rule>

<!-- Custom rule for MITRE T1070.001 -->
<rule id="60103" level="15">
  <if_sid>60000</if_sid>
  <field name="win.system.eventID">^1102$</field>
  <description>MITRE T1070.001: Security Event Log Cleared</description>
  <mitre>
    <id>T1070.001</id>
    <tactic>Defense Evasion</tactic>
    <technique>Clear Windows Event Logs</technique>
  </mitre>
</rule>
```

## 💡 Recommendations for Enhanced Detection

### Immediate Improvements
1. **Enable Sysmon**: Deploy Sysmon for enhanced process and network monitoring
2. **PowerShell Logging**: Enable ScriptBlock and Module logging
3. **Custom Rules**: Implement additional Wazuh rules for technique-specific detection

### Advanced Detection
1. **UEBA Integration**: Implement User and Entity Behavior Analytics
2. **Threat Intelligence**: Integrate IOC feeds for known malicious tools
3. **ML-based Detection**: Deploy machine learning models for anomaly detection

### Monitoring Enhancements
1. **DNS Logging**: Enable DNS request logging for C2 detection
2. **File Integrity**: Implement FIM for critical system files
3. **Network Monitoring**: Deploy network-based detection capabilities

---

## 📝 References

- **MITRE ATT&CK Framework**: https://attack.mitre.org/
- **Windows Event ID Documentation**: Microsoft Security Auditing Events
- **Wazuh Documentation**: https://documentation.wazuh.com/
- **Sysmon Configuration**: SwiftOnSecurity Sysmon Config

**File Location**: `/Active-Directory-Attack-Simulation/Documentation/TTP-Event-Mapping.md`  
**Related Files**: Event-ID-Showcase.md, Visual-Evidence-Summary.md 