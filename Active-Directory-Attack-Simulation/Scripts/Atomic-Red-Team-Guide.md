# Atomic Red Team Implementation Guide

> **Complete guide for installing, configuring, and executing Atomic Red Team tests in Active Directory environments.**

## 🎯 Overview

Atomic Red Team is a library of tests mapped to the MITRE ATT&CK framework that allows security teams to test their detection capabilities. This guide provides step-by-step instructions for implementing Atomic Red Team in an Active Directory environment for comprehensive security testing.

## 📋 Prerequisites

### System Requirements
- **Windows Systems**: Windows 10/11 or Windows Server 2016+
- **PowerShell**: Version 5.1 or PowerShell Core 6+
- **Administrative Access**: Local administrator privileges required
- **Network Access**: Internet connectivity for downloads
- **Memory**: Minimum 4GB RAM recommended
- **Storage**: 2GB free space for Atomic Red Team files

### Environment Setup
- **Domain Controller**: Windows Server 2025
- **Client Workstation**: Windows 11 Pro (domain-joined)
- **Attack Platform**: Windows 10/11 or Kali Linux
- **SIEM**: Wazuh deployment with real-time monitoring

## 🚀 Installation Process

### Step 1: PowerShell Preparation

**Check PowerShell Version**:
```powershell
# Verify PowerShell version
$PSVersionTable.PSVersion

# Should be 5.1 or higher
```

**Set Execution Policy**:
```powershell
# Allow script execution (run as Administrator)
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser -Force

# Verify the change
Get-ExecutionPolicy -List
```

**Enable PowerShell Logging** (Optional but Recommended):
```powershell
# Enable PowerShell script block logging
$regPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"
if (!(Test-Path $regPath)) {
    New-Item -Path $regPath -Force
}
Set-ItemProperty -Path $regPath -Name "EnableScriptBlockLogging" -Value 1
```

### Step 2: Install Atomic Red Team Module

**Method 1: PowerShell Gallery (Recommended)**:
```powershell
# Install required modules
Install-Module -Name invoke-atomicredteam,powershell-yaml -Force -Scope CurrentUser

# Import the module
Import-Module Invoke-AtomicRedTeam

# Verify installation
Get-Command -Module Invoke-AtomicRedTeam
```

**Method 2: Manual Installation**:
```powershell
# Download from GitHub
$downloadPath = "$env:TEMP\atomic-red-team.zip"
Invoke-WebRequest -Uri "https://github.com/redcanaryco/atomic-red-team/archive/master.zip" -OutFile $downloadPath

# Extract to desired location
$extractPath = "C:\AtomicRedTeam"
Expand-Archive -Path $downloadPath -DestinationPath $extractPath -Force

# Import manually
Import-Module "$extractPath\atomic-red-team-master\execution-frameworks\Invoke-AtomicRedTeam\Invoke-AtomicRedTeam.psm1"
```

### Step 3: Download Atomics Folder

```powershell
# Install Atomic test files
Install-AtomicRedTeam -getAtomics -Force

# Default location: C:\AtomicRedTeam\atomics
# Verify installation
Get-ChildItem "C:\AtomicRedTeam\atomics" | Select-Object Name | Sort-Object Name
```

### Step 4: Verify Installation

```powershell
# Test basic functionality
Invoke-AtomicTest T1003.001 -ShowDetailsBrief

# Check available techniques
Get-ChildItem "C:\AtomicRedTeam\atomics" | Where-Object { $_.Name -match "^T\d{4}" } | Measure-Object
```

## 🔧 Configuration

### Environment Variables
```powershell
# Set Atomic Red Team path (if not default)
$env:ATOMIC_RED_TEAM = "C:\AtomicRedTeam"

# Set atomics path
$env:ATOMIC_REDTEAM_ATOMICS = "C:\AtomicRedTeam\atomics"
```

### Custom Configuration File
```powershell
# Create custom config (optional)
$config = @{
    PathToAtomicsFolder = "C:\AtomicRedTeam\atomics"
    ExecutionLogPath = "C:\AtomicRedTeam\execution.log"
    PathToInvokeFolder = "C:\AtomicRedTeam\invoke-atomicredteam"
}

# Save configuration
$config | ConvertTo-Json | Out-File "C:\AtomicRedTeam\config.json"
```

## ⚔️ Active Directory Technique Execution

### Authentication and Credential Access

#### T1078 - Valid Accounts
```powershell
# Show available tests
Invoke-AtomicTest T1078 -ShowDetailsBrief

# Execute with domain context
Invoke-AtomicTest T1078 -TestNumbers 1,2 -InputArgs @{
    "username" = "testuser@lab.local"
    "password" = "TestPassword123!"
}
```

#### T1003.001 - LSASS Memory Dump
```powershell
# Check prerequisites
Invoke-AtomicTest T1003.001 -GetPrereqs

# Execute credential dumping test
Invoke-AtomicTest T1003.001 -TestNumbers 1

# Expected Event IDs: 4688, 4648, 10 (if Sysmon enabled)
```

#### T1558.003 - Kerberoasting
```powershell
# Execute Kerberoasting test
Invoke-AtomicTest T1558.003

# Expected Event IDs: 4769, 4770
```

### Discovery Techniques

#### T1087.002 - Domain Account Discovery
```powershell
# Execute domain enumeration
Invoke-AtomicTest T1087.002

# Expected Event IDs: 4661, 4662
```

#### T1069.002 - Domain Groups Discovery
```powershell
# Execute group enumeration
Invoke-AtomicTest T1069.002

# Expected Event IDs: 4661, 4662
```

### Lateral Movement

#### T1021.001 - Remote Desktop Protocol
```powershell
# Execute RDP lateral movement test
Invoke-AtomicTest T1021.001 -InputArgs @{
    "target_host" = "192.168.100.20"
    "username" = "lab\testuser"
    "password" = "TestPassword123!"
}

# Expected Event IDs: 4624, 4625, 4634
```

### Persistence and Privilege Escalation

#### T1547.001 - Registry Run Keys
```powershell
# Execute registry persistence
Invoke-AtomicTest T1547.001

# Expected Event IDs: 4657, 4656
```

#### T1134 - Access Token Manipulation
```powershell
# Execute token manipulation
Invoke-AtomicTest T1134

# Expected Event IDs: 4672, 4624
```

### Defense Evasion

#### T1070.001 - Clear Windows Event Logs
```powershell
# Execute event log clearing
Invoke-AtomicTest T1070.001

# Expected Event IDs: 1102, 1100
```

## 📊 Batch Execution Scripts

### Complete AD Test Suite
```powershell
# Comprehensive Active Directory test suite
$ADTechniques = @{
    "T1078" = "Valid Accounts"
    "T1087.002" = "Domain Account Discovery"
    "T1069.002" = "Domain Groups Discovery" 
    "T1003.001" = "LSASS Memory Dump"
    "T1558.003" = "Kerberoasting"
    "T1021.001" = "Remote Desktop Protocol"
    "T1550.002" = "Pass the Hash"
    "T1134" = "Access Token Manipulation"
    "T1547.001" = "Registry Run Keys"
    "T1070.001" = "Clear Windows Event Logs"
}

# Execute with logging
$logPath = "C:\AtomicRedTeam\AD-Test-Results.log"
Start-Transcript -Path $logPath

foreach ($technique in $ADTechniques.Keys) {
    Write-Host "`n[$(Get-Date)] Executing $technique - $($ADTechniques[$technique])" -ForegroundColor Green
    
    try {
        # Show test details
        Invoke-AtomicTest $technique -ShowDetailsBrief
        
        # Execute test
        Invoke-AtomicTest $technique -PromptForInputArgs
        
        Write-Host "[$(Get-Date)] Successfully executed $technique" -ForegroundColor Green
        
        # Wait between tests
        Start-Sleep -Seconds 60
        
    }
    catch {
        Write-Host "[$(Get-Date)] Failed to execute $technique : $_" -ForegroundColor Red
    }
}

Stop-Transcript
```

### Targeted Execution by Tactic
```powershell
# Execute by MITRE ATT&CK Tactic
function Invoke-TacticTests {
    param(
        [Parameter(Mandatory=$true)]
        [ValidateSet("InitialAccess", "Execution", "Persistence", "PrivilegeEscalation", "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Collection")]
        [string]$Tactic
    )
    
    $TacticTechniques = @{
        "CredentialAccess" = @("T1003.001", "T1558.003")
        "Discovery" = @("T1087.002", "T1069.002")
        "LateralMovement" = @("T1021.001", "T1550.002")
        "Persistence" = @("T1547.001")
        "PrivilegeEscalation" = @("T1134")
        "DefenseEvasion" = @("T1070.001")
    }
    
    if ($TacticTechniques.ContainsKey($Tactic)) {
        foreach ($technique in $TacticTechniques[$Tactic]) {
            Write-Host "Executing $technique for tactic $Tactic" -ForegroundColor Yellow
            Invoke-AtomicTest $technique
            Start-Sleep -Seconds 30
        }
    }
}

# Usage examples
Invoke-TacticTests -Tactic "CredentialAccess"
Invoke-TacticTests -Tactic "Discovery"
```

## 🔍 Monitoring and Validation

### Wazuh Integration
```powershell
# Function to check Wazuh alerts after test execution
function Test-WazuhDetection {
    param(
        [string]$TechniqueID,
        [int]$WaitSeconds = 60
    )
    
    Write-Host "Waiting $WaitSeconds seconds for Wazuh detection..." -ForegroundColor Yellow
    Start-Sleep -Seconds $WaitSeconds
    
    # Query Wazuh API (customize endpoint and credentials)
    $wazuhAPI = "https://192.168.100.50:55000"
    $headers = @{
        "Authorization" = "Bearer YOUR_TOKEN_HERE"
        "Content-Type" = "application/json"
    }
    
    try {
        $alerts = Invoke-RestMethod -Uri "$wazuhAPI/alerts" -Headers $headers -Method GET
        $relatedAlerts = $alerts | Where-Object { $_.rule.mitre.id -eq $TechniqueID }
        
        if ($relatedAlerts) {
            Write-Host "✅ Detection successful for $TechniqueID" -ForegroundColor Green
            $relatedAlerts | Select-Object timestamp, rule.description, rule.level | Format-Table
        } else {
            Write-Host "❌ No detection found for $TechniqueID" -ForegroundColor Red
        }
    }
    catch {
        Write-Host "Unable to query Wazuh API: $_" -ForegroundColor Red
    }
}
```

### Event Log Validation
```powershell
# Function to check Windows Event Logs
function Test-EventLogGeneration {
    param(
        [string]$TechniqueID,
        [array]$ExpectedEventIDs
    )
    
    $startTime = (Get-Date).AddMinutes(-5)
    
    foreach ($eventID in $ExpectedEventIDs) {
        $events = Get-WinEvent -FilterHashtable @{
            LogName = 'Security'
            ID = $eventID
            StartTime = $startTime
        } -ErrorAction SilentlyContinue
        
        if ($events) {
            Write-Host "✅ Event ID $eventID found for $TechniqueID" -ForegroundColor Green
        } else {
            Write-Host "❌ Event ID $eventID not found for $TechniqueID" -ForegroundColor Red
        }
    }
}

# Usage example
Test-EventLogGeneration -TechniqueID "T1003.001" -ExpectedEventIDs @(4688, 4648)
```

## 🛡️ Cleanup and Restoration

### Automatic Cleanup
```powershell
# Execute with automatic cleanup
Invoke-AtomicTest T1003.001 -Cleanup

# Cleanup all tests in a session
$executedTests = @("T1003.001", "T1558.003", "T1087.002")
foreach ($test in $executedTests) {
    Write-Host "Cleaning up $test..." -ForegroundColor Yellow
    Invoke-AtomicTest $test -Cleanup
}
```

### Manual System Restoration
```powershell
# Manual cleanup script
function Invoke-SystemCleanup {
    Write-Host "Starting system cleanup..." -ForegroundColor Yellow
    
    # Remove suspicious services
    $suspiciousServices = Get-Service | Where-Object { $_.Name -like "*Suspicious*" -or $_.Name -like "*Test*" }
    foreach ($service in $suspiciousServices) {
        Write-Host "Removing service: $($service.Name)" -ForegroundColor Red
        sc.exe delete $service.Name
    }
    
    # Clear temporary files
    Remove-Item -Path "$env:TEMP\*.exe" -Force -ErrorAction SilentlyContinue
    Remove-Item -Path "$env:TEMP\*.dll" -Force -ErrorAction SilentlyContinue
    
    # Reset registry changes (if known)
    $regPaths = @(
        "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\AtomicTest*",
        "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\AtomicTest*"
    )
    
    foreach ($path in $regPaths) {
        Remove-ItemProperty -Path $path -Name "*" -Force -ErrorAction SilentlyContinue
    }
    
    Write-Host "System cleanup completed." -ForegroundColor Green
}
```

## 📋 Best Practices

### Security Guidelines
1. **Isolated Environment**: Always run in isolated lab environments
2. **Authorization**: Obtain proper authorization before testing
3. **Monitoring**: Ensure monitoring solutions are active
4. **Documentation**: Document all test execution
5. **Cleanup**: Always cleanup after testing

### Execution Best Practices
1. **Incremental Testing**: Execute techniques one at a time
2. **Wait Periods**: Allow time between tests for detection
3. **Baseline**: Establish baseline before testing
4. **Validation**: Verify expected results after each test
5. **Error Handling**: Handle execution errors gracefully

### Documentation Standards
1. **Test Planning**: Document test objectives and scope
2. **Execution Log**: Maintain detailed execution logs
3. **Results**: Document test results and detection status
4. **Lessons Learned**: Capture insights and improvements
5. **Reporting**: Create comprehensive test reports

## 🔗 Resources and Support

### Official Resources
- **Atomic Red Team GitHub**: https://github.com/redcanaryco/atomic-red-team
- **Documentation**: https://atomicredteam.io/
- **Invoke-AtomicRedTeam**: https://github.com/redcanaryco/invoke-atomicredteam

### Community Resources
- **MITRE ATT&CK**: https://attack.mitre.org/
- **Red Canary Blog**: https://redcanary.com/blog/
- **Atomic Red Team Slack**: Join the community for support

### Troubleshooting
- **Common Issues**: Check GitHub issues for solutions
- **Prerequisites**: Ensure all prerequisites are met
- **Permissions**: Verify administrative privileges
- **Antivirus**: Consider AV exclusions for testing

---

## 📝 Summary

This guide provides comprehensive instructions for implementing Atomic Red Team in Active Directory environments. The framework enables systematic testing of detection capabilities across the MITRE ATT&CK framework, providing valuable insights into security posture and detection effectiveness.

**Key Benefits**:
- Automated technique execution
- Standardized testing methodology  
- Comprehensive MITRE ATT&CK coverage
- Integration with existing monitoring solutions
- Repeatable and documented testing process

**File Location**: `/Active-Directory-Attack-Simulation/Scripts/Atomic-Red-Team-Guide.md`  
**Related Files**: 
- [brute force.py](brute force.py) - Custom brute force script
- [suspicious service.py](suspicious service.py) - Custom service creation script
- [TTP Event Mapping](../Documentation/TTP-Event-Mapping.md) - Technical correlation guide 