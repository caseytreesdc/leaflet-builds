import sys


NVP_20200817 = {
    'preheader': 'Plus, we’re cancelling our traditional fall event season',
    'article-1__link': 'https://caseytrees.org/2020/08/executive-statement-on-fall-events/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/statetreequiz-browser2020.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/06/statetreequiz-email.png',
    'article-1__heading': 'Executive Statement on Fall Events',
    'article-1__description': 'We have always, and will always, err on the side of caution to ensure your safety and this is no exception.',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Even with the bit of rain, trees need more water this week.',
    'article-2__link': 'https://caseytrees.org/2020/08/an-update-on-pepcos-green-wall/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/vinewall-update-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/vinewall-update-email.png',
    'article-2__heading': 'An Update on PEPCO’s Green Wall',
    'article-2__description': 'Ahh the beauty of consistent maintenance and care (not to mention a satisfying before and after!).',
    'article-3__link': 'https://caseytrees.org/2020/08/catch-us-for-teen-tuesday-exploring-land-use-and-climate-change/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/teentuesday-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/teentuesdayemail.png',
    'article-3__heading': 'Catch Us for Teen Tuesday: Exploring Land Use and Climate Change',
    'article-3__description': 'A tree-source just for teens!',
    'banner__link': 'https://casey-trees-dc.square.site/product/junior-urban-forester-package/85?cs=true',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Leaflet-ad_TREEWISE.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/Leaflet-ad_TREEWISE.png',
    'banner__alt-text': 'at-home learning for kids',
}

NVP = NVP_20200817
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
