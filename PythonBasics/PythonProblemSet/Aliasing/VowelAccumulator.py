
input_string=input("Enter any Text ")
vowels="aeiouAEIOU"
vowel_accumulator=""

for char in input_string:
    if char in vowels:
        vowel_accumulator=vowel_accumulator + char

print(vowel_accumulator)