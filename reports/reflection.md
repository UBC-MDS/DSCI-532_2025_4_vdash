# Reflection on Milestone 2

For this milestone: the following key implementations have been made based on our app sketch and proposal:

## Data Visualizations:

- Bar Chart: depicting the number of car models per company for manufacturer comparison.  
- Histogram displaying car price distribution within a selected company.  
- Boxplots- visualizing horsepower and price distribution by company, car type, and fuel type.  
- Scatterplot highlighting the relationship between horsepower (or performance) and price which helps with identifying value propositions among various models.

## Currency for price stability: 
The dashboard uses a 1.27 CAD/USD exchange rate to ensure consistency in price comparisons with the dataset's static pricing and avoid distortions from currency fluctuations

## Limitations and Future directions

Real-time currency conversion via APIs poses challenges like rate fluctuations, API limits, and inconsistencies with static dataset pricing, making offline functionality essential. 
A practical approach is to fetch exchange rates periodically from reliable sources, store them locally, and default to the last stored rate if the API fails to ensure stability.