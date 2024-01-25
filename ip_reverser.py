import os

def reverse_ip(ip):
    segments = ip.split('.')
    reversed_segments = segments[::-1]
    reversed_ip = '.'.join(reversed_segments)
    return reversed_ip

def reverse_ips(input_file, output_file):
    with open(input_file, 'r') as file:
        ips = file.readlines()
    
    reversed_ips = [reverse_ip(ip.strip()) for ip in ips]
    
    # Check if the output file exists, create it if necessary
    if not os.path.exists(output_file):
        with open(output_file, 'w'):
            pass
    
    with open(output_file, 'w') as file:
        file.write('\n'.join(reversed_ips))

if __name__ == '__main__':
    input_file = 'C:\\temp\\scripts\\2023-all-ips.txt'  # Replace with your input file path
    output_file = 'C:\\temp\\scripts\\2023-all-ips_output.txt'  # Replace with your output file path
    
    reverse_ips(input_file, output_file)
