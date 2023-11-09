import ipaddress  # Import the ipaddress module for IP address validation

# Function to calculate subnet mask based on the number of subnet bits
def calculate_subnet_mask(subnet_bits):
    subnet_mask = (2 ** 32 - 1) ^ (2 ** (32 - subnet_bits) - 1)
    return subnet_mask

# Main function
def main():
    try:
        # Get user input for an IP address
        ip_address = input("Enter an IP address: ")
        
        # Validate the IP address
        ipaddress.IPv4Address(ip_address)
        
        # Get user input for the number of subnet bits
        subnet_bits = int(input("Enter the number of subnet bits: "))
        
        # Validate the subnet bits input
        if subnet_bits < 0 or subnet_bits > 32:
            print("Invalid subnet bits. Please enter a number between 0 and 32.")
        else:
            # Call the calculate_subnet_mask function and display the result
            subnet_mask = calculate_subnet_mask(subnet_bits)
            print(f"Subnet mask for {subnet_bits} subnet bits: {subnet_mask}")
    except ValueError:
        # Handle invalid input (invalid IP address or non-integer subnet bits)
        print("Invalid IP address or subnet bits. Please enter valid inputs.")

# Entry point of the program
if __name__ == "__main__":
    # Call the main function
    main()