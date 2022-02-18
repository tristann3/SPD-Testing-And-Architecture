def extract_position(line):
    if not isinstance(line, str):
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else:
                pos = None
    return pos

def test_extract_position_debug():
    line = 'debug'
    assert extract_position(line) == None

def test_extract_position_hello_world():
    line = 'x:hello_world'
    assert extract_position(line) == 'hello_world'

def test_extract_position_none():
    line = None
    assert extract_position(line) == None

def test_extract_position_not_string_type():
    line = 1
    assert extract_position(line) == None

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)
