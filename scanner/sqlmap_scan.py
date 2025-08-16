import subprocess

def run_sqlmap(url):
    result = []
    result.append(f"[+] Running SQLMap on {url}...")
    
    try:
        # Run sqlmap command and capture output  
        process = subprocess.run([
            "sqlmap",
            "-u", url,
            "--batch",
            "--crawl=1",
            "--level=2",
            "--random-agent"
        ], capture_output=True, text=True, timeout=600)
        
        # Get the output
        if process.stdout:
            result.extend(process.stdout.split('\n'))
        if process.stderr:
            result.append("STDERR:")
            result.extend(process.stderr.split('\n'))
            
    # Removed CLI print compatibility for clean backend
                
        return "\n".join([line for line in result if line.strip()])
        
    except subprocess.TimeoutExpired:
        error_msg = f"[-] SQLMap scan timed out for {url}"
    # Removed CLI print compatibility for clean backend
        return error_msg
    except FileNotFoundError:
        error_msg = "[-] Error: SQLMap not found. Please install SQLMap and add it to your PATH."
    # Removed CLI print compatibility for clean backend
        return error_msg
    except Exception as e:
        error_msg = f"[-] Error running SQLMap: {e}"
    # Removed CLI print compatibility for clean backend
        return error_msg
        