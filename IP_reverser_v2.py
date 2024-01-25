import os

def reverse_ip(ip):
    if ip.endswith('.0'):
        return ip  # Skip IPs ending with '.0'
    
    segments = ip.split('.')
    reversed_segments = segments[::-1]
    reversed_ip = '.'.join(reversed_segments)
    return reversed_ip

def reverse_ips(input_file, output_file):
    with open(input_file, 'r') as file:
        ips = file.readlines()
    
    reversed_ips = [reverse_ip(ip.strip()) for ip in ips if not ip.strip().endswith('.0')]
    
    # Check if the output file exists, create it if necessary
    if not os.path.exists(output_file):
        with open(output_file, 'w'):
            pass
    
    with open(output_file, 'w') as file:
        file.write('\n'.join(reversed_ips))

if __name__ == '__main__':
    # Prompt the user for input and output file names
    input_file = input("Which file do you want to reverse the IPs for? ")
    
    # Extract the filename from the path
    filename = os.path.splitext(os.path.basename(input_file))[0]
    
    # Create the output file name automatically
    output_file = f'{filename}_output.txt'
    
    reverse_ips(input_file, output_file)
