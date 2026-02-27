rivers = {
    'yangtze': 'china',
    'volga': 'russia',
    'mississippi': 'united states',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nCountries included in this data set:")
for country in rivers.values():
    print("- " + country.title())
