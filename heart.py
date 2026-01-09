def print_heart():
    # Define the range for the heart shape
    # The mathematical equation for a heart is complex, this uses a pattern approximation
    for row in range(6):
        for col in range(7):
            # Conditions to determine where to print a star
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or \
               (row - col == 2) or (row + col == 8):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print() # Move to the next line after each row

if __name__ == "__main__":
    print_heart()

