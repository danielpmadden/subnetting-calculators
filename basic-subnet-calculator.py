# Function to calculate subnet mask based on the number of subnet bits

MAX_SUBNET_BITS = 32 

def get_subnet_bits():
    # Prompt user for subnet bits and validate input
    
    while True:
        print("Enter the number of subnet bits (0-32):")
        num_bits = input()
        
        try:
            num_bits = int(num_bits)
            if 0 <= num_bits <= MAX_SUBNET_BITS:
                return num_bits
        except ValueError:
            pass
        
        print("Invalid input. Enter an integer between 0 and {MAX_SUBNET_BITS}.")

def calculate_subnet_mask(num_subnet_bits):
    # Calculate subnet mask from number of subnet bits
    
    return (2**32 - 1) ^ (2**(32 - num_subnet_bits) - 1)

def print_subnet_mask(num_subnet_bits, subnet_mask):
    # Print subnet mask info to console
    
    print("Subnet mask for {num_subnet_bits} subnet bits: {subnet_mask}")
    
def main():
    # Prompt for subnet bits, calculate and display subnet mask
    
    num_subnet_bits = get_subnet_bits()
    subnet_mask = calculate_subnet_mask(num_subnet_bits)
    print_subnet_mask(num_subnet_bits, subnet_mask)

if __name__ == "__main__":
    main()
