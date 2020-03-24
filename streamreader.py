import sys

NVP_20200324 = {
    'preheader': 'trees are growing',
    'article-1__link': 'https://caseytrees.org/'
}

NVP = NVP_20200324

#

def replacekeys(line):
    for name, value in NVP.items():
        line = line.replace(f'%%{name}%%', value)

    return line


# read redirected standard input line by line

for line in sys.stdin:
    print(replacekeys(line), end='')
