import json
import os
import pickle

def read_json(path):
    file_name = path
    with open(file_name) as f:
        data = json.load(f)
    return path

def read_all_json_files(path):
    all_json_files = []
    for file in os.listdir(path):
        full_file_name = os.path.join(path, file)
        with open(full_file_name, 'r') as f2:
            data2 = json.load(f2)
            all_json_file.append(data2)
    return (all_json_files)

def write_pickle(path):
    path = os.path.join(obj,file, [protocol])
    pickle.dump(a,b,protocol)

    return super_smash_characters.pickle
def load_pickle(path):
    return pickle.loads(path)
