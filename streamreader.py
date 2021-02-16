import sys


NVP_20210208 = {
    'preheader': 'This promo won’t last, go grab your goodies now',
    'article-1__link': 'https://caseytrees.org/2021/02/lets-welcome-the-new-casey-trees-store-with-a-promo/?utm_source=leaflet&utm_medium=email&utm_campaign=onlinestore',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/02/Leafelt-Email-Miss-You-So-Merch.gif',
    'article-1__heading': 'Let’s Welcome the New Casey Trees Store with a Promo',
    'article-1__description': 'We love you so merch, we’re giving away free goodies with every purchase!',
    'banner-a__text-1': 'Ready2Play',
    'banner-a__text-2': "Ready2Play",
    'banner-a__link': 'https://caseytrees.org/2021/02/ready2play-ward-by-ward-meetings/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/02/leaflet_ready2play_button.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/02/leaflet_ready2play_button.png',
    'banner-a__alt-text': "Ready2Play",
    'article-2__link': 'https://caseytrees.org/2021/02/black-history-month-marvin-gaye-park/?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-2__alt-text': 'Marvin Gaye Park',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/02/Marvin-gaye-park-email.png',
    'article-2__heading': 'Black History Month: Marvin Gaye Park',
    'article-2__description': 'Who are our planting locations named after? We’re finding out.',
    'article-3__link': 'https://caseytrees.org/2021/02/the-story-on-understory-trees-2/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/02/understory-email.png',
    'article-3__heading': 'The Story on Understory Trees',
    'article-3__description': 'These trees play a vital role in creating a balanced ecosystem by providing food and shelter for much of our wildlife, including birds and small mammals.',
    'banner-b__link': 'https://caseytrees.org/remote',
    'banner-b__text-1': 'Casey Trees Remote', 
    'banner-b__text-2': 'Casey Trees Remote', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_ct-remote.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_ct-remote-mobile.png',
    'banner-b__alt-text': 'Casey Trees Remote',
}

NVP = NVP_20210208
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
