mitre_attack_matrix = {
    "Reconnaissance": {
        "techniques_count": 10,
        "techniques": [
            "Active Scanning (3)",
            "Gather Victim Host Information (4)",
            "Gather Victim Identity Information (3)",
            "Gather Victim Network Information (6)",
            "Gather Victim Org Information (4)",
            "Phishing for Information (4)",
            "Search Closed Sources (2)",
            "Search Open Technical Databases (5)",
            "Search Open Websites/Domains (3)",
            "Search Victim-Owned Websites"
        ]
    },
    "Resource Development": {
        "techniques_count": 8,
        "techniques": [
            "Acquire Access",
            "Acquire Infrastructure (8)",
            "Compromise Accounts (3)",
            "Compromise Infrastructure (8)",
            "Develop Capabilities (4)",
            "Establish Accounts (3)",
            "Obtain Capabilities (7)",
            "Stage Capabilities (6)"
        ]
    },
    "Initial Access": {
        "techniques_count": 10,
        "techniques": [
            "Content Injection",
            "Drive-by Compromise",
            "Exploit Public-Facing Application",
            "External Remote Services",
            "Hardware Additions",
            "Phishing (4)",
            "Replication Through Removable Media",
            "Supply Chain Compromise (3)",
            "Trusted Relationship",
            "Valid Accounts (4)"
        ]
    },
    "Execution": {
        "techniques_count": 14,
        "techniques": [
            "Cloud Administration Command",
            "Command and Scripting Interpreter (10)",
            "Container Administration Command",
            "Deploy Container",
            "Exploitation for Client Execution",
            "Inter-Process Communication (3)",
            "Native API",
            "Scheduled Task/Job (5)",
            "Serverless Execution",
            "Shared Modules",
            "Software Deployment Tools",
            "System Services (2)",
            "User Execution (3)",
            "Windows Management Instrumentation"
        ]
    },
    "Persistence": {
        "techniques_count": 20,
        "techniques": [
            "Account Manipulation (6)",
            "BITS Jobs",
            "Boot or Logon Autostart Execution (14)",
            "Boot or Logon Initialization Scripts (5)",
            "Browser Extensions",
            "Compromise Host Software Binary",
            "Create Account (3)",
            "Create or Modify System Process (5)",
            "Event Triggered Execution (16)",
            "External Remote Services",
            "Hijack Execution Flow (13)",
            "Implant Internal Image",
            "Modify Authentication Process (9)",
            "Office Application Startup (6)",
            "Power Settings",
            "Pre-OS Boot (5)",
            "Scheduled Task/Job (5)",
            "Server Software Component (5)",
            "Traffic Signaling (2)",
            "Valid Accounts (4)"
        ]
    },
    "Privilege Escalation": {
        "techniques_count": 14,
        "techniques": [
            "Abuse Elevation Control Mechanism (6)",
            "Access Token Manipulation (5)",
            "Account Manipulation (6)",
            "Boot or Logon Autostart Execution (14)",
            "Boot or Logon Initialization Scripts (5)",
            "Create or Modify System Process (5)",
            "Domain or Tenant Policy Modification (2)",
            "Escape to Host",
            "Event Triggered Execution (16)",
            "Exploitation for Privilege Escalation",
            "Hijack Execution Flow (13)",
            "Process Injection (12)",
            "Scheduled Task/Job (5)",
            "Valid Accounts (4)"
        ]
    },
    "Defense Evasion": {
        "techniques_count": 43,
        "techniques": [
            "Abuse Elevation Control Mechanism (6)",
            "Access Token Manipulation (5)",
            "BITS Jobs",
            "Build Image on Host",
            "Debugger Evasion",
            "Deobfuscate/Decode Files or Information",
            "Deploy Container",
            "Direct Volume Access",
            "Domain or Tenant Policy Modification (2)",
            "Execution Guardrails (1)",
            "Exploitation for Defense Evasion",
            "File and Directory Permissions Modification (2)",
            "Hide Artifacts (12)",
            "Hijack Execution Flow (13)",
            "Impair Defenses (11)",
            "Impersonation",
            "Indicator Removal (9)",
            "Indirect Command Execution",
            "Masquerading (9)",
            "Modify Authentication Process (9)",
            "Modify Cloud Compute Infrastructure (5)",
            "Modify Registry",
            "Modify System Image (2)",
            "Network Boundary Bridging (1)",
            "Obfuscated Files or Information (13)",
            "Plist File Modification",
            "Pre-OS Boot (5)",
            "Process Injection (12)",
            "Reflective Code Loading",
            "Rogue Domain Controller",
            "Rootkit",
            "Subvert Trust Controls (6)",
            "System Binary Proxy Execution (14)",
            "System Script Proxy Execution (2)",
            "Template Injection",
            "Traffic Signaling (2)",
            "Trusted Developer Utilities Proxy Execution (1)",
            "Unused/Unsupported Cloud Regions",
            "Use Alternate Authentication Material (4)",
            "Valid Accounts (4)",
            "Virtualization/Sandbox Evasion (3)",
            "Weaken Encryption (2)",
            "XSL Script Processing"
        ]
    },
    "Credential Access": {
        "techniques_count": 17,
        "techniques": [
            "Adversary-in-the-Middle (3)",
            "Brute Force (4)",
            "Credentials from Password Stores (6)",
            "Exploitation for Credential Access",
            "Forced Authentication",
            "Forge Web Credentials (2)",
            "Input Capture (4)",
            "Modify Authentication Process (9)",
            "Multi-Factor Authentication Interception",
            "Multi-Factor Authentication Request Generation",
            "Network Sniffing",
            "OS Credential Dumping (8)",
            "Steal Application Access Token",
            "Steal or Forge Authentication Certificates",
            "Steal or Forge Kerberos Tickets (4)",
            "Steal Web Session Cookie",
            "Unsecured Credentials (8)"
        ]
    },
    "Discovery": {
        "techniques_count": 32,
        "techniques": [
            "Account Discovery (4)",
            "Application Window Discovery",
            "Browser Information Discovery",
            "Cloud Infrastructure Discovery",
            "Cloud Service Dashboard",
            "Cloud Service Discovery",
            "Cloud Storage Object Discovery",
            "Container and Resource Discovery",
            "Debugger Evasion",
            "Device Driver Discovery",
            "Domain Trust Discovery",
            "File and Directory Discovery",
            "Group Policy Discovery",
            "Log Enumeration",
            "Network Service Discovery",
            "Network Share Discovery",
            "Network Sniffing",
            "Password Policy Discovery",
            "Peripheral Device Discovery",
            "Permission Groups Discovery (3)",
            "Process Discovery",
            "Query Registry",
            "Remote System Discovery",
            "Software Discovery (1)",
            "System Information Discovery",
            "System Location Discovery (1)",
            "System Network Configuration Discovery (2)",
            "System Network Connections Discovery",
            "System Owner/User Discovery",
            "System Service Discovery",
            "System Time Discovery",
            "Virtualization/Sandbox Evasion (3)"
        ]
    },
    "Lateral Movement": {
        "techniques_count": 9,
        "techniques": [
            "Exploitation of Remote Services",
            "Internal Spearphishing",
            "Lateral Tool Transfer",
            "Remote Service Session Hijacking (2)",
            "Remote Services (8)",
            "Replication Through Removable Media",
            "Software Deployment Tools",
            "Taint Shared Content",
            "Use Alternate Authentication Material (4)"
        ]
    },
    "Collection": {
        "techniques_count": 17,
        "techniques": [
            "Adversary-in-the-Middle (3)",
            "Archive Collected Data (3)",
            "Audio Capture",
            "Automated Collection",
            "Browser Session Hijacking",
            "Clipboard Data",
            "Data from Cloud Storage",
            "Data from Configuration Repository (2)",
            "Data from Information Repositories (3)",
            "Data from Local System",
            "Data from Network Shared Drive",
            "Data from Removable Media",
            "Data Staged (2)",
            "Email Collection (3)",
            "Input Capture (4)",
            "Screen Capture",
            "Video Capture"
        ]
    },
    "Command and Control": {
        "techniques_count": 18,
        "techniques": [
            "Application Layer Protocol (4)",
            "Communication Through Removable Media",
            "Content Injection",
            "Data Encoding (2)",
            "Data Obfuscation (3)",
            "Dynamic Resolution (3)",
            "Encrypted Channel (2)",
            "Fallback Channels",
            "Hide Infrastructure",
            "Ingress Tool Transfer",
            "Multi-Stage Channels",
            "Non-Application Layer Protocol",
            "Non-Standard Port",
            "Protocol Tunneling",
            "Proxy (4)",
            "Remote Access Software",
            "Traffic Signaling (2)",
            "Web Service (3)"
        ]
    },
    "Exfiltration": {
        "techniques_count": 9,
        "techniques": [
            "Automated Exfiltration (1)",
            "Data Transfer Size Limits",
            "Exfiltration Over Alternative Protocol (3)",
            "Exfiltration Over C2 Channel",
            "Exfiltration Over Other Network Medium (1)",
            "Exfiltration Over Physical Medium (1)",
            "Exfiltration Over Web Service (4)",
            "Scheduled Transfer",
            "Transfer Data to Cloud Account"
        ]
    },
    "Impact": {
        "techniques_count": 14,
        "techniques": [
            "Account Access Removal",
            "Data Destruction",
            "Data Encrypted for Impact",
            "Data Manipulation (3)",
            "Defacement (2)",
            "Disk Wipe (2)",
            "Endpoint Denial of Service (4)",
            "Financial Theft",
            "Firmware Corruption",
            "Inhibit System Recovery",
            "Network Denial of Service (2)",
            "Resource Hijacking",
            "Service Stop",
            "System Shutdown/Reboot"
        ]
    }
}

print(mitre_attack_matrix)

ground_truth_matrix = {
    "Reconnaissance": {
        "techniques_count": 1,
        "techniques": [
            "Phishing for Information (4)"
        ]
    },
    "Resource Development": {
        "techniques_count": 3,
        "techniques": [
            "Acquire Infrastructure (8)",
            "Compromise Accounts (3)",
            "Establish Accounts (3)"
        ]
    },
    "Initial Access": {
        "techniques_count": 2,
        "techniques": [
            "Phishing (4)",
            "Valid Accounts (4)"
        ]
    },
    "Execution": {
        "techniques_count": 0,
        "techniques": []
    },
    "Persistence": {
        "techniques_count": 0,
        "techniques": []
    },
    "Privilege Escalation": {
        "techniques_count": 1,
        "techniques": [
            "Account Manipulation"
        ]
    },
    "Defense Evasion": {
        "techniques_count": 3,
        "techniques": [
            "Access Token Manipulation",
            "Deobfuscate/Decode Files or Information",
            "Masquerading"
        ]
    },
    "Credential Access": {
        "techniques_count": 4,
        "techniques": [
            "Brute Force",
            "Credentials from Password Stores",
            "Input Capture",
            "Modify Authentication Process"
        ]
    },
    "Discovery": {
        "techniques_count": 2,
        "techniques": [
            "Account Discovery",
            "File and Directory Discovery"
        ]
    },
    "Lateral Movement": {
        "techniques_count": 1,
        "techniques": [
            "Use Alternate Authentication Material"
        ]
    },
    "Collection": {
        "techniques_count": 2,
        "techniques": [
            "Automated Collection",
            "Email Collection"
        ]
    },
    "Command and Control": {
        "techniques_count": 4,
        "techniques": [
            "Application Layer Protocol (4)",
            "Data Encoding (2)",
            "Data Obfuscation (3)",
            "Web Service (3)"
        ]
    },
    "Exfiltration": {
        "techniques_count": 1,
        "techniques": [
            "Exfiltration Over Web Service (4)"
        ]
    },
    "Impact": {
        "techniques_count": 0,
        "techniques": []
    }
}

print(ground_truth_matrix)

assert(len(ground_truth_matrix) == len(mitre_attack_matrix))
assert(all(tactic in ground_truth_matrix for tactic in mitre_attack_matrix))
assert(all(tactic in mitre_attack_matrix for tactic in ground_truth_matrix))
all_subtechniques_mitre = set()
all_subtechniques_ground = set()
for tactic, tactic_item in ground_truth_matrix.items():
    techniques = set(tactic_item["techniques"])
    all_subtechniques_ground.update(techniques)
for tactic, tactic_item in mitre_attack_matrix.items():
    techniques = set(tactic_item["techniques"])
    all_subtechniques_mitre.update(techniques)

assert(all_subtechniques_ground.issubset(all_subtechniques_mitre))
