def get_population(country_dict):
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),     
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])           
    }
    keys = population_dict.keys()
    values = population_dict.values()
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

def get_population_percentage(data):
    country_percentage = {}
    for i in range(len(data)):
        country_percentage[data[i]['Country/Territory']] = float(data[i]['World Population Percentage'])
    keys = country_percentage.keys()
    values = country_percentage.values()
    return keys, values
        
        
    


