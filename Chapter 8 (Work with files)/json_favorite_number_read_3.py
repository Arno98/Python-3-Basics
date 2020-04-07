import json

file_number = "love_number.json"
with open(file_number) as file_doc_number:
	read_number = json.load(file_doc_number)
	print(read_number)
