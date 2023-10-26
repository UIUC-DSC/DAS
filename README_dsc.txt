Team DAS - Danny Silverstein, Anton Charov, and Sam Barbeau

Overview: 
Our U.S. County Recommender System is a user-friendly application designed to assist users in finding the most suitable county in the United States to live in based on their personal preferences and demographic information. By collecting a variety of data points ranging from age, race, and preferred temperature to additional specific preferences, our system provides tailored recommendations aiming to enhance the user’s quality of life and overall satisfaction in their new locale.

Languages: 
Python (cleaning), SQL (filtering counties by score), R (cleaning and generating QoL dataset)

Goal:
By prompting the user with questions, we will generate a "profile" for the user. Using this profile, we will match them to a county by generating scores that indicate the similarity between that county and the user's answers. Given our imense number of columns as seen below, our questions to the user will be prompted in such a way that they answer multiple columns in one question. To ensure that we can apply an answer from one column to another column, we generated linear regression models to assess similarity using pandas, statsmodels.formula.api, seaborn, and matplotlib.pyplot. This code can be seen in logRegressionsNotes.py. 

Using a website, we plan on matching a user to their ideal county/counties through a series of questions. Once the questions are finished, states with ideal counties (top 10 highest rated counties using SQL) will highlight yellow, allowing the user to click on the state to see more information about the county's score breakdown. 

Citations/Datasets:
- John Davis (johnjdavisiv), Kaggle: US Counties: COVID19 + Weather + Socio/Health data (big_dataset.csv). 
This dataset contains the columns: state, county, lat, lon, high_school_graduation_rate, total_population, area_sqmi, percent_uninsured, percent_some_college,eightieth_percentile_income, twentieth_percentile_income, median_household_income, annual_average_violent_crimes, percent_less_than_18_years_of_age, percent_65_and_over, percent_black, percent_american_indian_alaska_native, percent_asian, percent_native_hawaiian_other_pacific_islander, percent_hispanic, percent_non_hispanic_white, percent_drive_alone_to_work, percent_long_commute_drives_alone, percent_below_poverty, percent_unemployed_CDC, km_to_closest_station, station_name, min_winter_temp, mean_winter_temp, max_winter_temp, min_summer_temp, mean_summer_temp, max_summer_temp, snow (boolean).

The above dataset was also used by Sam to create a Quality of Life Column. His process for creating this column is explained below:
First I made a subset of the all columns county dataset with just county,state, and the columns I used to make the calculation. Then normalized the sum of the columns for each row (each row is a county) on a scale from 0,1 and took the complement (1 - x) since all the columns represent bad well being (higher data should mean lower score). Finally, I multiplied by 10 so the score is on a scale from 1,10.

- https://taxfoundation.org/data/all/state/2023-sales-tax-rates-midyear/
This dataset contains basic information about tax rates. It contains 3 columns after our cleaning process: State, State Tax Rate, and Rank.

- https://www.statista.com/statistics/1240947/cost-of-living-index-usa-by-state/
This dataset contains 2 columns after cleaning: State and Index. The greater the index, the greater the cost of living. The meaning of the Cost of Living Index (COLI) and its calculations can be found here: https://www.xpatulator.com/cost-of-living-article/How-to-Calculate-a-Cost-of-Living-Index_256.cfm

- MIT Election Data and Science Lab, 2018, "County Presidential Election Returns 2000-2020", https://doi.org/10.7910/DVN/VOQCHQ, Harvard Dataverse, V11, UNF:6:HaZ8GWG8D2abLleXN3uEig== [fileUNF]
This dataset contains political results from every US County in the 2020 Presidential Election. After cleaning, the columns contained are County, State, Party (DEM/REP), percent_dem (percent of dem votes in county), percent_rep (percent of rep votes in county).


