import json
import os
import pickle

#Part A
def read_json(path):
    file_name = path
    with open(file_name) as f:
        data = json.load(f)
    return data

read_json('/Users/nli/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json')

#Part B
def read_all_json_files(path):
    all_json_files = []
    for file in os.listdir(path):
        full_file_name = os.path.join(path, file)
        with open(full_file_name, 'r') as f2:
            data2 = json.load(f2)
            all_json_files.append(data2)
    return (all_json_files)

#Part C
path = '/Users/asamra/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json'
data = 'super_smash_characters.pickle'

def write_pickle(path, data):
    output_file = open(b'super_smash_characters.pickle', 'wb')
    pickle.dump(path, output_file)
    output_file.close()

write_pickle(path, data)

#Part D
def load_pickle(my_pickle):
    path = open('super_smash_characters.pickle', 'wb')
    pickle. dumps(int(my_pickle), path)
    print(path)

    # return pickle.loads(path)

load_pickle('/Users/nli/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')
