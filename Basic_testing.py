#!/usr/bin/env python3
"""
CONTOH BASIC SECURITY TESTING - EDUCATIONAL
"""

import requests
from urllib.parse import urljoin

def check_website_safety(url):
    """Contoh basic security check"""
    
    print(f"\n🔍 Checking: {url}")
    
    try:
        # Check if HTTPS
        if url.startswith('https://'):
            print("  ✅ Menggunakan HTTPS")
        else:
            print("  ⚠️  Pertimbangkan menggunakan HTTPS")
        
        # Check response headers
        response = requests.get(url, timeout=10, verify=True)
        
        security_headers = [
            'X-Frame-Options',
            'X-Content-Type-Options', 
            'Strict-Transport-Security',
            'Content-Security-Policy'
        ]
        
        print("\n  📋 Security Headers:")
        for header in security_headers:
            if header in response.headers:
                print(f"    ✅ {header}: {response.headers[header]}")
            else:
                print(f"    ⚠️  {header}: Not found")
        
        # Check server info exposure
        if 'Server' in response.headers:
            print(f"  ⚠️  Server info exposed: {response.headers['Server']}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    """Demo basic security checking"""
    
    print("="*50)
    print("BASIC WEBSITE SECURITY CHECKER")
    print("="*50)
    
    # Contoh website testing legal
    test_sites = [
        "https://httpbin.org",
        "https://example.com",
        "https://google.com"
    ]
    
    print("\n📡 Testing legal websites for educational purposes:\n")
    
    for site in test_sites:
        check_website_safety(site)
    
    print("\n" + "="*50)
    print("PELAJARAN:")
    print("1. HTTPS penting untuk enkripsi")
    print("2. Security headers mencegah serangan")
    print("3. Minimalkan info server yang diekspos")
    print("="*50)

if __name__ == "__main__":
    main()
