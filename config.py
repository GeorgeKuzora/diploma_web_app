from dotenv import dotenv_values


def config_load():
    config = dotenv_values(".env.mysql")
    return config
