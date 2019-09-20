import json

def write_obj_to_json(target_obj, out_path, indent=0):
    with open(out_path, "w") as out_stream:
        json.dump(target_obj, out_stream, indent=indent)