from deep_translator import GoogleTranslator as G


def eng(text):
    tarjima = G(source="uz", target="en").translate(text)
    return tarjima
def uz(text):
    tarjima = G(source="en", target="uz").translate(text)
    return tarjima


def ru(text):
    tarjima = G(source="uz", target="ru").translate(text)
    return tarjima
def ru_uz(text):
    tarjima = G(source="ru", target="uz").translate(text)
    return tarjima