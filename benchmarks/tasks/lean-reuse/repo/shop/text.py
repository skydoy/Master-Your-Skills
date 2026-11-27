import unicodedata


def slugify(name):
    """'São Paulo Lda.' -> 'sao-paulo-lda'"""
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    words = "".join(c if c.isalnum() else " " for c in ascii_name.lower()).split()
    return "-".join(words)
