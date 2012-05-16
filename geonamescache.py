class GeonamesCache:
    continents = {
        'AF': {'name': 'Africa', 'geonameid': 6255146},
        'AS': {'name': 'Asia', 'geonameid': 6255147},
        'EU': {'name': 'Europe', 'geonameid': 6255148},
        'NA': {'name': 'North America', 'geonameid': 6255149},
        'OC': {'name': 'Oceania', 'geonameid': 6255151},
        'SA': {'name': 'South America', 'geonameid': 6255150},
        'AN': {'name': 'Antarctica', 'geonameid': 6255152}
    }

    countries = {
        'AD': {'name': 'Andorra', 'continent_code': 'EU', 'geonameid': 3041565},
        'AE': {'name': 'United Arab Emirates', 'continent_code': 'AS', 'geonameid': 290557},
        'AF': {'name': 'Afghanistan', 'continent_code': 'AS', 'geonameid': 1149361},
        'AG': {'name': 'Antigua and Barbuda', 'continent_code': 'NA', 'geonameid': 3576396},
        'AI': {'name': 'Anguilla', 'continent_code': 'NA', 'geonameid': 3573511},
        'AL': {'name': 'Albania', 'continent_code': 'EU', 'geonameid': 783754},
        'AM': {'name': 'Armenia', 'continent_code': 'AS', 'geonameid': 174982},
        'AO': {'name': 'Angola', 'continent_code': 'AF', 'geonameid': 3351879},
        'AQ': {'name': 'Antarctica', 'continent_code': 'AN', 'geonameid': 6697173},
        'AR': {'name': 'Argentina', 'continent_code': 'SA', 'geonameid': 3865483},
        'AS': {'name': 'American Samoa', 'continent_code': 'OC', 'geonameid': 5880801},
        'AT': {'name': 'Austria', 'continent_code': 'EU', 'geonameid': 2782113},
        'AU': {'name': 'Australia', 'continent_code': 'OC', 'geonameid': 2077456},
        'AW': {'name': 'Aruba', 'continent_code': 'NA', 'geonameid': 3577279},
        'AX': {'name': 'Aland Islands', 'continent_code': 'EU', 'geonameid': 661882},
        'AZ': {'name': 'Azerbaijan', 'continent_code': 'AS', 'geonameid': 587116},
        'BA': {'name': 'Bosnia and Herzegovina', 'continent_code': 'EU', 'geonameid': 3277605},
        'BB': {'name': 'Barbados', 'continent_code': 'NA', 'geonameid': 3374084},
        'BD': {'name': 'Bangladesh', 'continent_code': 'AS', 'geonameid': 1210997},
        'BE': {'name': 'Belgium', 'continent_code': 'EU', 'geonameid': 2802361},
        'BF': {'name': 'Burkina Faso', 'continent_code': 'AF', 'geonameid': 2361809},
        'BG': {'name': 'Bulgaria', 'continent_code': 'EU', 'geonameid': 732800},
        'BH': {'name': 'Bahrain', 'continent_code': 'AS', 'geonameid': 290291},
        'BI': {'name': 'Burundi', 'continent_code': 'AF', 'geonameid': 433561},
        'BJ': {'name': 'Benin', 'continent_code': 'AF', 'geonameid': 2395170},
        'BL': {'name': 'Saint Barthelemy', 'continent_code': 'NA', 'geonameid': 3578476},
        'BM': {'name': 'Bermuda', 'continent_code': 'NA', 'geonameid': 3573345},
        'BN': {'name': 'Brunei', 'continent_code': 'AS', 'geonameid': 1820814},
        'BO': {'name': 'Bolivia', 'continent_code': 'SA', 'geonameid': 3923057},
        'BQ': {'name': 'Bonaire, Saint Eustatius and Saba ', 'continent_code': 'NA', 'geonameid': 7626844},
        'BR': {'name': 'Brazil', 'continent_code': 'SA', 'geonameid': 3469034},
        'BS': {'name': 'Bahamas', 'continent_code': 'NA', 'geonameid': 3572887},
        'BT': {'name': 'Bhutan', 'continent_code': 'AS', 'geonameid': 1252634},
        'BV': {'name': 'Bouvet Island', 'continent_code': 'AN', 'geonameid': 3371123},
        'BW': {'name': 'Botswana', 'continent_code': 'AF', 'geonameid': 933860},
        'BY': {'name': 'Belarus', 'continent_code': 'EU', 'geonameid': 630336},
        'BZ': {'name': 'Belize', 'continent_code': 'NA', 'geonameid': 3582678},
        'CA': {'name': 'Canada', 'continent_code': 'NA', 'geonameid': 6251999},
        'CC': {'name': 'Cocos Islands', 'continent_code': 'AS', 'geonameid': 1547376},
        'CD': {'name': 'Democratic Republic of the Congo', 'continent_code': 'AF', 'geonameid': 203312},
        'CF': {'name': 'Central African Republic', 'continent_code': 'AF', 'geonameid': 239880},
        'CG': {'name': 'Republic of the Congo', 'continent_code': 'AF', 'geonameid': 2260494},
        'CH': {'name': 'Switzerland', 'continent_code': 'EU', 'geonameid': 2658434},
        'CI': {'name': 'Ivory Coast', 'continent_code': 'AF', 'geonameid': 2287781},
        'CK': {'name': 'Cook Islands', 'continent_code': 'OC', 'geonameid': 1899402},
        'CL': {'name': 'Chile', 'continent_code': 'SA', 'geonameid': 3895114},
        'CM': {'name': 'Cameroon', 'continent_code': 'AF', 'geonameid': 2233387},
        'CN': {'name': 'China', 'continent_code': 'AS', 'geonameid': 1814991},
        'CO': {'name': 'Colombia', 'continent_code': 'SA', 'geonameid': 3686110},
        'CR': {'name': 'Costa Rica', 'continent_code': 'NA', 'geonameid': 3624060},
        'CU': {'name': 'Cuba', 'continent_code': 'NA', 'geonameid': 3562981},
        'CV': {'name': 'Cape Verde', 'continent_code': 'AF', 'geonameid': 3374766},
        'CW': {'name': 'Curacao', 'continent_code': 'NA', 'geonameid': 7626836},
        'CX': {'name': 'Christmas Island', 'continent_code': 'AS', 'geonameid': 2078138},
        'CY': {'name': 'Cyprus', 'continent_code': 'EU', 'geonameid': 146669},
        'CZ': {'name': 'Czech Republic', 'continent_code': 'EU', 'geonameid': 3077311},
        'DE': {'name': 'Germany', 'continent_code': 'EU', 'geonameid': 2921044},
        'DJ': {'name': 'Djibouti', 'continent_code': 'AF', 'geonameid': 223816},
        'DK': {'name': 'Denmark', 'continent_code': 'EU', 'geonameid': 2623032},
        'DM': {'name': 'Dominica', 'continent_code': 'NA', 'geonameid': 3575830},
        'DO': {'name': 'Dominican Republic', 'continent_code': 'NA', 'geonameid': 3508796},
        'DZ': {'name': 'Algeria', 'continent_code': 'AF', 'geonameid': 2589581},
        'EC': {'name': 'Ecuador', 'continent_code': 'SA', 'geonameid': 3658394},
        'EE': {'name': 'Estonia', 'continent_code': 'EU', 'geonameid': 453733},
        'EG': {'name': 'Egypt', 'continent_code': 'AF', 'geonameid': 357994},
        'EH': {'name': 'Western Sahara', 'continent_code': 'AF', 'geonameid': 2461445},
        'ER': {'name': 'Eritrea', 'continent_code': 'AF', 'geonameid': 338010},
        'ES': {'name': 'Spain', 'continent_code': 'EU', 'geonameid': 2510769},
        'ET': {'name': 'Ethiopia', 'continent_code': 'AF', 'geonameid': 337996},
        'FI': {'name': 'Finland', 'continent_code': 'EU', 'geonameid': 660013},
        'FJ': {'name': 'Fiji', 'continent_code': 'OC', 'geonameid': 2205218},
        'FK': {'name': 'Falkland Islands', 'continent_code': 'SA', 'geonameid': 3474414},
        'FM': {'name': 'Micronesia', 'continent_code': 'OC', 'geonameid': 2081918},
        'FO': {'name': 'Faroe Islands', 'continent_code': 'EU', 'geonameid': 2622320},
        'FR': {'name': 'France', 'continent_code': 'EU', 'geonameid': 3017382},
        'GA': {'name': 'Gabon', 'continent_code': 'AF', 'geonameid': 2400553},
        'GB': {'name': 'United Kingdom', 'continent_code': 'EU', 'geonameid': 2635167},
        'GD': {'name': 'Grenada', 'continent_code': 'NA', 'geonameid': 3580239},
        'GE': {'name': 'Georgia', 'continent_code': 'AS', 'geonameid': 614540},
        'GF': {'name': 'French Guiana', 'continent_code': 'SA', 'geonameid': 3381670},
        'GG': {'name': 'Guernsey', 'continent_code': 'EU', 'geonameid': 3042362},
        'GH': {'name': 'Ghana', 'continent_code': 'AF', 'geonameid': 2300660},
        'GI': {'name': 'Gibraltar', 'continent_code': 'EU', 'geonameid': 2411586},
        'GL': {'name': 'Greenland', 'continent_code': 'NA', 'geonameid': 3425505},
        'GM': {'name': 'Gambia', 'continent_code': 'AF', 'geonameid': 2413451},
        'GN': {'name': 'Guinea', 'continent_code': 'AF', 'geonameid': 2420477},
        'GP': {'name': 'Guadeloupe', 'continent_code': 'NA', 'geonameid': 3579143},
        'GQ': {'name': 'Equatorial Guinea', 'continent_code': 'AF', 'geonameid': 2309096},
        'GR': {'name': 'Greece', 'continent_code': 'EU', 'geonameid': 390903},
        'GS': {'name': 'South Georgia and the South Sandwich Islands', 'continent_code': 'AN', 'geonameid': 3474415},
        'GT': {'name': 'Guatemala', 'continent_code': 'NA', 'geonameid': 3595528},
        'GU': {'name': 'Guam', 'continent_code': 'OC', 'geonameid': 4043988},
        'GW': {'name': 'Guinea-Bissau', 'continent_code': 'AF', 'geonameid': 2372248},
        'GY': {'name': 'Guyana', 'continent_code': 'SA', 'geonameid': 3378535},
        'HK': {'name': 'Hong Kong', 'continent_code': 'AS', 'geonameid': 1819730},
        'HM': {'name': 'Heard Island and McDonald Islands', 'continent_code': 'AN', 'geonameid': 1547314},
        'HN': {'name': 'Honduras', 'continent_code': 'NA', 'geonameid': 3608932},
        'HR': {'name': 'Croatia', 'continent_code': 'EU', 'geonameid': 3202326},
        'HT': {'name': 'Haiti', 'continent_code': 'NA', 'geonameid': 3723988},
        'HU': {'name': 'Hungary', 'continent_code': 'EU', 'geonameid': 719819},
        'ID': {'name': 'Indonesia', 'continent_code': 'AS', 'geonameid': 1643084},
        'IE': {'name': 'Ireland', 'continent_code': 'EU', 'geonameid': 2963597},
        'IL': {'name': 'Israel', 'continent_code': 'AS', 'geonameid': 294640},
        'IM': {'name': 'Isle of Man', 'continent_code': 'EU', 'geonameid': 3042225},
        'IN': {'name': 'India', 'continent_code': 'AS', 'geonameid': 1269750},
        'IO': {'name': 'British Indian Ocean Territory', 'continent_code': 'AS', 'geonameid': 1282588},
        'IQ': {'name': 'Iraq', 'continent_code': 'AS', 'geonameid': 99237},
        'IR': {'name': 'Iran', 'continent_code': 'AS', 'geonameid': 130758},
        'IS': {'name': 'Iceland', 'continent_code': 'EU', 'geonameid': 2629691},
        'IT': {'name': 'Italy', 'continent_code': 'EU', 'geonameid': 3175395},
        'JE': {'name': 'Jersey', 'continent_code': 'EU', 'geonameid': 3042142},
        'JM': {'name': 'Jamaica', 'continent_code': 'NA', 'geonameid': 3489940},
        'JO': {'name': 'Jordan', 'continent_code': 'AS', 'geonameid': 248816},
        'JP': {'name': 'Japan', 'continent_code': 'AS', 'geonameid': 1861060},
        'KE': {'name': 'Kenya', 'continent_code': 'AF', 'geonameid': 192950},
        'KG': {'name': 'Kyrgyzstan', 'continent_code': 'AS', 'geonameid': 1527747},
        'KH': {'name': 'Cambodia', 'continent_code': 'AS', 'geonameid': 1831722},
        'KI': {'name': 'Kiribati', 'continent_code': 'OC', 'geonameid': 4030945},
        'KM': {'name': 'Comoros', 'continent_code': 'AF', 'geonameid': 921929},
        'KN': {'name': 'Saint Kitts and Nevis', 'continent_code': 'NA', 'geonameid': 3575174},
        'KP': {'name': 'North Korea', 'continent_code': 'AS', 'geonameid': 1873107},
        'KR': {'name': 'South Korea', 'continent_code': 'AS', 'geonameid': 1835841},
        'XK': {'name': 'Kosovo', 'continent_code': 'EU', 'geonameid': 831053},
        'KW': {'name': 'Kuwait', 'continent_code': 'AS', 'geonameid': 285570},
        'KY': {'name': 'Cayman Islands', 'continent_code': 'NA', 'geonameid': 3580718},
        'KZ': {'name': 'Kazakhstan', 'continent_code': 'AS', 'geonameid': 1522867},
        'LA': {'name': 'Laos', 'continent_code': 'AS', 'geonameid': 1655842},
        'LB': {'name': 'Lebanon', 'continent_code': 'AS', 'geonameid': 272103},
        'LC': {'name': 'Saint Lucia', 'continent_code': 'NA', 'geonameid': 3576468},
        'LI': {'name': 'Liechtenstein', 'continent_code': 'EU', 'geonameid': 3042058},
        'LK': {'name': 'Sri Lanka', 'continent_code': 'AS', 'geonameid': 1227603},
        'LR': {'name': 'Liberia', 'continent_code': 'AF', 'geonameid': 2275384},
        'LS': {'name': 'Lesotho', 'continent_code': 'AF', 'geonameid': 932692},
        'LT': {'name': 'Lithuania', 'continent_code': 'EU', 'geonameid': 597427},
        'LU': {'name': 'Luxembourg', 'continent_code': 'EU', 'geonameid': 2960313},
        'LV': {'name': 'Latvia', 'continent_code': 'EU', 'geonameid': 458258},
        'LY': {'name': 'Libya', 'continent_code': 'AF', 'geonameid': 2215636},
        'MA': {'name': 'Morocco', 'continent_code': 'AF', 'geonameid': 2542007},
        'MC': {'name': 'Monaco', 'continent_code': 'EU', 'geonameid': 2993457},
        'MD': {'name': 'Moldova', 'continent_code': 'EU', 'geonameid': 617790},
        'ME': {'name': 'Montenegro', 'continent_code': 'EU', 'geonameid': 3194884},
        'MF': {'name': 'Saint Martin', 'continent_code': 'NA', 'geonameid': 3578421},
        'MG': {'name': 'Madagascar', 'continent_code': 'AF', 'geonameid': 1062947},
        'MH': {'name': 'Marshall Islands', 'continent_code': 'OC', 'geonameid': 2080185},
        'MK': {'name': 'Macedonia', 'continent_code': 'EU', 'geonameid': 718075},
        'ML': {'name': 'Mali', 'continent_code': 'AF', 'geonameid': 2453866},
        'MM': {'name': 'Myanmar', 'continent_code': 'AS', 'geonameid': 1327865},
        'MN': {'name': 'Mongolia', 'continent_code': 'AS', 'geonameid': 2029969},
        'MO': {'name': 'Macao', 'continent_code': 'AS', 'geonameid': 1821275},
        'MP': {'name': 'Northern Mariana Islands', 'continent_code': 'OC', 'geonameid': 4041468},
        'MQ': {'name': 'Martinique', 'continent_code': 'NA', 'geonameid': 3570311},
        'MR': {'name': 'Mauritania', 'continent_code': 'AF', 'geonameid': 2378080},
        'MS': {'name': 'Montserrat', 'continent_code': 'NA', 'geonameid': 3578097},
        'MT': {'name': 'Malta', 'continent_code': 'EU', 'geonameid': 2562770},
        'MU': {'name': 'Mauritius', 'continent_code': 'AF', 'geonameid': 934292},
        'MV': {'name': 'Maldives', 'continent_code': 'AS', 'geonameid': 1282028},
        'MW': {'name': 'Malawi', 'continent_code': 'AF', 'geonameid': 927384},
        'MX': {'name': 'Mexico', 'continent_code': 'NA', 'geonameid': 3996063},
        'MY': {'name': 'Malaysia', 'continent_code': 'AS', 'geonameid': 1733045},
        'MZ': {'name': 'Mozambique', 'continent_code': 'AF', 'geonameid': 1036973},
        'NA': {'name': 'Namibia', 'continent_code': 'AF', 'geonameid': 3355338},
        'NC': {'name': 'New Caledonia', 'continent_code': 'OC', 'geonameid': 2139685},
        'NE': {'name': 'Niger', 'continent_code': 'AF', 'geonameid': 2440476},
        'NF': {'name': 'Norfolk Island', 'continent_code': 'OC', 'geonameid': 2155115},
        'NG': {'name': 'Nigeria', 'continent_code': 'AF', 'geonameid': 2328926},
        'NI': {'name': 'Nicaragua', 'continent_code': 'NA', 'geonameid': 3617476},
        'NL': {'name': 'Netherlands', 'continent_code': 'EU', 'geonameid': 2750405},
        'NO': {'name': 'Norway', 'continent_code': 'EU', 'geonameid': 3144096},
        'NP': {'name': 'Nepal', 'continent_code': 'AS', 'geonameid': 1282988},
        'NR': {'name': 'Nauru', 'continent_code': 'OC', 'geonameid': 2110425},
        'NU': {'name': 'Niue', 'continent_code': 'OC', 'geonameid': 4036232},
        'NZ': {'name': 'New Zealand', 'continent_code': 'OC', 'geonameid': 2186224},
        'OM': {'name': 'Oman', 'continent_code': 'AS', 'geonameid': 286963},
        'PA': {'name': 'Panama', 'continent_code': 'NA', 'geonameid': 3703430},
        'PE': {'name': 'Peru', 'continent_code': 'SA', 'geonameid': 3932488},
        'PF': {'name': 'French Polynesia', 'continent_code': 'OC', 'geonameid': 4030656},
        'PG': {'name': 'Papua New Guinea', 'continent_code': 'OC', 'geonameid': 2088628},
        'PH': {'name': 'Philippines', 'continent_code': 'AS', 'geonameid': 1694008},
        'PK': {'name': 'Pakistan', 'continent_code': 'AS', 'geonameid': 1168579},
        'PL': {'name': 'Poland', 'continent_code': 'EU', 'geonameid': 798544},
        'PM': {'name': 'Saint Pierre and Miquelon', 'continent_code': 'NA', 'geonameid': 3424932},
        'PN': {'name': 'Pitcairn', 'continent_code': 'OC', 'geonameid': 4030699},
        'PR': {'name': 'Puerto Rico', 'continent_code': 'NA', 'geonameid': 4566966},
        'PS': {'name': 'Palestinian Territory', 'continent_code': 'AS', 'geonameid': 6254930},
        'PT': {'name': 'Portugal', 'continent_code': 'EU', 'geonameid': 2264397},
        'PW': {'name': 'Palau', 'continent_code': 'OC', 'geonameid': 1559582},
        'PY': {'name': 'Paraguay', 'continent_code': 'SA', 'geonameid': 3437598},
        'QA': {'name': 'Qatar', 'continent_code': 'AS', 'geonameid': 289688},
        'RE': {'name': 'Reunion', 'continent_code': 'AF', 'geonameid': 935317},
        'RO': {'name': 'Romania', 'continent_code': 'EU', 'geonameid': 798549},
        'RS': {'name': 'Serbia', 'continent_code': 'EU', 'geonameid': 6290252},
        'RU': {'name': 'Russia', 'continent_code': 'EU', 'geonameid': 2017370},
        'RW': {'name': 'Rwanda', 'continent_code': 'AF', 'geonameid': 49518},
        'SA': {'name': 'Saudi Arabia', 'continent_code': 'AS', 'geonameid': 102358},
        'SB': {'name': 'Solomon Islands', 'continent_code': 'OC', 'geonameid': 2103350},
        'SC': {'name': 'Seychelles', 'continent_code': 'AF', 'geonameid': 241170},
        'SD': {'name': 'Sudan', 'continent_code': 'AF', 'geonameid': 366755},
        'SS': {'name': 'South Sudan', 'continent_code': 'AF', 'geonameid': 7909807},
        'SE': {'name': 'Sweden', 'continent_code': 'EU', 'geonameid': 2661886},
        'SG': {'name': 'Singapore', 'continent_code': 'AS', 'geonameid': 1880251},
        'SH': {'name': 'Saint Helena', 'continent_code': 'AF', 'geonameid': 3370751},
        'SI': {'name': 'Slovenia', 'continent_code': 'EU', 'geonameid': 3190538},
        'SJ': {'name': 'Svalbard and Jan Mayen', 'continent_code': 'EU', 'geonameid': 607072},
        'SK': {'name': 'Slovakia', 'continent_code': 'EU', 'geonameid': 3057568},
        'SL': {'name': 'Sierra Leone', 'continent_code': 'AF', 'geonameid': 2403846},
        'SM': {'name': 'San Marino', 'continent_code': 'EU', 'geonameid': 3168068},
        'SN': {'name': 'Senegal', 'continent_code': 'AF', 'geonameid': 2245662},
        'SO': {'name': 'Somalia', 'continent_code': 'AF', 'geonameid': 51537},
        'SR': {'name': 'Suriname', 'continent_code': 'SA', 'geonameid': 3382998},
        'ST': {'name': 'Sao Tome and Principe', 'continent_code': 'AF', 'geonameid': 2410758},
        'SV': {'name': 'El Salvador', 'continent_code': 'NA', 'geonameid': 3585968},
        'SX': {'name': 'Sint Maarten', 'continent_code': 'NA', 'geonameid': 7609695},
        'SY': {'name': 'Syria', 'continent_code': 'AS', 'geonameid': 163843},
        'SZ': {'name': 'Swaziland', 'continent_code': 'AF', 'geonameid': 934841},
        'TC': {'name': 'Turks and Caicos Islands', 'continent_code': 'NA', 'geonameid': 3576916},
        'TD': {'name': 'Chad', 'continent_code': 'AF', 'geonameid': 2434508},
        'TF': {'name': 'French Southern Territories', 'continent_code': 'AN', 'geonameid': 1546748},
        'TG': {'name': 'Togo', 'continent_code': 'AF', 'geonameid': 2363686},
        'TH': {'name': 'Thailand', 'continent_code': 'AS', 'geonameid': 1605651},
        'TJ': {'name': 'Tajikistan', 'continent_code': 'AS', 'geonameid': 1220409},
        'TK': {'name': 'Tokelau', 'continent_code': 'OC', 'geonameid': 4031074},
        'TL': {'name': 'East Timor', 'continent_code': 'OC', 'geonameid': 1966436},
        'TM': {'name': 'Turkmenistan', 'continent_code': 'AS', 'geonameid': 1218197},
        'TN': {'name': 'Tunisia', 'continent_code': 'AF', 'geonameid': 2464461},
        'TO': {'name': 'Tonga', 'continent_code': 'OC', 'geonameid': 4032283},
        'TR': {'name': 'Turkey', 'continent_code': 'AS', 'geonameid': 298795},
        'TT': {'name': 'Trinidad and Tobago', 'continent_code': 'NA', 'geonameid': 3573591},
        'TV': {'name': 'Tuvalu', 'continent_code': 'OC', 'geonameid': 2110297},
        'TW': {'name': 'Taiwan', 'continent_code': 'AS', 'geonameid': 1668284},
        'TZ': {'name': 'Tanzania', 'continent_code': 'AF', 'geonameid': 149590},
        'UA': {'name': 'Ukraine', 'continent_code': 'EU', 'geonameid': 690791},
        'UG': {'name': 'Uganda', 'continent_code': 'AF', 'geonameid': 226074},
        'UM': {'name': 'United States Minor Outlying Islands', 'continent_code': 'OC', 'geonameid': 5854968},
        'US': {'name': 'United States', 'continent_code': 'NA', 'geonameid': 6252001},
        'UY': {'name': 'Uruguay', 'continent_code': 'SA', 'geonameid': 3439705},
        'UZ': {'name': 'Uzbekistan', 'continent_code': 'AS', 'geonameid': 1512440},
        'VA': {'name': 'Vatican', 'continent_code': 'EU', 'geonameid': 3164670},
        'VC': {'name': 'Saint Vincent and the Grenadines', 'continent_code': 'NA', 'geonameid': 3577815},
        'VE': {'name': 'Venezuela', 'continent_code': 'SA', 'geonameid': 3625428},
        'VG': {'name': 'British Virgin Islands', 'continent_code': 'NA', 'geonameid': 3577718},
        'VI': {'name': 'U.S. Virgin Islands', 'continent_code': 'NA', 'geonameid': 4796775},
        'VN': {'name': 'Vietnam', 'continent_code': 'AS', 'geonameid': 1562822},
        'VU': {'name': 'Vanuatu', 'continent_code': 'OC', 'geonameid': 2134431},
        'WF': {'name': 'Wallis and Futuna', 'continent_code': 'OC', 'geonameid': 4034749},
        'WS': {'name': 'Samoa', 'continent_code': 'OC', 'geonameid': 4034894},
        'YE': {'name': 'Yemen', 'continent_code': 'AS', 'geonameid': 69543},
        'YT': {'name': 'Mayotte', 'continent_code': 'AF', 'geonameid': 1024031},
        'ZA': {'name': 'South Africa', 'continent_code': 'AF', 'geonameid': 953987},
        'ZM': {'name': 'Zambia', 'continent_code': 'AF', 'geonameid': 895949},
        'ZW': {'name': 'Zimbabwe', 'continent_code': 'AF', 'geonameid': 878675},
        'CS': {'name': 'Serbia and Montenegro', 'continent_code': 'EU', 'geonameid': None},
        'AN': {'name': 'Netherlands Antilles', 'continent_code': 'NA', 'geonameid': None}
    }

    us_states = {
        'AK': {'name': 'Alaska', 'geonameid': 5879092},
        'AL': {'name': 'Alabama', 'geonameid': 4829764},
        'AR': {'name': 'Arkansas', 'geonameid': 4099753},
        'AZ': {'name': 'Arizona', 'geonameid': 5551752},
        'CA': {'name': 'California', 'geonameid': 5332921},
        'CO': {'name': 'Colorado', 'geonameid': 5417618},
        'CT': {'name': 'Connecticut', 'geonameid': 4831725},
        'DC': {'name': 'District of Columbia', 'geonameid': 4138106},
        'DE': {'name': 'Delaware', 'geonameid': 4142224},
        'FL': {'name': 'Florida', 'geonameid': 4155751},
        'GA': {'name': 'Georgia', 'geonameid': 4197000},
        'HI': {'name': 'Hawaii', 'geonameid': 5855797},
        'IA': {'name': 'Iowa', 'geonameid': 4862182},
        'ID': {'name': 'Idaho', 'geonameid': 5596512},
        'IL': {'name': 'Illinois', 'geonameid': 4896861},
        'IN': {'name': 'Indiana', 'geonameid': 4921868},
        'KS': {'name': 'Kansas', 'geonameid': 4273857},
        'KY': {'name': 'Kentucky', 'geonameid': 6254925},
        'LA': {'name': 'Louisiana', 'geonameid': 4331987},
        'MA': {'name': 'Massachusetts', 'geonameid': 6254926},
        'MD': {'name': 'Maryland', 'geonameid': 4361885},
        'ME': {'name': 'Maine', 'geonameid': 4971068},
        'MI': {'name': 'Michigan', 'geonameid': 5001836},
        'MN': {'name': 'Minnesota', 'geonameid': 5037779},
        'MO': {'name': 'Missouri', 'geonameid': 4398678},
        'MS': {'name': 'Mississippi', 'geonameid': 4436296},
        'MT': {'name': 'Montana', 'geonameid': 5667009},
        'NC': {'name': 'North Carolina', 'geonameid': 4482348},
        'ND': {'name': 'North Dakota', 'geonameid': 5690763},
        'NE': {'name': 'Nebraska', 'geonameid': 5073708},
        'NH': {'name': 'New Hampshire', 'geonameid': 5090174},
        'NJ': {'name': 'New Jersey', 'geonameid': 5101760},
        'NM': {'name': 'New Mexico', 'geonameid': 5481136},
        'NV': {'name': 'Nevada', 'geonameid': 5509151},
        'NY': {'name': 'New York', 'geonameid': 5128638},
        'OH': {'name': 'Ohio', 'geonameid': 5165418},
        'OK': {'name': 'Oklahoma', 'geonameid': 4544379},
        'OR': {'name': 'Oregon', 'geonameid': 5744337},
        'PA': {'name': 'Pennsylvania', 'geonameid': 6254927},
        'RI': {'name': 'Rhode Island', 'geonameid': 5224323},
        'SC': {'name': 'South Carolina', 'geonameid': 4597040},
        'SD': {'name': 'South Dakota', 'geonameid': 5769223},
        'TN': {'name': 'Tennessee', 'geonameid': 4662168},
        'TX': {'name': 'Texas', 'geonameid': 4736286},
        'UT': {'name': 'Utah', 'geonameid': 5549030},
        'VA': {'name': 'Virginia', 'geonameid': 6254928},
        'VT': {'name': 'Vermont', 'geonameid': 5242283},
        'WA': {'name': 'Washington', 'geonameid': 5815135},
        'WI': {'name': 'Wisconsin', 'geonameid': 5279468},
        'WV': {'name': 'West Virginia', 'geonameid': 4826850},
        'WY': {'name': 'Wyoming', 'geonameid': 5843591}
    }