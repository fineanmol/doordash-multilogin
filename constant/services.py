class Service:
    def __init__(self, id, name, short_name, region):
        self.id = id
        self.name = name
        self.short_name = short_name
        self.region = region

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_short_name(self):
        return self.short_name

    def get_region(self):
        return self.region

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_short_name(self, short_name):
        self.short_name = short_name

    def set_region(self, region):
        self.region = region


def _create_default_services():
    service_data = [
        {"ID": 1, "name": 'United States', "short_name": 'US', "region": 'North America'},
        {"ID": 53, "name": 'Mexico', "short_name": 'MX', "region": 'North America'},
        {"ID": 128, "name": 'Guadeloupe', "short_name": 'GP', "region": 'North America'},
        {"ID": 148, "name": 'Anguilla', "short_name": 'AI', "region": 'North America'},
        {"ID": 2, "name": 'United Kingdom', "short_name": 'GB', "region": 'Europe'},
        {"ID": 3, "name": 'Netherlands', "short_name": 'NL', "region": 'Europe'},
        {"ID": 4, "name": 'Russia', "short_name": 'RU', "region": 'Europe'},
        {"ID": 5, "name": 'Latvia', "short_name": 'LV', "region": 'Europe'},
        {"ID": 6, "name": 'Sweden', "short_name": 'SE', "region": 'Europe'},
        {"ID": 8, "name": 'Portugal', "short_name": 'PT', "region": 'Europe'},
        {"ID": 10, "name": 'Estonia', "short_name": 'EE', "region": 'Europe'},
        {"ID": 13, "name": 'Romania', "short_name": 'RO', "region": 'Europe'},
        {"ID": 19, "name": 'Denmark', "short_name": 'DK', "region": 'Europe'},
        {"ID": 21, "name": 'Poland', "short_name": 'PL', "region": 'Europe'},
        {"ID": 23, "name": 'France', "short_name": 'FR', "region": 'Europe'},
        {"ID": 24, "name": 'Germany', "short_name": 'DE', "region": 'Europe'},
        {"ID": 25, "name": 'Ukraine', "short_name": 'UA', "region": 'Europe'},
        {"ID": 32, "name": 'Ireland', "short_name": 'IE', "region": 'Europe'},
        {"ID": 37, "name": 'Serbia', "short_name": 'RS', "region": 'Europe'},
        {"ID": 47, "name": 'Lithuania', "short_name": 'LT', "region": 'Europe'},
        {"ID": 48, "name": 'Croatia', "short_name": 'HR', "region": 'Europe'},
        {"ID": 50, "name": 'Austria', "short_name": 'AT', "region": 'Europe'},
        {"ID": 51, "name": 'Belarus', "short_name": 'BY', "region": 'Europe'},
        {"ID": 55, "name": 'Spain', "short_name": 'ES', "region": 'Europe'},
        {"ID": 57, "name": 'Slovenia', "short_name": 'SI', "region": 'Europe'},
        {"ID": 75, "name": 'Belgium', "short_name": 'BE', "region": 'Europe'},
        {"ID": 76, "name": 'Bulgaria', "short_name": 'BG', "region": 'Europe'},
        {"ID": 77, "name": 'Hungary', "short_name": 'HU', "region": 'Europe'},
        {"ID": 78, "name": 'Moldova', "short_name": 'MD', "region": 'Europe'},
        {"ID": 79, "name": 'Italy', "short_name": 'IT', "region": 'Europe'},
        {"ID": 102, "name": 'Greece', "short_name": 'GR', "region": 'Europe'},
        {"ID": 104, "name": 'Iceland', "short_name": 'IS', "region": 'Europe'},
        {"ID": 112, "name": 'Slovakia', "short_name": 'SK', "region": 'Europe'},
        {"ID": 115, "name": 'Monaco', "short_name": 'MC', "region": 'Europe'},
        {"ID": 123, "name": 'Albania', "short_name": 'AL', "region": 'Europe'},
        {"ID": 130, "name": 'Finland', "short_name": 'FI', "region": 'Europe'},
        {"ID": 131, "name": 'Luxembourg', "short_name": 'LU', "region": 'Europe'},
        {"ID": 133, "name": 'Montenegro', "short_name": 'ME', "region": 'Europe'},
        {"ID": 134, "name": 'Switzerland', "short_name": 'CH', "region": 'Europe'},
        {"ID": 135, "name": 'Norway', "short_name": 'NO', "region": 'Europe'},
        {"ID": 7, "name": 'Kazakhstan', "short_name": 'KZ', "region": 'Asia'},
        {"ID": 9, "name": 'Indonesia', "short_name": 'ID', "region": 'Asia'},
        {"ID": 11, "name": 'Vietnam', "short_name": 'VN', "region": 'Asia'},
        {"ID": 12, "name": 'Philippines', "short_name": 'PH', "region": 'Asia'},
        {"ID": 15, "name": 'India', "short_name": 'IN', "region": 'Asia'},
        {"ID": 18, "name": 'Kyrgyzstan', "short_name": 'KG', "region": 'Asia'},
        {"ID": 20, "name": 'Malaysia', "short_name": 'MY', "region": 'Asia'},
        {"ID": 26, "name": 'China', "short_name": 'CN', "region": 'Asia'},
        {"ID": 28, "name": 'Kyrgyzstan', "short_name": 'KG', "region": 'Asia'},
        {"ID": 29, "name": 'Israel', "short_name": 'IL', "region": 'Asia'},
        {"ID": 33, "name": 'Cambodia', "short_name": 'KH', "region": 'Asia'},
        {"ID": 34, "name": 'Laos', "short_name": 'LA', "region": 'Asia'},
        {"ID": 38, "name": 'Yemen', "short_name": 'YE', "region": 'Asia'},
        {"ID": 44, "name": 'Uzbekistan', "short_name": 'UZ', "region": 'Asia'},
        {"ID": 49, "name": 'Iraq', "short_name": 'IQ', "region": 'Asia'},
        {"ID": 52, "name": 'Thailand', "short_name": 'TH', "region": 'Asia'},
        {"ID": 54, "name": 'Taiwan', "short_name": 'TW', "region": 'Asia'},
        {"ID": 58, "name": 'Bangladesh', "short_name": 'BD', "region": 'Asia'},
        {"ID": 60, "name": 'Turkey', "short_name": 'TR', "region": 'Asia'},
        {"ID": 62, "name": 'Pakistan', "short_name": 'PK', "region": 'Asia'},
        {"ID": 67, "name": 'Mongolia', "short_name": 'MN', "region": 'Asia'},
        {"ID": 69, "name": 'Afghanistan', "short_name": 'AF', "region": 'Asia'},
        {"ID": 72, "name": 'Cyprus', "short_name": 'CY', "region": 'Asia'},
        {"ID": 74, "name": 'Nepal', "short_name": 'NP', "region": 'Asia'},
        {"ID": 88, "name": 'Kuwait', "short_name": 'KW', "region": 'Asia'},
        {"ID": 91, "name": 'Oman', "short_name": 'OM', "region": 'Asia'},
        {"ID": 92, "name": 'Qatar', "short_name": 'QA', "region": 'Asia'},
        {"ID": 95, "name": 'Jordan', "short_name": 'JO', "region": 'Asia'},
        {"ID": 98, "name": 'Brunei', "short_name": 'BN', "region": 'Asia'},
        {"ID": 101, "name": 'Georgia', "short_name": 'GE', "region": 'Asia'},
        {"ID": 114, "name": 'Tajikistan', "short_name": 'TJ', "region": 'Asia'},
        {"ID": 116, "name": 'Bahrain', "short_name": 'BH', "region": 'Asia'},
        {"ID": 118, "name": 'Armenia', "short_name": 'AM', "region": 'Asia'},
        {"ID": 121, "name": 'Lebanon', "short_name": 'LB', "region": 'Asia'},
        {"ID": 126, "name": 'Bhutan', "short_name": 'BT', "region": 'Asia'},
        {"ID": 127, "name": 'Maldives', "short_name": 'MV', "region": 'Asia'},
        {"ID": 129, "name": 'Turkmenistan', "short_name": 'TM', "region": 'Asia'},
        {"ID": 141, "name": 'Singapore', "short_name": 'SG', "region": 'Asia'},
        {"ID": 14, "name": 'Nigeria', "short_name": 'NG', "region": 'Africa'},
        {"ID": 16, "name": 'Kenya', "short_name": 'KE', "region": 'Africa'},
        {"ID": 27, "name": 'Tanzania', "short_name": 'TZ', "region": 'Africa'},
        {"ID": 30, "name": 'Madagascar', "short_name": 'MG', "region": 'Africa'},
        {"ID": 31, "name": 'Egypt', "short_name": 'EG', "region": 'Africa'},
        {"ID": 36, "name": 'Gambia', "short_name": 'GM', "region": 'Africa'},
        {"ID": 41, "name": 'Morocco', "short_name": 'MA', "region": 'Africa'},
        {"ID": 42, "name": 'Ghana', "short_name": 'GH', "region": 'Africa'},
        {"ID": 45, "name": 'Cameroon', "short_name": 'CM', "region": 'Africa'},
        {"ID": 46, "name": 'Chad', "short_name": 'TD', "region": 'Africa'},
        {"ID": 56, "name": 'Algeria', "short_name": 'DZ', "region": 'Africa'},
        {"ID": 59, "name": 'Senegal', "short_name": 'SN', "region": 'Africa'},
        {"ID": 63, "name": 'Guinea', "short_name": 'GN', "region": 'Africa'},
        {"ID": 64, "name": 'Mali', "short_name": 'ML', "region": 'Africa'},
        {"ID": 66, "name": 'Ethiopia', "short_name": 'ET', "region": 'Africa'},
        {"ID": 70, "name": 'Uganda', "short_name": 'UG', "region": 'Africa'},
        {"ID": 71, "name": 'Angola', "short_name": 'AO', "region": 'Africa'},
        {"ID": 73, "name": 'Mozambique', "short_name": 'MZ', "region": 'Africa'},
        {"ID": 82, "name": 'Tunisia', "short_name": 'TN', "region": 'Africa'},
        {"ID": 86, "name": 'Zimbabwe', "short_name": 'ZW', "region": 'Africa'},
        {"ID": 87, "name": 'Togo', "short_name": 'TG', "region": 'Africa'},
        {"ID": 90, "name": 'Swaziland', "short_name": 'SZ', "region": 'Africa'},
        {"ID": 94, "name": 'Mauritania', "short_name": 'MR', "region": 'Africa'},
        {"ID": 96, "name": 'Burundi', "short_name": 'BI', "region": 'Africa'},
        {"ID": 97, "name": 'Benin', "short_name": 'BJ', "region": 'Africa'},
        {"ID": 99, "name": 'Botswana', "short_name": 'BW', "region": 'Africa'},
        {"ID": 105, "name": 'Comoros', "short_name": 'KM', "region": 'Africa'},
        {"ID": 106, "name": 'Liberia', "short_name": 'LR', "region": 'Africa'},
        {"ID": 107, "name": 'Lesotho', "short_name": 'LS', "region": 'Africa'},
        {"ID": 108, "name": 'Malawi', "short_name": 'MW', "region": 'Africa'},
        {"ID": 109, "name": 'Namibia', "short_name": 'NA', "region": 'Africa'},
        {"ID": 110, "name": 'Niger', "short_name": 'NE', "region": 'Africa'},
        {"ID": 111, "name": 'Rwanda', "short_name": 'RW', "region": 'Africa'},
        {"ID": 117, "name": 'Zambia', "short_name": 'ZM', "region": 'Africa'},
        {"ID": 119, "name": 'Somalia', "short_name": 'SO', "region": 'Africa'},
        {"ID": 122, "name": 'Gabon', "short_name": 'GA', "region": 'Africa'},
        {"ID": 125, "name": 'Mauritius', "short_name": 'MU', "region": 'Africa'},
        {"ID": 132, "name": 'Djibouti', "short_name": 'DJ', "region": 'Africa'},
        {"ID": 137, "name": 'Eritrea', "short_name": 'ER', "region": 'Africa'},
        {"ID": 139, "name": 'Seychelles', "short_name": 'SC', "region": 'Africa'},
        {"ID": 35, "name": 'Haiti', "short_name": 'HT', "region": 'South America'},
        {"ID": 39, "name": 'Colombia', "short_name": 'CO', "region": 'South America'},
        {"ID": 43, "name": 'Argentina', "short_name": 'AR', "region": 'South America'},
        {"ID": 61, "name": 'Peru', "short_name": 'PE', "region": 'South America'},
        {"ID": 65, "name": 'Venezuela', "short_name": 'VE', "region": 'South America'},
        {"ID": 68, "name": 'Brazil', "short_name": 'BR', "region": 'South America'},
        {"ID": 80, "name": 'Paraguay', "short_name": 'PY', "region": 'South America'},
        {"ID": 84, "name": 'Bolivia', "short_name": 'BO', "region": 'South America'},
        {"ID": 89, "name": 'Ecuador', "short_name": 'EC', "region": 'South America'},
        {"ID": 103, "name": 'Guyana', "short_name": 'GY', "region": 'South America'},
        {"ID": 113, "name": 'Suriname', "short_name": 'SR', "region": 'South America'},
        {"ID": 120, "name": 'Chile', "short_name": 'CL', "region": 'South America'},
        {"ID": 124, "name": 'Uruguay', "short_name": 'UY', "region": 'South America'},
        {"ID": 138, "name": 'Aruba', "short_name": 'AW', "region": 'South America'},
        {"ID": 136, "name": 'Australia', "short_name": 'AU', "region": 'Oceania'},
        {"ID": 140, "name": 'Fiji', "short_name": 'FJ', "region": 'Oceania'},
        {"ID": 81, "name": 'Honduras', "short_name": 'HN', "region": 'Central America'},
        {"ID": 83, "name": 'Nicaragua', "short_name": 'NI', "region": 'Central America'},
        {"ID": 85, "name": 'Guatemala', "short_name": 'GT', "region": 'Central America'},
        {"ID": 93, "name": 'Panama', "short_name": 'PA', "region": 'Central America'},
        {"ID": 100, "name": 'Belize', "short_name": 'BZ', "region": 'Central America'},
        {"ID": 142, "name": 'Jamaica', "short_name": 'JM', "region": 'Carribeans'},
        {"ID": 143, "name": 'Barbados', "short_name": 'BB', "region": 'Carribeans'},
        {"ID": 144, "name": 'Bahamas', "short_name": 'BS', "region": 'Carribeans'},
        {"ID": 145, "name": 'Dominica', "short_name": 'DM', "region": 'Carribeans'},
        {"ID": 146, "name": 'Grenada', "short_name": 'GD', "region": 'Carribeans'},
        {"ID": 147, "name": 'Montserrat', "short_name": 'MS', "region": 'Carribeans'}
    ]
    return [Service(data["ID"], data["name"], data["short_name"], data["region"]) for data in service_data]


class ServiceList:
    def __init__(self):
        self.services = _create_default_services()

    def add_service(self, service):
        self.services.append(service)

    def remove_service(self, service):
        self.services.remove(service)

    def get_services(self):
        return self.services

    def get_service_by_id(self, id):
        for service in self.services:
            if service.id == id:
                return service

        return None

