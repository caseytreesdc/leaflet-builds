import sys


NVP_20210913 = {
    'preheader': 'we’re celebrating our public lands for National Public Lands Day',
    'article-1__link': 'https://caseytrees.org/2021/09/celebrate-national-public-lands-day-with-casey-trees-and-the-national-environmental-education-foundation/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': 'sunlight through the trees',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/05/mental-health-email.png',
    'article-1__heading': 'Celebrate National Public Lands Day with Casey Trees and the National Environmental Education Foundation',
    'article-1__description': 'Join us at our special event',
    'banner-a__link': 'https://caseytrees.org/take-action/water/',
    'banner-a__alt-text': 'Weekly Watering Alert: Water',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water.jpg',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/2021-Watering-Alerts_must-water-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/09/we-cant-plant-in-the-summer-so-heres-how-volunteers-helped/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-2__alt-text': 'volunteers having fun at a tree care event',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/09/summer-treecare-wrap-email.png',
    'article-2__heading': 'We Can’t Plant in the Summer, So Here’s How Volunteers Helped',
    'article-2__description': 'Leaning into the protect part of our mission to restore, enhance, and protect',
    'article-3__link': 'https://caseytrees.org/2021/09/how-dc-gives-urban-trees-a-second-life/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-3__alt-text': 'large pieces of wood neatly organized in semicircle',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/11/urban-wood-reuse-email.png',
    'article-3__heading': 'How DC Gives Urban Trees a Second Life',
    'article-3__description': 'We had such a great time at the Urban Tree Summit’s Urban Wood Reuse field session we wanted to revisit how the District is creatively reusing felled wood',
    'banner-b__link': 'https://casey-trees.myshopify.com/',
    'banner-b__alt-text': "Browse our Store!",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_browse-our-new-store.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_browse-our-new-store-mobile.png',
}

NVP = NVP_20210913
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
