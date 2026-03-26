def divide(a, b):
    print("debug:", a, b)
    return a / b


def load_user_name(config):
    try:
        return config["name"]
    except Exception:
        pass


def format_report(items):
    # TODO: support empty items better
    return ",".join(items)
