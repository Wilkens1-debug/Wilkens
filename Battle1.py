def retire_espas(Blok):
    Blok_san_espas = ''.join(Blok.split())
    return Blok_san_espas

Blok = """
        Badio Wilkens gen pou email wbadio693@gmail.
    """

Blok_san_espas = retire_espas(Blok)
print(Blok_san_espas)
