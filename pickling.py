# exmple of pickle from "The quick python book" pg 183

import pickle


def save_data():
    global a, b, c
    file = open("state", "wb")
    data = {"a": a, "b": b, "c": c}
    pickle.dump(data, file)
    file.close()


def restore_data():
    global a, b, c
    file = open("state", "rb")
    data = pickle.load(file)
    file.close()
    a = data["a"]
    b = data["b"]
    c = data["c"]


# another example


def pickel2():

    data = {
        "a": [1, 2.0, 3, 4 + 6j],
        "b": ("caharcter string", b"byte string"),
        "c": {None, True, False},
    }

    with open("data.pickle", "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

    with open("data.pickle", "rb") as f:
        saved_data = pickle.load(f)

    print(saved_data)


# pickel2()
