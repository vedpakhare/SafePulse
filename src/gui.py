# src/gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from scanner import check_firewall, check_wifi_security, check_rootkits, check_common_vulnerabilities

class SafePulseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SafePulse - Cyber Hygiene Scanner")
        self.root.geometry("600x400")
        
        # Header
        header = ttk.Frame(root)
        header.pack(pady=10)
        ttk.Label(header, text="SafePulse", font=("Helvetica", 16, "bold")).pack()
        ttk.Label(header, text="Your System's Heartbeat of Security").pack()
        
        # Scan Button
        ttk.Button(root, text="Run Security Scan", command=self.run_scan).pack(pady=20)
        
        # Results Frame
        self.results_frame = ttk.Frame(root)
        self.results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Text widget for results
        self.results_text = tk.Text(self.results_frame, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.results_text.config(state=tk.DISABLED)
        
        # Footer
        ttk.Label(root, text="Visit https://safepulse.github.io for more information").pack(side=tk.BOTTOM, pady=5)
    
    def run_scan(self):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "=== Running Security Scan ===\n\n")
        
        # Run checks
        checks = [
            ("Firewall Status", check_firewall()),
            ("WiFi Security", check_wifi_security()),
            ("Rootkit Check", check_rootkits())
        ]
        
        # Add common vulnerabilities
        vuln_checks = check_common_vulnerabilities()
        checks.extend([(f"Vulnerability: {name}", (status, msg)) for name, status, msg in vuln_checks])
        
        # Display results
        for name, (status, message) in checks:
            color = "green" if status else "red"
            self.results_text.insert(tk.END, f"{name}:\n", "bold")
            self.results_text.insert(tk.END, f"  {message}\n\n", color)
        
        self.results_text.insert(tk.END, "\n=== Scan Complete ===")
        self.results_text.config(state=tk.DISABLED)
        
        # Scroll to top
        self.results_text.see(1.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = SafePulseGUI(root)
    
    # Configure tags for colored text
    app.results_text.tag_config("bold", font=("Helvetica", 10, "bold"))
    app.results_text.tag_config("green", foreground="green")
    app.results_text.tag_config("red", foreground="red")
    
    root.mainloop()
