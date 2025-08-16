import subprocess
import sys
from io import StringIO


def run_port_scan(domain):
    result = []
    # Removed CLI banner for clean backend
    
    try:
        # Run nmap command and capture output
        process = subprocess.run([
            "nmap",
            "-Pn",
            "-sV",
            "-T4",
            domain
        ], capture_output=True, text=True, timeout=300)
        
        # Get the output
        if process.stdout:
            result.extend(process.stdout.split('\n'))
        if process.stderr:
            result.append("STDERR:")
            result.extend(process.stderr.split('\n'))
            
    # Removed CLI print compatibility for clean backend
                
        return "\n".join([line for line in result if line.strip()])
        
    except subprocess.TimeoutExpired:
        error_msg = f"[-] Port scan timed out for {domain}"
    # Removed CLI print compatibility for clean backend
        return error_msg
    except FileNotFoundError:
        error_msg = "[-] Error: Nmap not found. Please install Nmap and add it to your PATH."
    # Removed CLI print compatibility for clean backend
        return error_msg
    except Exception as e:
        error_msg = f"[-] Error running port scan: {e}"
    # Removed CLI print compatibility for clean backend
        return error_msg           