import re


def clean_string_line_breakers(input_string):
    cleaned_string = re.sub(r'\n{2,}', '\n\n', input_string)
    return cleaned_string.strip()


def clean_string_spaces(input_string):
    cleaned_string = re.sub(r' +', ' ', input_string)
    cleaned_string = re.sub(r'\n', '', cleaned_string)
    return cleaned_string.strip()
