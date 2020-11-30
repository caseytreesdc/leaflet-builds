import sys


NVP_20201124 = {
    'preheader': 'show some love for the pandemic’s surprising hero - urban trees!',
    'article-1__link': 'https://caseytrees.org/2020/11/mark-a-grateful-givingtuesday-tomorrow-with-a-quiz-on-the-differences-between-volunteer-and-crew-plantings/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/volunteers-browser.gif',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/11/volunteers-email.gif',
    'article-1__heading': 'Mark a Grateful #GivingTuesday Tomorrow with a Quiz on the Differences Between Volunteer and Crew Plantings',
    'article-1__description': 'COVID safety precautions meant a season without our flagship community tree plantings. Can you guess what happened instead?',
    'banner-a__text-1': 'MAKE A YEAR END GIFT',
    'banner-a__text-2': 'delete this',
    'banner-a__link': 'https://connect.clickandpledge.com/w/Form/75ace67d-9469-48de-a04f-3f86dfb86f7e?utm_source=leaflet&utm_medium=email&utm_campaign=eoy&utm_content=email3&trk=givingtuesday3',
    'banner-a__image-browser': '',
    'banner-a__image-responsive': '',
    'banner-a__alt-text': '',
    'article-2__link': 'https://caseytrees.org/2020/11/world-soil-day-healthy-soil-means-healthy-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=easement',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://i.imgur.com/gQO5SA3.gif',
    'article-2__image-mobile': 'https://i.pinimg.com/originals/0f/c5/67/0fc567c0a90a4ebb149383d4c8a09f04.gif',
    'article-2__heading': 'World Soil Day: Healthy Soil Means Healthy Trees',
    'article-2__description': 'How we’re preserving the land that is left as an increasingly large portion of DC’s land is covered by concrete and asphalt',
    'article-3__link': 'https://caseytrees.org/2020/11/which-is-which-sweetgum-edition/?utm_source=leaflet&utm_medium=email&utm_campaign=treerebate',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/folklore-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/11/folklore-email2.png',
    'article-3__heading': 'Fun Folklore Forecasting',
    'article-3__description': 'Can trees predict the future?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;',
    'banner-b__link': 'https://www.eventbrite.com/e/montgomery-parks-and-casey-trees-tickets-121720670803',
    'banner-b__text': '', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_summit.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_summit-mobile.png',
    'banner-b__alt-text': 'Register for the  Dec. 2nd Urban Tree Summit!',
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
