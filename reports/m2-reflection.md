# Reflection for Milestone 2

## Features Implemented and Pending Implementation

- All buttons, dropdowns, sliders, and input boxes from the app sketch have been implemented.

    - **Currency Switch**: Toggles between CAD and USD for price visualization.
    - **Company Selection Dropdowns**: Used for selecting companies in both overview and detailed analysis.
    - **Fuel Type Dropdown**: Filters data based on fuel types.
    - **Price Range Selector**: Filters cars based on their price.
    - **Total Speed Range Selector**: Filters cars by their top speed.
    - **Seat Number Range Selector**: Filters cars based on seating capacity.

## Data Visualizations

- The summary card: showing max total speed and horsepower for selected companies.
- Bar Chart: depicting the number of car models per company for manufacturer comparison.  
- Grouped histogram: visualizing car price range for selected company.
- Boxplots: visualizing horsepower and price distribution by company, car type, and fuel type.  
- Scatterplot highlighting the relationship between horsepower (or performance) and price which helps with identifying value propositions among various models.

## Differences from Proposal/Sketch

- The structure follows our original sketch with minor usability enhancements:
  - Improved layout organization for better screen space utilization
  - Enhanced filter positioning for more intuitive user interaction
  - Refined chart placement for better visual flow

## Known Issues and Bugs

- The currency switch button occasionally malfunctions, either freezing or failing to work properly.
- The dashboard uses a 1.27 CAD/USD exchange rate to ensure consistency in price comparisons with the dataset's static pricing and avoid distortions from currency fluctuations.

## Deviations from DSCI 531 Best Practices

- Box plots were used instead of density plots, as density plots can be misleading with outliers. Although box plots may be harder for non-technical users according to DSCI 531, tooltips were added to display key summary stats, making them more user-friendly.

## Limitations and Future Improvements

- The dashboard faces occasional performance issues with the currency switch.
- Due to outliers, the current price slider may not be useful.
- Future work will focus on improving the currency switch reliability and providing more fluid interactions.

## Implement More of Our Proposal (Challenging)

- We introduced Car Type Dropdown (`car_types_dropdown`), which allows users to filter cars by type, enhancing detailed analysis.

### Implementation Details:
- **Input Component**: Dropdown listing various car types.
- **Output Component**: All charts in the detailed analysis section dynamically update based on selection.
- **Callback Mechanism**: A callback listens for `car_types_dropdown` changes, filtering data before updating visualizations.

### Justification for Adding Car Type Dropdown:
- Improves user control through refined data filtering.
- Enhances detailed analysis by enabling easier car type comparisons.
- Aligns with our goal of providing multiple filtering options for an enriched interactive experience.
Footer



