def remove(chars, s):
    for c in chars:
        s.replace(s, '')
    return s


def clean(s):
    if s:
        return remove(['\n', '\t'], s).strip()
    return None