def get_num_words(content):
    tokens = content.split()
    return len(tokens)


def get_occurrences_map(content):
    omap = {}

    tokens = content.split()
    for token in tokens:
        characters = list(token)
        for ch in characters:
            k = ch.lower()
            val = omap.get(k, 0)
            omap[k] = val + 1

    return omap


def sort_on(items):
    return items["num"]


def get_char_counts(omap):
    char_counts = []

    for char in omap:
        curr_map = {"char": char, "num": omap[char]}
        char_counts.append(curr_map)

    char_counts.sort(reverse=True, key=sort_on)
    return char_counts
