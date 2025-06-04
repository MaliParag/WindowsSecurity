import re

def generate_filename(title):
    # Convert to lowercase
    filename = title.lower()
    # Replace ampersands
    filename = filename.replace('&', '_and_')
    # Replace spaces and special characters with underscores
    filename = re.sub(r'[^a-z0-9_]+', '_', filename)
    # Collapse consecutive underscores
    filename = re.sub(r'_+', '_', filename)
    # Remove leading/trailing underscores that might result from replacements
    filename = filename.strip('_')
    # Append .md
    filename += ".md"
    return filename

titles = [
    "Applocker",
    "Browser Protection",
    "Microsoft Defender Application Guard",
    "Microsoft Vulnerable Driver Block",
    "Smart App Control",
    "Trusted Signing",
    "Virtualization Based Integrity (VBI)",
    "Windows Sandbox",
    "Windows Subsystem For Linux (WSL)",
    "WSL App Isolation",
    "Microsoft Entra ID",
    "Microsoft Entra Private Access",
    "Microsoft Entra Internet Access",
    "Azure Attestation Service",
    "Microsoft Defender for Endpoint",
    "Cloud-native device management",
    "Microsoft Intune",
    "Windows enrollment attestation",
    "Microsoft Cloud PKI",
    "Enterprise Privilege Management (EPM)",
    "Mobile Application Management (MDM)",
    "Security baselines",
    "Local Administrator Password Solution (LAPS)",
    "Windows Autopilot",
    "Windows Update for Business",
    "Windows Autopatch",
    "Windows Hotpatch",
    "OneDrive for work or school",
    "Universal Print",
    "Microsoft account",
    "Find my device",
    "OneDrive for personal use",
    "Family Safety",
    "Personal Vault",
    "Configuration Lock",
    "Direct Memory Access (DMA) Protection",
    "Hardware Enforced Stack Protection",
    "Hypervisor Enforced Bug Reporting (HEBR)",
    "Hypervisor Protected Code Integrity (HVCI)",
    "Kernel Data Memory Entropy DMA Protection",
    "Microsoft Secure Process Protections",
    "Secure Boot",
    "Trusted Platform Module (TPM) 2.0",
    "Virtualization Based Security (VBS)",
    "Access Management And Control (UAC)",
    "Account Lockout Policy",
    "Azure AD Join",
    "Credential Guard",
    "Enhanced Phishing Protection",
    "Enhanced Sign In Security",
    "FIDO2",
    "Microsoft Authenticator",
    "Microsoft Privacy Statements And Controls",
    "Privacy Controls",
    "Privacy Resource Usage",
    "Remote Credential Guard",
    "Smart Card",
    "Token Protection",
    "VBS Key Protection",
    "Windows Diagnostic Data Processor Configuration",
    "Windows Hello",
    "Windows Hello For Business",
    "Webauthn",
    "5G and eSIM",
    "BitLocker",
    "BitLocker To Go",
    "Certificates",
    "Code Signing and Integrity",
    "Config Refresh",
    "Controlled Folder Access",
    "Cryptography",
    "Device Health Attestation",
    "Domain Name System (DNS) Security",
    "Email Encryption",
    "Encrypted File System (EFS)",
    "Encrypted Hard Drive",
    "Exploit Protection",
    "Internet Protocol Security (IPSec)",
    "Kiosk Mode",
    "Microsoft Defender Antivirus",
    "Microsoft Defender Application Guard", # Duplicate
    "Microsoft Defender For Business",
    "Network Access Protection",
    "Personal Data Encryption",
    "Rust For Windows",
    "Server Message Block (SMB) For Remote Connections",
    "Tamper Protection",
    "Transport Layer Security (TLS)",
    "Wi-Fi Protection",
    "Windows Firewall",
    "Windows Protected Process",
    "Windows Security App",
    "Windows Security Policy Settings And Auditing",
    "Common Criteria (CC)",
    "DevDivSecOps",
    "Federal Information Processing Standard (FIPS)",
    "Microsoft Offensive Research And Security Engineering (MORSE)",
    "Secure Future Initiative (SFI)",
    "Security Development Lifecycle (SDL)",
    "Software Bill Of Materials (SBOM)",
    "Windows Kernel And Microsoft Bug Bounty Programs",
    "Windows Software Development Kit (SDK)"
]

for title in titles:
    filename = generate_filename(title)
    print(f"Original: {title}")
    print(f"Filename: {filename}")
    print("-" * 20)
