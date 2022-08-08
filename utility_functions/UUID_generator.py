import uuid 

def generate_random_string():
    # Convert a UUID to a string of hex digits in standard form
    uuid_string = str(uuid.uuid4()).replace("-","")
    # print(uuid_string)
    return uuid_string

# generate_random_string()