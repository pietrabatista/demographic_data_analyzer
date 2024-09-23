import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    df.describe()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts() # Conta quantos valores existem na coluna 'race' e mostra a ocorrência de cada raça. 

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    total = len(df)
    bachelor = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelor / total) * 100, 1)
 
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    masters_50k = len(df[(df['education'] == 'Masters') & (df['salary'] == '>50K')])

    doctorate_50k = len(df[(df['education'] == 'Doctorate') & (df['salary'] == '>50K')])

    bachelor_50k = len(df[(df['education'] == 'Bachelors') & (df['salary'] == '>50K')])

    advanced_education = len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])

    advanced_education_50k = (masters_50k + doctorate_50k + bachelor_50k)
    
    percentage_advanced_education_50k = round((advanced_education_50k / advanced_education) * 100, 1)


    # What percentage of people without advanced education make more than 50K?

    not_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    not_advanced_education_50k = len(not_advanced_education[not_advanced_education['salary'] == '>50K'])

    percentage_not_advanced_education_50k = round((not_advanced_education_50k / len(not_advanced_education)) * 100, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = advanced_education
    lower_education = not_advanced_education

    # percentage with salary >50K
    higher_education_rich = percentage_advanced_education_50k
    lower_education_rich = percentage_not_advanced_education_50k

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])

    min_hour_50k = len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])

    percentage_min_hour_50k = round((min_hour_50k / num_min_workers) * 100, 1)

    rich_percentage = percentage_min_hour_50k

    # What country has the highest percentage of people that earn >50K?

    everyone_above_50k = df[df['salary'] == '>50K']

    total_per_country = df['native-country'].value_counts()

    above_50k_per_country = everyone_above_50k['native-country'].value_counts()

    percentage_above_50k = ((above_50k_per_country / total_per_country) * 100).round(1)


    highest_earning_country = percentage_above_50k.idxmax()
    highest_earning_country_percentage = round((above_50k_per_country[highest_earning_country] / total_per_country[highest_earning_country]) * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.

    india_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    occupation_above_50k = india_50k['occupation'].value_counts()
   
    top_IN_occupation = occupation_above_50k.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
