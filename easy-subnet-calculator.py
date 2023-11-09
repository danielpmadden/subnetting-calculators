def subnet_calculator():
    try:
        # Get network IP address from the user
        network_ip = input("Enter network IP address (e.g., 192.168.1.0): ")
        network = ipaddress.IPv4Network(network_ip, strict=False)  # Create an IPv4 network object
        
        # Get the number of subnet bits from the user
        subnet_bits = int(input("Enter the number of subnet bits: "))
        
        # Calculate subnet mask, network address, and broadcast address
        subnet_mask = network.netmask
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        
        # Display the results
        print(f"Subnet Mask: {subnet_mask}")
        print(f"Network Address: {network_address}")
        print(f"Broadcast Address: {broadcast_address}")
        
    except ValueError:
        print("Invalid input. Please enter valid values.")

# Entry point of the program
if __name__ == "__main__":
    subnet_calculator()