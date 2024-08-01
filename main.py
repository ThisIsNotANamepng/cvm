import cvm_count

def test_estimate(word_list):
    
    #create a CVM class object, specifying the threshold - the number of elemenets that can be stored in a set.
    counter = cvm_count.CVM(threshold=1000)

    for word in word_list:
        #use the method `record` to go through each element
        counter.record(word)

    actual_num_unique = len(set(word_list))
    #use the method `estimate` to estimate the number unique elements seen so far.
    estimated_num_unique = counter.estimate()

    print('Actual =', actual_num_unique, ', Estimated =', estimated_num_unique)
    print('Difference =', actual_num_unique - estimated_num_unique)
    print('Difference perc =', round(100*(actual_num_unique - estimated_num_unique)/actual_num_unique, 2))
    print('Num rounds =', counter._num_rounds)

def read_ebook(file_path):
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Remove leading and trailing whitespace
            if line:  # Check if the line is not empty
                words.extend(line.split())  # Split the line into words and add to the list
    return words

# Example usage:
file_path = 'dataset.txt'  # Replace with the path to your UTF-8 encoded text file
words_list = read_ebook(file_path)

test_estimate(words_list)
