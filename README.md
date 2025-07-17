# AD Endpoint and Hardening Lab

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Portfolio-blue)
![CIS Compliance](https://img.shields.io/badge/CIS%20Compliance-90%25-brightgreen)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-12%2B%20Event%20IDs-red)
![Wazuh SIEM](https://img.shields.io/badge/Wazuh-SIEM-orange)

> **Comprehensive cybersecurity lab demonstrating Active Directory attack simulation with visual evidence and endpoint hardening validation achieving high CIS compliance.**

## 🎯 Project Overview

This repository contains two interconnected cybersecurity projects that demonstrate both offensive security techniques and defensive hardening measures:

1. **Active Directory Attack Simulation** - MITRE ATT&CK technique execution with comprehensive Event ID documentation
2. **Endpoint Hardening Validation** - CIS benchmark compliance through systematic system hardening

## 🛠️ Tools & Technologies Used

### Security Tools
- **Wazuh SIEM** - Centralized logging, detection, and compliance monitoring
- **Atomic Red Team** - Automated MITRE ATT&CK technique execution
- **Custom Python Scripts** - Targeted attack automation (brute force, service creation)
- **Windows Event Viewer** - Native security event monitoring and evidence capture
- **Native Windows Tools** - Built-in system utilities for attack simulation

### Infrastructure
- **Windows Server 2019** - Domain Controller (aioulab.local)
- **Windows 11 Pro** - Domain-joined endpoint with Local Group Policy hardening
- **Kali Linux** - Hardened penetration testing platform with 100% CIS compliance
- **Active Directory** - Isolated lab domain environment
- **PowerShell** - Automation and security configuration

## 📁 Repository Structure

```
AD-Endpoint-and-Hardening-Lab/
├── README.md                          # This comprehensive overview
├── Active-Directory-Attack-Simulation/
│   ├── README.md                      # Detailed attack simulation documentation
│   ├── Scripts/
│   │   ├── Atomic-Red-Team-Guide.md   # ART installation and execution guide
│   │   ├── brute force.py             # Custom brute force script (T1110.001)
│   │   └── suspicious service.py      # Custom service creation script (T1543.003)
│   ├── Screenshots/                   # 12 Event ID screenshots + endpoint config
│   │   ├── Event_ID_*.png             # Windows security event evidence
│   │   ├── User_Account_*.png         # Account lifecycle events
│   │   ├── Account_Lockout.png        # Brute force detection
│   │   └── Endpoint_AD.png            # Domain configuration evidence
│   └── Documentation/
│       ├── Event-ID-Showcase.md       # Comprehensive visual event analysis
│       ├── Visual-Evidence-Summary.md # Quick reference for all screenshots
│       └── TTP-Event-Mapping.md       # Technical MITRE ATT&CK mapping
├── Endpoint-Hardening/
│   ├── README.md                      # Hardening methodology and results
│   ├── Documentation/
│   │   ├── Windows-Hardening-Summary.md # Windows 11 CIS hardening details
│   │   ├── Kali-Hardening-Summary.md   # Kali Linux hardening (100% compliance)
│   │   └── CIS-Compliance-Results.md   # Comprehensive compliance analysis
│   └── Screenshots/
│       ├── Wazuh-SCA-Windows/         # Windows compliance dashboards
│       └── Wazuh-SCA-Kali/            # Kali compliance dashboards
```

## 🎯 Goals & Outcomes

### Active Directory Attack Simulation
- ✅ Successfully executed MITRE ATT&CK techniques using Atomic Red Team + custom scripts
- ✅ Generated and documented 12+ distinct Windows Event IDs with screenshots
- ✅ Achieved 95%+ detection rate through Wazuh SIEM monitoring
- ✅ Comprehensive visual evidence collection covering authentication, account management, and directory services
- ✅ Validated attack simulation methodology with multiple execution approaches

### Endpoint Hardening Validation
- ✅ **Windows 11**: Achieved 90% CIS benchmark compliance (352/394 controls) via Local Group Policy
- ✅ **Kali Linux**: Achieved 100% CIS benchmark compliance (16/16 controls) via system configurations
- ✅ Validated compliance through automated Wazuh SCA dashboards with before/after comparisons
- ✅ Comprehensive documentation of hardening procedures for reproducibility

## 🔍 Key Achievements

1. **Visual Evidence Documentation**: 12+ distinct Event ID screenshots with comprehensive analysis
2. **High Detection Rate**: 95%+ attack detection through Wazuh SIEM monitoring
3. **Excellent Compliance Rates**: 90% (Windows) and 100% (Kali) CIS benchmark compliance
4. **Methodology Validation**: Multiple attack execution approaches (Atomic Red Team + custom scripts + manual AD changes)
5. **Comprehensive Documentation**: Detailed visual evidence, technical mapping, and procedural documentation

## 🚀 Getting Started

### For Active Directory Security Analysis
1. **Visual Evidence**: Browse `/Active-Directory-Attack-Simulation/Screenshots/` for Event ID screenshots
2. **Attack Simulation**: Review `/Active-Directory-Attack-Simulation/README.md` for methodology
3. **Technical Documentation**: Check `/Active-Directory-Attack-Simulation/Documentation/` for detailed analysis
4. **Scripts**: Explore `/Active-Directory-Attack-Simulation/Scripts/` for execution guides and custom tools

### For Endpoint Hardening Review
1. **Hardening Results**: Navigate to `/Endpoint-Hardening/README.md` for compliance overview
2. **Detailed Analysis**: Review documentation in `/Endpoint-Hardening/Documentation/`
3. **Visual Proof**: Check `/Endpoint-Hardening/Screenshots/` for Wazuh SCA dashboards

Each folder contains comprehensive documentation with setup instructions, methodologies, and findings.

## 📊 Results Summary

| Project Component | Metric | Achievement |
|-------------------|--------|-------------|
| **Event ID Documentation** | 12+ distinct screenshots | ✅ Complete |
| **Attack Detection Rate** | 95%+ via Wazuh SIEM | ✅ Excellent |
| **Windows CIS Compliance** | 90% (352/394 controls) | ✅ Achieved |
| **Kali CIS Compliance** | 100% (16/16 controls) | ✅ Perfect |
| **Visual Evidence Coverage** | Authentication + Account Management + Directory Services | ✅ Comprehensive |
| **Documentation Quality** | 4 detailed guides + technical mapping | ✅ Professional |

## 🔗 Professional Links

- **LinkedIn**: [Muhammad Rafay Ali](https://www.linkedin.com/in/muhammad-rafay-ali)
- **Email**: rafay.arshad1@outlook.com
- **GitHub**: [This Repository](https://github.com/0xRafuSec/AD-Endpoint-and-Hardening-Lab)

## 💡 Project Highlights

### What Makes This Lab Unique
- **Visual Evidence Focus**: Complete Event ID documentation with actual screenshots
- **Dual Methodology**: Combined automated tools (Atomic Red Team) with custom scripts and manual changes
- **High Detection Rate**: 95%+ attack detection validates monitoring effectiveness  
- **Perfect Documentation**: Professional-grade documentation suitable for portfolio presentation
- **Real-World Relevance**: Techniques and hardening measures directly applicable to enterprise environments

### Technical Depth Demonstrated
- **MITRE ATT&CK Mapping**: Direct correlation between attack techniques and generated events
- **CIS Compliance**: Industry-standard hardening with measurable compliance rates
- **SIEM Integration**: Real-time monitoring and correlation with Wazuh
- **Multiple Attack Vectors**: Authentication, account management, directory services, and persistence

---

## 📝 Project Credits

**Author**: Muhammad Rafay Ali (0xRafuSec)
**Date**: 2025  
**Purpose**: Cybersecurity Portfolio Demonstration  
**Status**: ✅ Complete and Clean  
**Industry Relevance**: Enterprise Security Operations

**Key Achievement**: This lab demonstrates comprehensive hands-on experience with both offensive security testing and defensive hardening measures, showcasing practical cybersecurity skills directly applicable to enterprise security operations and SOC environments.