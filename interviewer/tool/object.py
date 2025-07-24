def sortKeys(json):
    """
    排序JSON数据的函数，包括其嵌套的对象和数组, 默认会移除值为None的健
    """
    if isinstance(json, dict):
        # 对字典类型进行排序，以及递归排序其值，如果它们可迭代
        return {key: sortKeys(value) for key, value in sorted(json.items()) if value is not None}
    elif isinstance(json, list):
        # 对于列表，只需排序其中可能嵌套的项目
        return [sortKeys(item) for item in json]
    else:
        # 不是字典或列表，直接返回原始数据
        return json


def safeGet(d, *args):
    """
    安全地获取嵌套JSON对象中的值。
    :param d: 待查询的字典或JSON对象
    :param args: 键的列表，表示要查询的路径
    :return: 如果找到指定路径的值，则返回该值；否则，返回None
    """
    if d is None:
        return None

    if len(args) == 0:
        return None

    v = d
    for key in args:
        if key in v:
            v = v[key]
        else:
            return None
    return v


def concat(*args):
    """
    接受变长参数，将各种类型按顺序拼接成字符串，并编码成字节。
    """
    concatenated_string = ''.join(map(str, args))
    return concatenated_string.encode()


def composite(*byte_arrays):
    """
    将多个字节数组拼接成一个新的字节数组。
    """
    return b''.join(byte_arrays)
