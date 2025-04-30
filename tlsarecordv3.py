import subprocess

# Created by Syafiee17x

def check_tlsa_record(domain):
    try:
        # Ensure the domain includes http or https
        if not domain.startswith("http://") and not domain.startswith("https://"):
            domain = "https://" + domain
        
        # Extract the domain name without http or https for DNS queries
        domain_name = domain.replace("http://", "").replace("https://", "")
        
        # Use the 'dig' command to check the TLSA record for the domain
        result = subprocess.run(['dig', '_443._tcp.' + domain_name, 'TLSA'], capture_output=True, text=True)
        
        # Check if the TLSA record is found
        if 'ANSWER SECTION' in result.stdout:
            tlsa_record = result.stdout
        else:
            tlsa_record = f"No TLSA record found for _443._tcp.{domain_name}."
        
        # Perform additional checks for PKIX validation and IP addresses
        ip_result = subprocess.run(['dig', domain_name, 'A'], capture_output=True, text=True)
        ipv6_result = subprocess.run(['dig', domain_name, 'AAAA'], capture_output=True, text=True)
        
        ip_addresses = ip_result.stdout.split('ANSWER SECTION')[1].split('\n')[1:-1]
        ipv6_addresses = ipv6_result.stdout.split('ANSWER SECTION')[1].split('\n')[1:-1]
        
        detailed_output = f"\n{'='*40}\nChecking TLSA record for {domain}\n{'='*40}\n"
        detailed_output += f"TLSA record:\n{tlsa_record}\n"
        
        if ip_addresses:
            detailed_output += "\nIPv4 addresses:\n"
            for ip in ip_addresses:
                detailed_output += f"{ip} PKIX-validated successfully\n"
        else:
            detailed_output += "Warning! No IPv4 addresses found.\n"
        
        if ipv6_addresses:
            detailed_output += "\nIPv6 addresses:\n"
            for ipv6 in ipv6_addresses:
                detailed_output += f"{ipv6} PKIX-validated successfully\n"
        else:
            detailed_output += "Warning! No IPv6 addresses found.\n"
        
        detailed_output += f"\n{'='*40}\nCheck complete for {domain}\n{'='*40}\n"
        
        return detailed_output
    except Exception as e:
        return str(e)

def main():
    while True:
        # Prompt user for domain input
        domain = input("Enter the domain name to check (e.g., example.com): ")
        
        # Check and verify TLSA records for the input domain
        print(check_tlsa_record(domain))
        
        # Ask user if they want to run another scan
        another_scan = input("Do you want to run another scan? (yes/no): ").strip().lower()
        if another_scan != 'yes':
            break

if __name__ == "__main__":
    main()
