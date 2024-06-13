import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read("config.txt")
    params = {
        "m": config.getfloat("parameters", "m"),
        "k": config.getfloat("parameters", "k"),
        "b": config.getfloat("parameters", "b"),
        "f": config.getfloat("parameters", "f"),
        "x0": config.getfloat("parameters", "x0"),
        "v0": config.getfloat("parameters", "v0"),
        "t_max": config.getfloat("parameters", "t_max"),
        "h": config.getfloat("parameters", "h")
    }
    return params