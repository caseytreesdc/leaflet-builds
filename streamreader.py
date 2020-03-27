import sys


NVP_20200327 = {
    'preheader': 'plus, #blossombracket semifinals and always be sure to look for the helpers',
    'article-1__link': 'https://caseytrees.org/2020/03/semi-finals-of-our-blossom-bracket/?utm_source=leaflet&utm_medium=email&utm_campaign=spring',
    'article-1__alt-text': '#blossombracket semis',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2020/03/Cherry-March-Madness-Bracket-week-3_Leaflet-email.png',
    'article-1__heading': 'Semi-Finals of our Blossom Bracket',
    'article-1__description': 'The first contest is a doozy.',
    'article-2__link': 'https://caseytrees.org/2020/03/get-up-and-get-out-of-your-house-and-your-head/?utm_source=leaflet&utm_medium=email&utm_campaign=random',
    'article-2__alt-text': 'Trees and mental health',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/03/get-outside-email.jpg',
    'article-2__heading': 'Get Up and Get Out (of Your House and Your Head!)',
    'article-2__description': 'Spending time is nature can improve mental health, something practically all of us need these days.',
    'article-3__link': 'https://caseytrees.org/2020/03/look-for-the-helpers/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-3__alt-text': 'Always look for the helpers',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/03/helpers-email.png',
    'article-3__heading': 'Look for the Helpers',
    'article-3__description': 'A lot is uncertain these days, but there is a lot that is certain, including the power of those doing good'
}

NVP = NVP_20200327
#


def replacekeys(line):
    # built-in dictionary method that returns a list of its (key, value) tuple pairs
    for name, value in NVP.items():
        line = line.replace(f'%%{name}%%', value)

    return line


# read redirected standard input line by line

for line in sys.stdin:
    # stdout is redirected to > filename.html
    print(replacekeys(line), end='')

