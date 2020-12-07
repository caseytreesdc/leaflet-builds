import sys


NVP_20201207 = {
    'preheader': 'and tips on regenerative pruning',
    'article-1__link': 'https://caseytrees.org/2020/12/we-made-it-through-2020-a-gift-guide/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2020/12/Gift-Guide-Leaflet-Preview.gif',
    'article-1__heading': 'We Made It Through 2020: A Gift Guide',
    'article-1__description': 'What a year folks! Let’s treat each other - the simple things are often best',
    'banner-a__text-1': 'MAKE A YEAR-END GIFT',
    'banner-a__text-2': '',
    'banner-a__link': 'https://connect.clickandpledge.com/w/Form/2ab97890-387e-4b10-a454-6ab08350e1b8?utm_source=leaflet&utm_medium=email&utm_campaign=eoy&utm_content=email8&trk=eoy5',
    'banner-a__image-browser': '',
    'banner-a__image-responsive': '',
    'banner-a__alt-text': '',
    'article-2__link': 'https://caseytrees.org/2020/12/from-the-archives-pruning-tips/?utm_source=leaflet&utm_medium=email&utm_campaign=feeforservice',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/12/tree-pruning-email.png',
    'article-2__heading': 'From the Archives: Pruning Tips',
    'article-2__description': 'Tips on how to prune trees yourself, or who you call if you don’t',
    'article-3__link': 'https://caseytrees.org/2020/12/preserving-the-rich-agricultural-and-cultural-legacy-of-the-casey-tree-farm-2/?utm_source=leaflet&utm_medium=email&utm_campaign=caseytreefarm',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/08/farm-rebate-email.png',
    'article-3__heading': 'Preserving the Rich Agricultural and Cultural Legacy of the Casey Tree Farm',
    'article-3__description': 'How our Farm, located on the banks of the Shenandoah River, cultivates 100 acres of land sustainably. And how you can help!',
    'banner-b__link': 'https://www.washingtonpost.com/local/dc-ward-8-parks-cleanup/2020/12/05/1d34f078-260f-11eb-8672-c281c7a2c96e_story.html',
    'banner-b__text-1': 'Casey Trees in the Post', 
    'banner-b__text-2': 'A Fight for Forestry Equity', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Mask_Ad_1.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/MaskAd2-responsive.png',
    'banner-b__alt-text': 'Protect Others. Protect Yourself. Protect Our Urban Forest. Link to masks on our online store.',
}

NVP = NVP_20201207
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
