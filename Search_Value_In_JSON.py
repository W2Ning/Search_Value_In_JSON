import json
import jsonpath
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', type=str, help="The json file you wanna to analysis")
parser.add_argument('--key', '-k', type=str, help="The key you wanna to search")

args = parser.parse_args()

keyname_jsonpath = "$.." + args.key


with open(file=args.file, mode='r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)


value_list = jsonpath.jsonpath(json_data,keyname_jsonpath)

f=open("result.txt","w")

for line in value_list:
    f.write(line+'\n')

print(*value_list,sep = '\n')
