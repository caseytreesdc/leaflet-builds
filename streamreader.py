import sys


NVP_2021206 = {
    'preheader': "and a welcome to the newest DDOT Director",
    'article-1__link': 'https://caseytrees.org/2021/12/its-the-little-things/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': 'planting crew planting pines',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/12/little-things-leaflet-email.png',
    'article-1__heading': 'It’s the Little Things',
    'article-1__description': 'One small tree for a yard, one giant leap for urban kind',
    'banner-a__link': 'https://connect.clickandpledge.com/w/Form/446220bb-4a7a-4225-8b33-39cd133877c1?trk=EOYEmail5&utm_source=listemail&utm_medium=email-5&utm_campaign=eoy2021',
    'banner-a__alt-text': 'Support Casey Trees this giving season. Donate Now',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/12/Leaflet-button_give-desktop.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/12/Leaflet-button_give-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/12/congratulations-new-ddot-director-everett-lott/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-2__alt-text': "new DDOT director Everett Lott",
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/12/dott-dir-new-email.png',
    'article-2__heading': 'Congratulations New DDOT Director Everett Lott',
    'article-2__description': 'We are so excited to work with Director Lott and all DDOT partners to continue to grow, enhance, and protect DC’s tree canopy. ',
    'article-3__link': 'https://caseytrees.org/2021/12/calling-all-urban-forestry-students-2/?utm_source=leaflet&utm_medium=email&utm_campaign=gcascholarship',
    'article-3__alt-text': 'inspecting tree leaves',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/12/gca-final-2-email.png',
    'article-3__heading': "Calling All Urban Forestry Students",
    'article-3__description': 'Apply for our $7,500 fellowship or forward to a friend who would be interested!',
    'banner-b__link': 'https://caseytrees.org/education/urban-forestry-fellowship/',
    'banner-b__alt-text': 'Urban Forestry Student Scholarship',
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca_v2.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca-mobile-2.png',
}

NVP = NVP_2021206
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
