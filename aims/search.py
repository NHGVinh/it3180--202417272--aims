
def search_by_category(dvds, category):
    return [
        dvd for dvd in dvds
        if category.lower() in dvd.category.lower()
    ]


def search_by_title(dvds, keyword):
    return [
        dvd for dvd in dvds
        if keyword.lower() in dvd.title.lower()
    ]
