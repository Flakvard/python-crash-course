favorite_language = {
    'Jen':'python',
    'Sarah':'c',
    'edward':'ruby',
    'phil':'c++'
}
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_language.keys():
    print(name)

if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll")

for name in sorted(favorite_language.keys(),reverse=True):
    print(f"{name.title()} thank you for taking our poll.")

print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language)

favorite_language = {
    'Jen':['python','ruby','C#'],
    'Sarah':['c','go'],
    'edward':['ruby'],
    'phil':['c++','c']
}
for name, languages in favorite_language.items():
    print(f"\n{name.title()}'s favourite language are:")
    for language in languages:
        print(f"{language.title()}")