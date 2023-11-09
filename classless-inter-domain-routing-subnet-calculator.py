import ipaddress  # Import the ipaddress module for IP address manipulation

# Function to calculate CIDR notation based on the network address and significant bits
def calculate_cidr(network_address, subnet_bits):
    # Calculate the CIDR network using ipaddress module
    network = ipaddress.IPv4Network(f"{network_address}/{subnet_bits}", strict=False)
    return network

# Main function
def main():
    try:
        # Get user input for network address
        network_address = input("Enter network address (e.g., 192.168.1.0): ")
        
        # Get user input for significant bits
        subnet_bits = int(input("Enter the number of significant bits: "))
        
        # Validate the significant bits input
        if subnet_bits < 0 or subnet_bits > 32:
            print("Invalid number of significant bits. Please enter a number between 0 and 32.")
            return
        
        # Call the calculate_cidr function and display the CIDR notation
        cidr_network = calculate_cidr(network_address, subnet_bits)
        print(f"CIDR Notation: {cidr_network}")
    except ValueError:
        # Handle invalid input (invalid IP address or non-integer significant bits)
        print("Invalid input. Please enter valid network address and significant bits.")

# Entry point of the program
if __name__ == "__main__":
    # Call the main function
    main()