from collections import Counter
def frequency_analysis(ciphertext):
    freq = Counter(ciphertext)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq
# Example usage
ciphertext = "ZEBRAS ARE BEAUTIFUL ANIMALS"
freq_list = frequency_analysis(ciphertext.replace(" ", ""))
print("Letter frequencies:", freq_list)

#Output:
Letter frequencies: [('A', 5), ('E', 3), ('B', 2), ('R', 2), ('S', 2), ('U', 2), ('I', 2), ('L', 2), ('Z', 1), ('T', 1), ('F', 1), ('N', 1), ('M', 1)]
