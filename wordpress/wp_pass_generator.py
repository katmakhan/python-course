# # Example usage
# custom_substrings = ["user", "home", "123"]
# custom_special_chars = "!@#"
# password_dict = generate_password_dictionary(
#     min_length=8,
#     max_length=12,
#     custom_substrings=custom_substrings,
#     custom_special_chars=custom_special_chars,
#     max_uppercase=3,
#     max_special=2
# )

# save_password_dict_to_json(password_dict, "password_dictionary.json")
# print("Password dictionary saved to 'password_dictionary.json'.")



import string
import itertools
import json

custom_substrings = ["admin", "user"]
number_list=["1","2","3","4","5","6","7","8","9","0"]
special_chars = ["$", "@", "#", "!", "*"]
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)

def generate_custom_strings(total_length):
	# char_pool = special_chars + uppercase_letters + lowercase_letters
	char_pool = special_chars+ number_list
	custom_strings = {}
	for substring in custom_substrings:
		print("Substring is ",substring)
		for combo in itertools.product(char_pool, repeat=total_length - len(substring)):
			custom_string = substring + "".join(combo)
			custom_strings[custom_string] = None
			print(custom_string)
		# break
	return custom_strings


# Example usage
result_data=generate_custom_strings(12)

# Write the JSON data to a file
with open("password_wordlist.json", "w") as f:
	json.dump(result_data, f, indent=4)

print("Done..")

