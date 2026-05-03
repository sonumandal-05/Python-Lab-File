# 5. Create a dictionary where the key hods the name of the countries and value indicates the language most spoken in
# the corresponding country. Take first input as the no. of key value pairs to be added in the dictionary. Write a program 
# to print the content of this dictionary in such a way that the key is sorted in the ascending order. 




size = int(input("Enter the number of key-value pairs to be added in the dictionary: "))
country_language_dict = {}
for _ in range(size):
    country = input("Enter country name: ")
    language = input("Enter most spoken language in that country: ")
    country_language_dict[country] = language
for country in sorted(country_language_dict.keys()):
    print(f"{country} - {country_language_dict[country]}")
    