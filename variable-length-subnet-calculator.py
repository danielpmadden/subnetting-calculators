# Function to calculate subnet masks for multiple subnets with different sizes (VLSM)
def calculate_subnet_masks(subnets):
    subnet_masks = []
    for subnet in subnets:
        subnet_mask = (2 ** 32 - 1) ^ (2 ** (32 - subnet) - 1)
        subnet_masks.append(subnet_mask)
    return subnet_masks

# Main function
def main():
    try:
        # Get user input for subnet bits of multiple subnets (space-separated)
        subnets = list(map(int, input("Enter subnet bits for multiple subnets (space-separated): ").split()))
        
        # Validate subnet bits input
        for subnet in subnets:
            if subnet < 0 or subnet > 32:
                print(f"Invalid subnet bits {subnet}. Please enter numbers between 0 and 32.")
                return
        
        # Call the calculate_subnet_masks function and display the results
        subnet_masks = calculate_subnet_masks(subnets)
        for i, subnet_mask in enumerate(subnet_masks):
            print(f"Subnet mask for subnet {i + 1} ({subnets[i]} bits): {subnet_mask}")
    except ValueError:
        # Handle invalid input (non-integer subnet bits)
        print("Invalid input. Please enter valid subnet bits.")

# Entry point of the program
if __name__ == "__main__":
    # Call the main function
    main()