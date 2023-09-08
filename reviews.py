import pandas as pd

#read in data
reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

#number of reviews per country
country_count = reviews.country.value_counts()
#print(country_count)

#average points per country, rounded to one decimal place 
avg_points = reviews.groupby('country')['points'].mean().round(1)

#need to create DataFrame to contain data 
df = pd.DataFrame.merge(country_count, avg_points, on = 'country')
#this merge thing is weird, maybe revise
#print(df)

#write data to csv
df.to_csv('data/reviews-per-country.csv')