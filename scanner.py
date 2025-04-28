#!/usr/bin/env python3
import os
import subprocess
import platform
from utils import print_result, run_command

def check_firewall():
    """Check if firewall is active"""
    try:
        if platform.system() == "Linux":
            result = subprocess.run(["sudo", "ufw", "status"], capture_output=True, text=True)
            if "active" in result.stdout.lower():
                return True, "Firewall is active"
            return False, "Firewall is not active"
        elif platform.system() == "Windows":
            # Windows firewall check
            result = subprocess.run(["netsh", "advfirewall", "show", "allprofiles"], capture_output=True, text=True)
            if "on" in result.stdout.lower():
                return True, "Windows Firewall is active"
            return False, "Windows Firewall is not active"
        else:
            return False, "Unsupported OS for firewall check"
    except Exception as e:
        return False, f"Firewall check failed: {str(e)}"

def check_wifi_security():
    """Check WiFi security settings"""
    try:
        if platform.system() == "Linux":
            result = subprocess.run(["sudo", "iwconfig"], capture_output=True, text=True)
            if "wpa2" in result.stdout.lower():
                return True, "WiFi uses WPA2 encryption"
            elif "wep" in result.stdout.lower():
                return False, "WiFi uses insecure WEP encryption"
            elif "open" in result.stdout.lower():
                return False, "WiFi is open (no encryption)"
            else:
                return False, "Unable to determine WiFi security"
        else:
            return False, "WiFi security check not implemented for this OS"
    except Exception as e:
        return False, f"WiFi security check failed: {str(e)}"

def check_rootkits():
    """Check for common rootkits"""
    try:
        if platform.system() == "Linux":
            result = subprocess.run(["sudo", "chkrootkit"], capture_output=True, text=True)
            if "infected" in result.stdout.lower():
                return False, "Possible rootkit infection detected"
            return True, "No rootkits detected"
        else:
            return False, "Rootkit check not implemented for this OS"
    except FileNotFoundError:
        return False, "chkrootkit not installed (run: sudo apt install chkrootkit)"
    except Exception as e:
        return False, f"Rootkit check failed: {str(e)}"

def check_common_vulnerabilities():
    """Check for common vulnerabilities"""
    results = []
    
    # Check for default credentials
    if platform.system() == "Linux":
        try:
            result = subprocess.run(["sudo", "grep", "-i", "password", "/etc/shadow"], capture_output=True, text=True)
            if ":::" in result.stdout:
                results.append(("Default passwords", False, "Accounts with empty passwords detected"))
            else:
                results.append(("Default passwords", True, "No empty passwords detected"))
        except Exception as e:
            results.append(("Default passwords", False, f"Check failed: {str(e)}"))
    
    return results

def main():
    print("\n=== SafePulse Security Scan ===")
    
    # Run checks
    checks = [
        ("Firewall Status", check_firewall()),
        ("WiFi Security", check_wifi_security()),
        ("Rootkit Check", check_rootkits())
    ]
    
    # Add common vulnerabilities
    vuln_checks = check_common_vulnerabilities()
    checks.extend(vuln_checks)
    
    # Display results
    for name, (status, message) in checks:
        print_result(name, status, message)
    
    print("\nScan completed. Review recommendations above.")

if __name__ == "__main__":
    main()
