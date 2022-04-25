# Python 3.10 
import random_user

user = {"name": {
    "first":"vannia", "last":"hernandez"
    }, "title":"Python 3.10 release manager"
}

match user: 
    case {"name":{"first":first_name}}


# from random_user
def get_age(user):
     """Get the age of a user, adapt to version 
        # Version 1.1
        "dob": "1966-04-17 11:57:01"
        # Version 1.3
        "dob": {"date": "1957-05-20T08:36:09.083Z", "age": 64}
     """
    match user:
        case {"dob": {"age": int(age)}}:
        return age
    case {"dob": dob}:
        now = datetime.now()
        dob_date = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S")
        return now.year - dob_date.year


