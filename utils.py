import html
import re


def split_all(value: str, *delimiters) -> list:
    regP = '|'.join(map(re.escape, delimiters))
    return remove_empty_strs(re.split(regP, value))

def split_some(value: str, max_count: int = 0, *delimiters) -> list:
    regP = '|'.join(map(re.escape, delimiters))
    return remove_empty_strs(re.split(regP, value, max_count))

def contains_str(value: str, *sub_strs) -> bool:
    if sub_strs is None:
        return False
    try:    
        for current in sub_strs:
            if isinstance(current, str):
                if value.count(current) > 0:
                    return True
            else:
                if value.count(str(current)) > 0:
                    return True
        
        return False
    except Exception: return False

def remove_empty_strs(values: list) -> list:
    myStrs: list[str] = []
    for s in values:
        if not is_invalid_str(s):
            myStrs.append(s)

    return myStrs

def is_invalid_str(value: str) -> bool:
    return not value or len(value.strip()) == 0 or value.isspace()


def html_mono(value, *argv) -> str:
    return f"<code>{html.escape(str(value))}</code>" +  get_html_normal(*argv)

def html_in_parenthesis(value) -> str:
    if not value:
        return ": "
    return f" ({ html.escape(str(value))}): "

def html_bold(value, *argv) -> str:
    return f"<b>{html.escape(str(value))}</b>" + get_html_normal(*argv)


def html_italic(value, *argv) -> str:
    return f"<i>{html.escape(str(value))}</i>" + get_html_normal(*argv)

def html_link(value, link: str, *argv) -> str:
    if not isinstance(link, str) or len(link) == 0:
        return html_mono(value, *argv)
    return f"<a href={html.escape(link)}>{html.escape(str(value))}</a>" +  get_html_normal(*argv)


def get_html_normal(*argv) -> str:
    if argv is None or len(argv) == 0: return ""
    my_str = ""
    for value in argv:
        if isinstance(value, str):
            my_str += value
    
    return my_str

def html_normal(value, *argv) -> str:
    my_str = html.escape(str(value))
    for value in argv:
        if isinstance(value, str):
            my_str += value
    return my_str
