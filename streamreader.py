import sys


NVP_20200518 = {
    'preheader': 'Plus, how trees can help us remember those we’ve lost and a mini wellness retreat to close out #MentalHealthAwarenessMonth.',
    'article-1__link': 'https://caseytrees.org/2020/05/stayathome-mini-wellness-and-nature-retreat?utm_source=leaflet&utm_medium=email&utm_campaign=random',
    'article-1__alt-text': 'Mindfulness, trees, and wellness',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/mindfulness-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/mindfulness-email.png',
    'article-1__heading': '#StayatHome Mini-Wellness and Nature Retreat',
    'article-1__description': 'Close out Mental Health Awareness Month with some quick and restorative practices courtesy of our Youth Programs Coordinator and Certified Yoga Instructor Kelsey.',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Young trees need plenty of water this week.',
    'article-2__link': 'https://caseytrees.org/2020/05/remembering-those-weve-lost-on-memorial-day?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-2__alt-text': 'A day of remembrance',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/memorial-bowser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/memorial-responlsive.png',
    'article-2__heading': 'Remembering Those We’ve Lost on Memorial Day',
    'article-2__description': "A perennial part of the landscape, trees provide a lush, growing, live memorial to honor special folks.",
    'article-3__link': 'https://caseytreesdc.github.io/ct-videos/ycytE04?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-3__alt-text': 'Your City Your Trees: Episode 4',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/ycyt-4-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/ycyt-4-responsive.png',
    'article-3__heading': 'Your City, Your Trees Episode 4: Leafing Out',
    'article-3__description': "From their shape, how they're arranged, and how they're attached, there's a lot to learn! Your City, Your Trees: Leafing Out will get you started.",
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
