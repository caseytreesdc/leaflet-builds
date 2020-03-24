import sys

NVP_20200324 = {
    'preheader': 'trees are growing',
    'article-1__link': 'https://caseytrees.org/',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2020/03/Cherry-March-Madness-Bracket_Leaflet-Preview-2.png',
    'article-1__heading': 'This is the Article 1 Heading',
    'article-1__description': 'This is the Article 1 Description',
    'article-2__link': 'https://caseytrees.org/',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/03/Cherry-March-Madness-Bracket_Leaflet-Preview-2.png',
    'article-2__heading': 'This is the Article 2 Heading',
    'article-2__description': 'This is the Article 2 Description',
    'article-3__link': 'https://caseytrees.org/',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/03/Cherry-March-Madness-Bracket_Leaflet-Preview-2.png',
    'article-3__heading': 'This is the Article 3 Heading',
    'article-3__description': 'This is the Article 3 Description'
}

NVP = NVP_20200324
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

