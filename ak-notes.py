import sys

filename = sys.argv[1]

NVP_03242020 = {
    'preheader': 'trees are going'
    'article-1__link': 'https://caseytrees.org/'
}

def replacekeys(nvp, line):
    print(line)

with open(filename) as hfile:
    for line in hfile:
        print(line, end='')