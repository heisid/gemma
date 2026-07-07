from time import strftime, localtime


def get_current_time() -> str:
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

EXTRA_TOOLS = {
    'get_current_time': get_current_time,
}