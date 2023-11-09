# Function to calculate subnet mask based on the number of subnet bits
def calculate_subnet_mask(subnet_bits):
    subnet_mask = (2 ** 32 - 1) ^ (2 ** (32 - subnet_bits) - 1)
    return subnet_mask

# Function to calculate CIDR notation based on the network address and significant bits
def calculate_cidr(network_address, subnet_bits):
    network = ipaddress.IPv4Network(f"{network_address}/{subnet_bits}", strict=False)
    return network

# Main function for the subnetting calculator
def subnet_calculator():
    try:
        # User input for selecting the calculator type
        choice = int(input("Select Calculator:\n1. Subnet Calculator\n2. Subnet Calculator with IP Address Validation\n3. VLSM Calculator\n4. CIDR Calculator\nEnter your choice: "))
        
        # Subnet Calculator
        if choice == 1:
            subnet_bits = int(input("Enter the number of subnet bits: "))
            subnet_mask = calculate_subnet_mask(subnet_bits)
            print(f"Subnet mask for {subnet_bits} subnet bits: {subnet_mask}")
        
        # Subnet Calculator with IP Address Validation
        elif choice == 2:
            ip_address = input("Enter an IP address: ")
            ipaddress.IPv4Address(ip_address)  # Validate the IP address
            subnet_bits = int(input("Enter the number of subnet bits: "))
            subnet_mask = calculate_subnet_mask(subnet_bits)
            print(f"Subnet mask for {subnet_bits} subnet bits: {subnet_mask}")
        
        # VLSM Calculator
        elif choice == 3:
            subnets = list(map(int, input("Enter subnet bits for multiple subnets (space-separated): ").split()))
            for subnet in subnets:
                subnet_mask = calculate_subnet_mask(subnet)
                print(f"Subnet mask for {subnet} subnet bits: {subnet_mask}")
        
        # CIDR Calculator
        elif choice == 4:
            network_address = input("Enter network address (e.g., 192.168.1.0): ")
            subnet_bits = int(input("Enter the number of significant bits: "))
            cidr_network = calculate_cidr(network_address, subnet_bits)
            print(f"CIDR Notation: {cidr_network}")
        
        else:
            print("Invalid choice. Please select a valid option.")
    
    except ValueError:
        print("Invalid input. Please enter valid values.")

# Entry point of the program
if __name__ == "__main__":
    subnet_calculator()