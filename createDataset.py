import random

def generate_data(x, y, z, filename):
    if y > x:
        raise ValueError("Number of unique values (y) cannot be greater than total number of values (x).")

    # Generates a list of non unique numbers
    non_unique_numbers = []

    for i in range(z):
        non_unique_numbers += list(range(1, x + 1))  # You can customize the range as needed
    
    unique_numbers=[]

    # Create a list with unique numbers and add duplicates    
    data = non_unique_numbers + [_ for _ in range(x + 1, x + (y + 1))]

    # Shuffle the list to intersperse unique numbers randomly
    random.shuffle(data)

    # Write the data to the text file
    with open(filename, 'w') as file:
        for number in data:
            file.write(f"{number}\n")

x = 100000  # Number of non-unique numbers to generate
y = 10000  # Number of unique numbers to generate
z = 3    # Number of times non-unique numbers should appear in dataset

filename = 'dataset.txt'  # Output file

generate_data(x, y, z, filename)
