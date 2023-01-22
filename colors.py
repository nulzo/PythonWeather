colors = {
    "Classic":{
        "Charm":111,
        "Cake":230,
        "Chaos":220,
        "Caution":124,
        "Cove":29,
        "Coral":175
    },
    "Modern":{
        "White":255,
        "Faux-Fur":188,
        "Sugar":231,
        "Marble":195,
        "Satin":189,
        "Plush":225

    },
    "Grayscale":{
        "Black":232,
        "Shadow":234,
        "Iron":238,
        "Stone":242,
        "Concrete":250,
        "White":254
    },
    "Weather":{
        "Overcast":59,
        "Mist":60,
        "Clear":45,
        "Sunny":11,
        "Light Snow":66,
        "Blizzard":75,
        "Cloudy":59,
        "Partly cloudy":61,
        "Snow":63,
        "Fog":15
    },
    "Temperature":{
        "Extremecold":17,
        "Freezing":19,
        "Cold":21,
        "Chilly":25,
        "Moderate":27,
        "Normal":36,
        "Temperate":72,
        "Warm":70,
        "Verywarm":11,
        "Hot":88,
        "Veryhot":52
    },
    "MISC":{
        "Error":160,
        "Success":118,
        "Loading":190
    }
}

def cringePrinter():
    i = 1
    print()
    print("MODERN PALETTE:")
    for k, v in colors["Modern"].items():
        if i % 3 == 0:
            print(f'\x1b[38;5;{v}m' + str(f"{k}") + u'\u001b[0m', end='\n')
        else:
            print(f'\x1b[38;5;{v}m' + str(f"{k}") + u'\u001b[0m', end=' ')
        i += 1
    print()
    print("CLASSIC PALETTE:")
    for k, v in colors["Classic"].items():
        if i % 3 == 0:
            print(f'\x1b[38;5;{v}m' + str(f"{k}") + u'\u001b[0m', end='\n')
        else:
            print(f'\x1b[38;5;{v}m' + str(f"{k}") + u'\u001b[0m', end=' ')
        i += 1
    print()
    print("GRAYSCALE PALETTE:")
    for k, v in colors["Grayscale"].items():
        if i % 3 == 0:
            print(f'\x1b[38;5;{v}m' + str(f"{k}") + u'\u001b[0m', end='\n')
        else:
            print(f'\x1b[38;5;{v}m' + str(f"{k}") + u'\u001b[0m', end=' ')
        i += 1
    print("TEMP PALETTE:")
    for k, v in colors["Temperature"].items():
        if i % 3 == 0:
            print(f'\x1b[38;5;{v}m' + str(f"{k}") + u'\u001b[0m', end='\n')
        else:
            print(f'\x1b[38;5;{v}m' + str(f"{k}") + u'\u001b[0m', end=' ')
        i += 1
    print()

def getPalette(color):
    for key in colors:
        for k in colors[key]:
            if color == k:
                palette = key
                return palette
    return None


def cringe(text, color=None, palette=None):
    try:
        if palette is None:
            palette = getPalette(color)
        return str(f'\x1b[38;5;{colors[palette][color]}m' + str(f"{text}") + u'\u001b[0m')
    except:
        return "!!! COLOR ERROR !!!"