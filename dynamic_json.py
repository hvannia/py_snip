import json

# bool must
# bool should
# bool must
# names w/o score
# ids
# bool should
# other conditions


def build_elastic_query(
    must_shoud_must_conditions,
    must_shoud_conditions,
    must_conditions,
    should_counditions,
):
    # this is always required
    x = {
        "bool": {
            "must": [
                {
                    "bool": {
                        "should": {
                            # always included names
                            "bool": {"must": must_shoud_must_conditions}
                        }
                    }
                }
            ]
        }
    }
    # build from inner

    # do concatenate list of dict
    ld1 + ld2
