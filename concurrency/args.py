def function(a, b, keyword=True, **kwargs):
    print(a, b)
    print(args)
    print(keyword)
    print(kwargs)


d = {"param_a": 43, "param_b": 44}
function(1, 2, *[5, 3, 4], param=42, **d)


import json
import pathlib


def dict_to_config(dictionary, file="config.json", verbose=False, **kwargs):
    # kwargs passed to json.dumps
    json_txt = json.dumps(dictionary, **kwargs)
    if verbose:
        print(json.txt)
    pathlib.Path(file).write_text(json_txt)


dict_to_config({"a": 1, "b": 2}, verbose=True, indent=2)
