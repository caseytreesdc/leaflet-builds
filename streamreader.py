import sys


NVP_20201124 = {
    'preheader': 'and how to treat common tree issues',
    'article-1__link': 'https://caseytrees.org/2020/12/we-made-it-through-2020-a-gift-guide/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://i.pinimg.com/originals/7c/50/ba/7c50ba64daf30ee45358376bc454fb89.gif',
    'article-1__image-mobile': 'https://i.pinimg.com/originals/b3/78/0a/b3780a110a6b672a2373a6e066f89f3d.gif',
    'article-1__heading': 'We Made It Through 2020: A Gift Guide',
    'article-1__description': 'What a year folks! Let’s treat each other - the simple things are often best',
    'banner-a__text-1': 'MAKE A YEAR-END GIFT',
    'banner-a__text-2': '',
    'banner-a__link': 'https://connect.clickandpledge.com/w/Form/75ace67d-9469-48de-a04f-3f86dfb86f7e?utm_source=Leaflet&utm_medium=email&utm_campaign=eoy&utm_content=email5&trk=eoy5',
    'banner-a__image-browser': '',
    'banner-a__image-responsive': '',
    'banner-a__alt-text': '',
    'article-2__link': 'https://caseytrees.org/2020/12/dont-panic-common-tree-issues-and-how-to-treat-them-2/?utm_source=leaflet&utm_medium=email&utm_campaign=feeforservice',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/12/tree-issue-rust-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/11/tree-issue-rust-email.png',
    'article-2__heading': 'Don’t Panic! Common Tree Issues and How to Treat Them',
    'article-2__description': 'We provide residential tree consultations through our Fee for Service program',
    'article-3__link': 'https://caseytrees.org/2020/12/preserving-the-rich-agricultural-and-cultural-legacy-of-the-casey-tree-farm-2/?utm_source=leaflet&utm_medium=email&utm_campaign=caseytreefarm',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/farm-rebate-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/farm-rebate-email.png',
    'article-3__heading': 'Preserving the Rich Agricultural and Cultural Legacy of the Casey Tree Farm',
    'article-3__description': 'How our Farm, located on the banks of the Shenandoah River, cultivates 100 acres of land sustainably. And how you can help!',
    'banner-b__link': 'https://casey-trees-dc.square.site/product/face-mask-dc-outline/88?cs=true?utm_source%3DLeaflet&trk=eoy5&utm_campaign=eoy&utm_content=email5&utm_medium=email',
    'banner-b__text': '', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Mask_Ad_1.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/MaskAd2-responsive.png',
    'banner-b__alt-text': 'Protect Others. Protect Yourself. Protect Our Urban Forest. Link to masks on our online store.',
}

NVP = NVP_20201124
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
