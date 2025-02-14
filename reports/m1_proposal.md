# Proposal

## Section 1: Motivation and Purpose

Our role: Data Scientist Consultancy Firm

Target audience: Car Buyers and Automotive Enthusiasts

Buying a car is a significant decision that takes multiple factors into account. Many buyers struggle to navigate vast amounts of data and make informed choices that best suit their needs. To address this challenge, we propose building an interactive car comparison dashboard that allows users to visually explore and compare different vehicle models in the market based on key specifications. Our dashboard will feature dynamic filters and visualizations, enabling users to adjust criteria such as price range, horsepower, fuel type, and seating capacity to find the best options. By providing an intuitive and interactive experience, our tool aims to simplify car selection and empower buyers with data-driven insights.

## Section 2: Description of the data

For this project, we are using the Ultimate Cars Dataset 2024, sourced from Kaggle. This dataset provides detailed specifications of various car models from different manufacturers, including their performance metrics, pricing, and fuel types. Our goal is to leverage this data to create an interactive Car Performance Dashboard that will help car buyers and automotive professionals compare different vehicle models based on key attributes.

### Dataset Overview

- **Total Rows:** 1,213
- **Total Columns:** 11
- **Data Source:** [The Ultimate Cars Dataset 2024](https://www.kaggle.com/datasets/abdulmalik1518/the-ultimate-cars-dataset-2024)

### Key Variables for Visualization

We will analyze the following key variables, which are essential for helping car buyers make informed decisions:

1. **Vehicle Specifications:**
   - `Company Names`: The brand/manufacturer of the vehicle.
   - `Cars Names`: The model name of the vehicle.
   - `Engines`: Engine type (e.g., V8, V12, Electric).
   - `CC/Battery Capacity`: The engine displacement or battery capacity for electric vehicles.
   - `HorsePower`: The vehicle’s horsepower, a key performance metric.
   - `Total Speed`: The top speed of the vehicle.
   - `Performance(0 - 100 KM/H)`: The acceleration time from 0 to 100 km/h.
   - `Torque`: The amount of torque (Nm) produced by the vehicle.

2. **Pricing and Fuel Information:**
   - `Cars Prices`: The listed price range (in US dollars) of the vehicle.
   - `Fuel Types`: The type of fuel used (e.g., Petrol, Electric, Hybrid).
   - `Seats`: The number of seats in the vehicle.

### Data Engineering and New Variables

To enhance the insights provided by our dashboard, we plan to derive the following new variables:

- Performance-to-Price Ratio: A calculated metric to compare horsepower relative to the price.
- Vehicle Segmentation: Grouping cars into categories based on their seats and fuel types.

### Justification for Dataset Choice

This dataset is well-suited for our project because it provides a comprehensive and structured collection of vehicle specifications from various manufacturers. By visualizing this data, our Car Performance Dashboard will enable users to:

- Compare car models based on speed, horsepower, and acceleration.
- Filter vehicles by price, fuel type, and seating capacity to find suitable options.
- Identify trends in car performance across different manufacturers and price categories.

By integrating dynamic filters and comparisons, our dashboard will simplify the decision-making process for car buyers, while also providing valuable insights for automotive professionals to refine product development and marketing strategies.


**Reference:**

Abdulmalik, A. (2024). The Ultimate Cars Dataset 2024 [Data set]. Kaggle. Retrieved from https://www.kaggle.com/datasets/abdulmalik1518/the-ultimate-cars-dataset-2024.



## Section 3: Research questions and usage scenarios

### Research questions

The following research questions will guide the interactive analysis of this dashboard:

- How do car prices vary across different manufacturers and fuel types?  
- What is the distribution of horsepower across different car types and price ranges?
- How does battery capacity (for EVs) or engine CC (for fuel cars) correlate with total speed and acceleration performance? 
- Which car types offer the best balance of price and performance (horsepower vs. acceleration time)?  
- How does seating capacity influence price and fuel type choices?

### Usage Scenario
#### Scenario 1: Car Buyers

Emily is a mother of two living in Richmond, a suburb of Vancouver. She is looking for a spacious and safe family vehicle to accommodate her kids and their belongings. With frequent weekend trips to Whistler and interior BC, she needs a car with good highway performance and cargo space.  

Emily wants to find a family-friendly vehicle with ample seating, cargo space, and good safety features while staying within a budget.  

Tasks:

[Filter] by seating capacity (minimum 5 seats) to ensure enough space for her family.
[Set] a price range of $30,000 to $50,000 CAD to see cars within her budget.
[Compare] SUVs and minivans to assess comfort, space, and fuel efficiency.
[Check] performance metrics such as horsepower and total speed for highway travel.

Emily opens VDash and selects the 6-seater option in the seating capacity filter. She then sets the price range and compares SUVs and minivans side by side. She also checks the fuel type filter, prioritizing hybrid options to reduce long-term fuel costs. The dashboard dynamically updates, showing available options with key performance metrics like horsepower, battery capacity, and highway speed.  

Emily finds that hybrid SUVs provide the best combination of space and fuel efficiency. She selects a few options and plans a visit to local dealerships for test drives. 

#### Scenario 2: Automotive Manufacturer (Product Managers)

Sophia is a Product Manager at a global automotive manufacturer. She is responsible for guiding the development of new car models, ensuring they meet market demand, and optimizing pricing strategies to stay competitive in a rapidly changing automotive landscape. Her main goals are to [analyze] how their vehicles compare in price, performance, and fuel efficiency with those of their competitors, [explore] on what features (horsepower, speed, fuel type) consumers value most, and [compare] their products against others in the industry to identify areas of improvement.

When Sophia opens the “Car Performance Dashboard”, she sees a comprehensive view of price distribution, horsepower, and speed across different vehicle types, fuel types, and competing brands. Sophia uses the dashboard to [filter] the data by company, fuel type (electric, hybrid, gasoline), and vehicle category (e.g., SUVs, sedans, sports cars) to analyze how her company’s cars compare with others. By exploring the price distribution and performance of hybrid vehicles, Sophia notices that her company’s hybrid vehicle is priced higher than some competitors but has superior horsepower and speed. This could be a strong selling point for premium consumers who value both performance and sustainability. Based on this insight, Sophia decides to push marketing efforts that emphasize the high performance and environmental benefits of their hybrid cars.

Next, Sophia comapres the performance of their mid-range sedans compared to competitors. She notices that while their vehicles are priced competitively, their horsepower lags behind certain competitors’ models, which may be a turn-off for performance-conscious buyers. This prompts her to request a review of engineering priorities for future iterations of this model to boost its horsepower while keeping costs within the target price range.

Using the [filter] and [compare] features, Sophia is able to identify which models in the same category are offering more horsepower or better speed for a similar price. She might decide to recommend slight price adjustments to her sales team or collaborate with engineering to improve certain performance attributes to ensure their vehicles offer the best value for their customers.


## Section 4: App sketch & brief description

-TO DO-
