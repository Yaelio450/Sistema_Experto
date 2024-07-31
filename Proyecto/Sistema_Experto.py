animes = [
    {"titulo": "Naruto", "genero": ["Accion", "Aventura"], "duracion": "Largo", "anio": 2002},
    {"titulo": "Death Note", "genero": ["Misterio", "Suspenso"], "duracion": "Corto", "anio": 2006},
    {"titulo": "One Piece", "genero": ["Accion", "Aventura"], "duracion": "Largo", "anio": 1999},
    {"titulo": "Attack on Titan", "genero": ["Accion", "Drama"], "duracion": "Medio", "anio": 2013},
    {"titulo": "Dragon Ball", "genero": ["Accion", "Aventura"], "duracion": "Largo", "anio": 1989},
    {"titulo": "Madoka Magica", "genero": ["Seinen", "Suspenso"], "duracion": "Corto", "anio": 2011},
    {"titulo": "Tokyo Ghoul", "genero": ["Accion", "Drama"], "duracion": "Medio", "anio": 2014},
    {"titulo": "Code Geass", "genero": ["Accion", "Mechas"], "duracion": "Medio", "anio": 2006},
    {"titulo": "Vtuber Legend", "genero": ["Comedia", "Slice of life"], "duracion": "Corto", "anio": 2024},
    {"titulo": "Alya oculta sus sentimientos hablando en ruso", "genero": ["Comedia", "Romance"], "duracion": "Corto", "anio": 2024},
    {"titulo": "Bleach", "genero": ["Accion", "Seinen"], "duracion": "Larga", "anio": 2004},
    {"titulo": "Kotora-san", "genero": ["Comedia", "Slice of life"], "duracion": "Corto", "anio": 2013},
    {"titulo": "Chobits", "genero": ["Romance", "Slice of life"], "duracion": "Corto", "anio": 2002},
    {"titulo": "Berserk", "genero": ["Accion", "Seinen"], "duracion": "Medio", "anio": 1997},
    {"titulo": "Captain Tsubasa road to 2002", "genero": ["Spokon", "Deporte"], "duracion": "Largo", "anio": 2001},
    {"titulo": "Hajime no Ippo", "genero": ["Accion", "Deporte"], "duracion": "Largo", "anio": 2000},
    {"titulo": "Jujutsu Kaisen", "genero": ["Accion", "Seinen"], "duracion": "Largo", "anio": 2020},
    {"titulo": "Sword art online", "genero": ["Isekai", "Fantacia"], "duracion": "Largo", "anio": 2012},
    {"titulo": "Konosuba", "genero": ["Isekai", "Comedia"], "duracion": "Corto", "anio": 2016},
    {"titulo": "Cell at work", "genero": ["Accion", "Comedia"], "duracion": "Largo", "anio": 2021},
    {"titulo": "Re:zero", "genero": ["Isekai", "Seinen"], "duracion": "Largo", "anio": 2016},
    {"titulo": "Boku no pico", "genero": ["Yaoi", "OVA"], "duracion": "Corto", "anio": 2006},
    {"titulo": "High school DXD", "genero": ["Fantacia", "Ecchi"], "duracion": "Largo", "anio": 2012},
    {"titulo": "High school of the dead", "genero": ["Terror", "Ecchi"], "duracion": "Corto", "anio": 2010},
]

def recomendar_anime(preferencias, animes):
    recomendaciones = []
    for anime in animes:
        coincidencia = True
        if preferencias["genero"]:
            if not any(g in anime["genero"] for g in preferencias["genero"]):
                coincidencia = False
        if preferencias["duracion"] and anime["duracion"] != preferencias["duracion"]:
            coincidencia = False
        if preferencias["anio"] and anime["anio"] != preferencias["anio"]:
            coincidencia = False
        if coincidencia:
            recomendaciones.append(anime["titulo"])
    return recomendaciones

def obtener_preferencias():
    preferencias = {}
    preferencias["genero"] = input("¿Qué género prefieres? (separados por comas): ").split(", ")
    preferencias["duracion"] = input("¿Prefieres animes cortos, medios o largos?: ")
    anio = input("¿Tienes alguna preferencia de año de lanzamiento? (déjalo en blanco si no): ")
    preferencias["anio"] = int(anio) if anio else None
    return preferencias

def main():
    preferencias = obtener_preferencias()
    recomendaciones = recomendar_anime(preferencias, animes)
    if recomendaciones:
        print("Te recomendamos estos animes:")
        for reco in recomendaciones:
            print(reco)
    else:
        print("No encontramos animes que coincidan con tus preferencias.")

if __name__ == "__main__":
    main()


