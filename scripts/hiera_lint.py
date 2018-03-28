import sys, yaml

errors = False

with open(sys.argv[1], 'r') as stream:
    try:
        y = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for item in y['development']:
    if item['hiera_name'].find('.') != -1:
        print("Syntax Error! Character '.' found in hiera_name value '%s'" % item['hiera_name'])
        errors = True

for item in y['production']:
    if item['hiera_name'].find('.') != -1:
        print("Syntax Error! Character '.' found in hiera_name value '%s'" % item['hiera_name'])
        errors = True

if errors:
    sys.exit(1)
else:
    print('No errors found.')
    sys.exit(0)
