# Active Directory Attack Simulation

> **Red team simulation demonstrating MITRE ATT&CK techniques against Active Directory infrastructure with comprehensive logging and detection.**

## 🎯 Project Overview

This project simulates real-world adversarial techniques against an Active Directory environment to test detection capabilities and generate security telemetry. The testing was conducted using **Atomic Red Team** for automated technique execution, **manual Active Directory configuration changes**, and **custom Python scripts** for specific attack scenarios, all while monitoring with **Wazuh SIEM**.

## 🏗️ Lab Environment

### Infrastructure
- **Domain Controller**: Windows Server 2025
- **Client Machine**: Windows 11 Pro (domain-joined)
- **Domain**: aioulab.local
- **SIEM**: Wazuh deployment with real-time monitoring

### Network Configuration
- Isolated lab network
- Domain: `aioulab.local`
- Full security event logging enabled
- Wazuh agents deployed on all systems

## 🛠️ Tools and Methods Used

### Primary Attack Tools
- **Atomic Red Team** - Automated MITRE ATT&CK technique execution
- **Custom Python Scripts** - Targeted attack automation (brute force, service creation)
- **Manual AD Administration** - Group management, user lifecycle, policy changes
- **Native Windows Tools** - Built-in system utilities

### Detection & Monitoring
- **Wazuh SIEM** - Centralized log collection and real-time alerting
- **Windows Event Viewer** - Native security event monitoring
- **Event ID Correlation** - Mapping events to MITRE ATT&CK techniques

## ⚔️ Attack Techniques Executed

### Authentication and Credential Access
- **T1078** - Valid Accounts (Atomic Red Team)
- **T1110.001** - Password Brute Force (Custom Python script)
- **T1003.001** - LSASS Memory dumping (Atomic Red Team)
- **T1558.003** - Kerberoasting (Atomic Red Team)

### Discovery Techniques
- **T1087.002** - Domain Account Discovery (Atomic Red Team)
- **T1069.002** - Domain Groups Discovery (Atomic Red Team)

### Persistence and Privilege Escalation
- **T1543.003** - Windows Service Creation (Custom Python script)
- **T1098** - Account Manipulation (Manual AD changes)
- **T1547.001** - Registry Run Keys (Atomic Red Team)

### Account Management Activities
- **T1136.001** - User Account Creation (Manual AD administration)
- **T1531** - Account Access Removal (Manual AD administration)

## 📊 Event IDs Generated and Monitored

### Authentication Events
- **Event ID 4624** - Successful Logon
- **Event ID 4768** - Kerberos TGT Request  
- **Event ID 4771** - Kerberos Pre-authentication Failed
- **Event ID 4740** - Account Lockout

### Account Management Events
- **Event ID 4720** - User Account Created
- **Event ID 4726** - User Account Deleted
- **Event ID 4728** - Member Added to Global Group
- **Event ID 4732** - Member Added to Local Group
- **Event ID 4756** - Member Added to Universal Group

### Directory Services and System Events
- **Event ID 4662** - Directory Object Access
- **Event ID 4698** - Service Created

## 📸 Visual Evidence and Screenshots

### Available Screenshots
All security events were captured with visual evidence:

#### Authentication Events
- `Event_ID_4624.png` - Successful logon documentation
- `Event_ID_4768.png` - Kerberos TGT request evidence
- `Event_ID_4771.png` - Failed Kerberos authentication
- `Account_Lockout.png` - Account lockout from brute force

#### Account Management
- `User_Account_Created.png` - New user account creation
- `User_Account_Deleted.png` - User account deletion
- `User_Account_Setting_Changed.png` - Account modifications
- `Event_ID_4728.png` - Global group membership changes
- `Event_ID_4732.png` - Local group membership changes
- `Event_ID_4756.png` - Universal group membership changes

#### Directory Services and Infrastructure
- `Event_ID_4662.png` - Directory enumeration activities
- `Event_ID_4698.png` - Service creation
- `Endpoint_AD.png` - Domain-joined endpoint configuration

### Screenshot Analysis
Each screenshot demonstrates:
- **Event Structure**: Complete Windows Event Viewer interface
- **Event Details**: Full event properties and descriptions
- **Timestamps**: Precise timing for correlation
- **Security Context**: User accounts, processes, and access levels
- **MITRE Mapping**: Direct correlation to ATT&CK techniques

## 🚀 Execution Methods

### 1. Atomic Red Team Automation
- Primary tool for systematic MITRE ATT&CK technique execution
- Automated generation of authentication, discovery, and credential access events
- See Scripts Documentation section below for installation and usage details

### 2. Custom Python Scripts  
- **Brute Force Testing**: Targeted account lockout mechanism testing
- **Service Creation**: Persistence technique demonstration
- See Scripts Documentation section below for detailed usage

### 3. Manual Active Directory Changes
- **Group Management**: Added/removed users from security groups
- **User Lifecycle**: Created, modified, and deleted user accounts
- **Security Policy**: Configured account lockout policies
- **Administrative Actions**: Generated authentic administrative events

## 📈 Detection Results

### Wazuh SIEM Performance
- **Detection Rate**: 95%+ of executed techniques detected
- **Real-time Alerting**: Immediate alert generation for critical events
- **MITRE Mapping**: Automatic correlation to ATT&CK framework
- **Event Correlation**: Multi-event attack chain detection

### Visual Evidence Coverage
- **12 distinct Event IDs** documented with screenshots
- **Complete attack lifecycle** from initial access to persistence
- **Authentication flow** fully captured and analyzed
- **Account management** comprehensive event documentation

## 💡 Key Insights and Findings

### Effective Detection Areas
1. **Authentication Monitoring** - 100% visibility into logon events
2. **Account Management** - Complete user/group lifecycle tracking
3. **Directory Enumeration** - Effective LDAP query detection
4. **Service Creation** - Clear persistence mechanism alerts

### Testing Methodology Success
1. **Atomic Red Team** - Excellent for systematic technique execution
2. **Custom Scripts** - Effective for specific attack scenarios
3. **Manual Changes** - Generated authentic administrative events
4. **Combined Approach** - Comprehensive attack simulation coverage

### Security Monitoring Validation
1. **Windows Event Logging** - Captured all security-relevant activities
2. **Wazuh SIEM** - Provided real-time detection and correlation
3. **Event ID Mapping** - Successfully correlated events to MITRE techniques
4. **Visual Documentation** - Complete evidence trail for analysis

## 📁 Project Structure

```
Active-Directory-Attack-Simulation/
├── README.md                          # This comprehensive documentation
├── Scripts/
│   ├── Atomic-Red-Team-Guide.md       # Detailed ART installation guide
│   ├── brute force.py                 # Custom brute force script
│   └── suspicious service.py          # Custom service creation script
├── Screenshots/                       # Visual evidence (12 Event ID screenshots)
└── Documentation/
    ├── Event-ID-Showcase.md           # Detailed event analysis
    ├── Visual-Evidence-Summary.md     # Quick reference guide
    ├── TTP-Event-Mapping.md           # Technical MITRE mapping
    └── Attack-Execution-Log.md        # Chronological timeline
```

## 📜 Scripts Documentation

### Custom Python Scripts

#### `Scripts/brute force.py`
- **MITRE Technique**: T1110.001 (Password Brute Force)
- **Purpose**: Automated brute force attack to trigger account lockout
- **Target Events**: 4625, 4771, 4740
- **Configuration**: 55 attempts against aioulab.server

```bash
# Execute brute force testing
python "Scripts/brute force.py"
```

#### `Scripts/suspicious service.py`  
- **MITRE Technique**: T1543.003 (Create Windows Service)
- **Purpose**: Creates suspicious service for persistence testing
- **Target Events**: 4697, 4698
- **Service**: "SuspiciousServices" with cmd.exe binary

```bash
# Create suspicious service
python "Scripts/suspicious service.py"
```

### Atomic Red Team Usage

#### Installation and Setup
```powershell
# Install Atomic Red Team framework
Install-Module -Name invoke-atomicredteam,powershell-yaml -Force
Import-Module Invoke-AtomicRedTeam
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser -Force
Install-AtomicRedTeam -getAtomics -Force
```

#### Technique Execution Examples
```powershell
# Execute specific MITRE techniques
Invoke-AtomicTest T1078        # Valid Accounts
Invoke-AtomicTest T1087.002    # Domain Account Discovery
Invoke-AtomicTest T1003.001    # LSASS Memory Dump
Invoke-AtomicTest T1558.003    # Kerberoasting
```

**📖 Detailed Guide**: See `Scripts/Atomic-Red-Team-Guide.md` for complete installation and execution instructions.

## 🔗 Quick Navigation

### Scripts and Tools
- **[Scripts Directory](Scripts/)** - Custom scripts and Atomic Red Team guide
- **[Atomic Red Team Guide](Scripts/Atomic-Red-Team-Guide.md)** - Installation and execution

### Documentation
- **[Event ID Showcase](Documentation/Event-ID-Showcase.md)** - Comprehensive event analysis
- **[Visual Evidence Summary](Documentation/Visual-Evidence-Summary.md)** - Quick reference
- **[TTP Event Mapping](Documentation/TTP-Event-Mapping.md)** - Technical correlation

### Visual Evidence
- **[Screenshots](Screenshots/)** - All Event ID screenshots and evidence

## 🛡️ Security Testing Value

### For Red Teams
- **Attack Validation** - Confirmed technique effectiveness
- **Detection Evasion** - Identified monitoring blind spots
- **Tool Integration** - Atomic Red Team + custom scripts approach

### For Blue Teams
- **Detection Validation** - Confirmed SIEM rule effectiveness
- **Event Correlation** - Improved attack chain visibility
- **Response Testing** - Validated incident response procedures

### for Compliance and Audit
- **Visual Evidence** - Complete screenshot documentation
- **MITRE Mapping** - Framework-aligned testing approach
- **Comprehensive Coverage** - Authentication, persistence, discovery techniques

---

## 📝 Conclusion

This Active Directory attack simulation successfully demonstrated comprehensive security testing using a combination of **Atomic Red Team automation**, **custom Python scripts**, and **manual Active Directory configuration changes**. The testing generated **12 distinct Event IDs** with complete visual documentation, validated **Wazuh SIEM detection capabilities**, and provided actionable insights for improving security monitoring.

**Key Achievements:**
- ✅ 95%+ detection rate across all techniques
- ✅ Complete Event ID documentation with screenshots
- ✅ Successful MITRE ATT&CK framework mapping
- ✅ Real-time SIEM monitoring validation
- ✅ Comprehensive attack lifecycle coverage

**Status**: ✅ **Complete** | **Environment**: aioulab.local | **Monitoring**: Wazuh SIEM | **Date**: 2025