# Joshua Furman
from os.path import exists

# Checks if a string is a floating point num
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Convert config values to correct Bool value
def convert_bool(data):
    true_values = ['true', 'on', 'yes']
    false_values = ['false', 'off', 'no']

    if data.lower() in true_values:
        return True
    elif data.lower() in false_values:
        return False
    else:
        return None

# Check if config value needs to be converted to proper Bool
def detect_bool(data):
    bool_checks = ['true', 'false', 'on', 'off', 'yes', 'no']
    if data.lower() in bool_checks:
        return True
    return False

def parse_file(filename):
    config_data = {}
    with open(filename, 'r') as file:
        for line in file:
            if not line.strip() or '#' in line: # ignore blank lines and commented lines
                continue

            data = line.split(sep='=', maxsplit=2) # split config names and vals
            
            if data[1].strip().isdigit(): # check if config val is an Int
                config_data[data[0].strip()] = int(data[1].strip())

            elif isfloat(data[1].strip()):  # check if config val is a float
                    config_data[data[0].strip()] = float(data[1].strip())

            elif detect_bool(data[1].strip()): # check if config val needs to be converted to a Bool
                config_data[data[0].strip()] = convert_bool(data[1].strip())

            else:
                config_data[data[0].strip()] = data[1].strip()

    return config_data
 
def main():
    config_file = ''
    # Make sure file exists
    while True:
        config_file = input('Please type which file to parse: ').strip()

        if exists(config_file):
            parsed_data = parse_file(config_file)
            break
        else:
            print('That file does not exist. Please try again.\n')

    for key, value in parsed_data.items():
        print(f'{key} is set to: {value}')

if __name__ == "__main__":
    main()
