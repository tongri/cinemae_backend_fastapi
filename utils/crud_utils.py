from collections import namedtuple, defaultdict


def dict_fetch_all(cursor) -> list:
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def accumulated_dict_fetch_all(cursor) -> list[dict]:
    columns = [col[0] for col in cursor.description]
    return [flat_to_object_dict(dict(zip(columns, row))) for row in cursor.fetchall()]


def accumulated_dict_fetch_one(cursor) -> dict:
    if not (fetched := cursor.fetchone()):
        return {}
    columns = [col[0] for col in cursor.description]
    return flat_to_object_dict(dict(zip(columns, fetched)))


def named_tuple_fetchall(cursor) -> list:
    """Return all rows from a cursor as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def get_update_set_command(data_dict: dict) -> str:
    params = [" = ".join([k, f":{k}"]) for k in data_dict]
    return ", ".join(params)


def flat_to_object_dict(income_dict: dict) -> dict:
    res_dict = defaultdict(dict)
    for k, v in income_dict.items():
        namings = k.split("__")
        if len(namings) > 1:
            res_dict[namings[0]][namings[1]] = v
        else:
            res_dict[k] = v

    return res_dict
