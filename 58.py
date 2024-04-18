armin_scores = {
    "sakhteman dadeh": (18, 3),
    "mohandesi narmafzar": (16, 3),
    "vasaya": (8, 1),
    "nazarie zabanha": (18, 3),
    "mabani computer": (20, 2),
}

mahdyar_scores = {
    "sakhteman dadeh": (20, 3),
    "mohandesi narmafzar": (14, 3),
    "vasaya": (18, 1),
    "nazarie zabanha": (5, 3),
    "mabani computer": (16, 2),
}


def status(scores):
    for k, v in scores.items():
        if v[0] >= 10:
            print(k, ": Passed")
        else:
            print(k, ": Failed")


def average(scores):
    nomarat = [i[0] * i[1] for i in scores.values()]
    vahedha = [i[1] for i in scores.values()]
    avg = sum(nomarat) / sum(vahedha)
    print(avg)

average(armin_scores)
