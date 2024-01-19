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

# nother example where json data is pickled and saved to s3 instead of local file
def pickle_to_s3(json_data):
    pickled= pickle.dumps(json_data)
    s3 = boto3.resource('s3')
    s3.Bucket('my-bucket').put_object(Key='my-key', Body=pickled)
    

# function to save a dataframe as a csv file to s3
def save_df_to_s3(df, bucket, key):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, key).put(Body=csv_buffer.getvalue())
    print(f"df saved to s3://{bucket}/{key}")

    # to use StringIO import StringIO from io

# function to get the pickled data from s3 and unpickle it

def get_pickled_data_from_s3(bucket, key):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, key)
    data = pickle.loads(obj.get()['Body'].read())
    return data

