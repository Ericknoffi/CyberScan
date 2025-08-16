import requests


def scan_basic_info(url):
    result = []
    result.append("[+] Scanning for basic information...")
    
    try:
        response = requests.get(url, timeout=5)
        result.append(f"[*] Status code: {response.status_code}")
        result.append(f"[*] Server: {response.headers.get('server', 'unknown')}")
         
        headers = {k.lower(): v for k, v in response.headers.items()}
        
        result.append("\n[!] Basic Security Headers")
        basic_headers = [
            'content-security-policy',
            'x-frame-options',
            'x-xss-protection'
        ]        
        for header in basic_headers:
            result.append(f"{header}: {response.headers.get(header, 'Missing')}")
            
        result.append("\n[!] Advanced Security Headers:")
        advanced_headers = [
            'strict-transport-security',
            'referrer-policy',
            'permissions-policy',
        ]
        for header in advanced_headers:
            result.append(f"{header}: {response.headers.get(header, 'Missing')}")
        
        result.append("\n[!] Cookies Flags Check:")
        cookies = response.cookies
        if not cookies:
            result.append("No cookies found.")
        else:
            for cookie in cookies:
                result.append(f"Cookie: {cookie.name}")
                result.append(f"  - Secure: {cookie.secure}")
                result.append(f"  - HttpOnly: {'✅' if 'httponly' in cookie._rest.keys() else '❌'}")
                samesite = cookie._rest.get('samesite', 'Missing')
                result.append(f"  - SameSite: {samesite}")
                
    # Removed CLI print compatibility for clean backend
            
        return "\n".join(result)
                
    except requests.RequestException as e:
        error_msg = f"[-] Error fetching {url}: {e}"
        print(error_msg)
        return error_msg
           