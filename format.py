import re
import sys


def up_number(value, type_update=None):
    if type_update == 'major':
        return f"{int(value[0])+1}.0.0"
    elif type_update == 'minor':
        return f"{value[0]}.{int(value[1])+1}.0"
    return f"{value[0]}.{value[1]}.{int(value[2])+1}"


with open(sys.argv[1]) as f:
    first_occur = next(x for x in f.read().split('\n') if re.findall('v\\d+\\.\\d+\\.\\d+ ', x))
    last_value = re.sub('(^.*v|\\s+\\(.*\\).*$)', '', first_occur).split('.')

if len(sys.argv) > 3:
    print(up_number(last_value, sys.argv[2]))
else:
    print(up_number(last_value))
