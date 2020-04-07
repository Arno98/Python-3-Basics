import json

with open("number_writer.json") as object_file:
	number_read = json.load(object_file)
	print(number_read)
