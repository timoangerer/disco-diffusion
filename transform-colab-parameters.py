from redbaron import RedBaron
import argparse

parser = argparse.ArgumentParser(description='Extract parameters from google cloab notebook.')
parser.add_argument('input_file', type=argparse.FileType('r'))
parser.add_argument('dest_file', type=argparse.FileType('w'))
args = parser.parse_args()
print("Received args: ", args, "\n")

with args.input_file as source_code:
    red = RedBaron(source_code.read())

paramComments = red.findAll("CommentNode", value=lambda value: value.startswith("#@param"))
print("Number of params:", len(paramComments), "\n")

print("Extracted defaults")
defaults = dict()
for comment in paramComments:
    variable_name = str(comment.previous.target.value)
    variable_value = comment.previous.value
    print(f'{variable_name}: {variable_value}')
    defaults[variable_name] = variable_value

for comment in paramComments:
    variable_name = comment.previous.target.value
    variable_value = comment.previous.value
    comment.previous.value.value = f'cfg.{variable_name}'

with args.dest_file as source_code:
    source_code.write(red.dumps())