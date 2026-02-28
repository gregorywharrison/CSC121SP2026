favorite_places = {
    'eric': ['newport', 'los angeles'],
    'carolina': ['asheville', 'tokyo'],
    'kimbo': ['crabtree', 'cataloochee'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")
