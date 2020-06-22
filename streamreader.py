import sys


NVP_20200518 = {
    'preheader': 'Plus, Your Favorite Hidden Urban Oasis is Open!',
    'article-1__link': 'https://caseytrees.org/2020/06/lets-talk-about-urban-island-effect/?utm_source=leaflet&utm_medium=email&utm_campaign=research',
    'article-1__alt-text': 'The Urban Island Heat Effect',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/06/UHI-email-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/06/UHI-email.png',
    'article-1__heading': 'Let’s Talk About Urban Island Effect',
    'article-1__description': 'And its unsurprising twist.',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Young trees need plenty of water this week.',
    'article-2__link': 'https://caseytrees.org/2020/06/the-arboretums-open/?utm_source=leaflet&utm_medium=email&utm_campaign=city-partner',
    'article-2__alt-text': 'the arboretum is open!',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/06/UNA-email-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/06/UNA-email.png',
    'article-2__heading': "The Arboretum’s Open!",
    'article-2__description': "Wide open spaces, unusual trees, and plenty of sunshine and fresh air.",
    'article-3__link': 'https://caseytrees.org/2020/06/color-coding-demystifying-city-spray-paint-marks-2/?utm_source=leaflet&utm_medium=email&utm_campaign=ddot-ufa',
    'article-3__alt-text': 'Demystifying City Spray Paint Marks',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/06/spray-paint-email-browser.jpg',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/06/spray-paint-email-responsive.jpg',
    'article-3__heading': 'Color Coding: Demystifying City Spray Paint Marks',
    'article-3__description': "What does that orange dot on a tree mean?",
    'banner__link': 'https://www.tfaforms.com/4826832',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/leaflet-youth-programs-2020.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/leaflet-youth-programs-2020.png',
    'banner__alt-text': 'youth programs survey',
}

NVP = NVP_20200518
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
