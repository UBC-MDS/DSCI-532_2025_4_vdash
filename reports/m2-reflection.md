# Reflection

## 1. Implemented Features
We have implemented most of the features outlined in our proposal. Our dashboard includes:
- **Currency Switch**: Toggles between CAD and USD for price visualization.
- **Company Selection Dropdowns**: Used for selecting companies in both overview and detailed analysis.
- **Fuel Type Dropdown**: Filters data based on fuel types.
- **Price Range Selector**: Filters cars based on their price.
- **Total Speed Range Selector**: Filters cars by their top speed.
- **Seat Number Range Selector**: Filters cars based on seating capacity.

All components are properly linked via callbacks to update charts dynamically.

## 2. Data Visualizations
- **Horsepower Boxplot**: Displays the distribution of horsepower across different selected filters, allowing users to compare performance variations. This visualization helps in identifying outliers and trends within specific categories.

## 3. Pending and Differentiated Implementations
- The structure follows our original sketch with minor usability enhancements:
  - Improved layout organization for better screen space utilization
  - Enhanced filter positioning for more intuitive user interaction
  - Refined chart placement for better visual flow

## 4. Known Issues
- Some callback interactions need refinement for smoother data updates.
- Performance optimization is needed as filtering large datasets causes slight lag.

## 5. Reflection on Best Practices
- Minor improvements can be made in responsiveness and color schemes.
- We chose to use Altair instead of Plotly because Altair's concise syntax and built-in statistical transformations made it a better choice for our needs.
- We adhered to best practices in component modularization for reusability, and better composability in our visualizations.

Minor improvements can be made in responsiveness and color schemes.

## 6. Strengths and Future Improvements
### Strengths:
- Interactive and easy to navigate.
- Multiple filtering options enhance data breakdown.
- Modular architecture enables easy expansion.

### Limitations:
- Performance could improve for large datasets.
- Some UI elements need better spacing and organization.

### Future Improvements:
- Optimize layout styling for better consistency and readability.
- Standardize unit formatting across visualizations.
- Improve filter range selection for better user control.
- Enhance error handling with informative messages when data fails to load or inputs are invalid.
- Optimize callback functions for better performance.
- Add interactive elements like hover-over tooltips.

By addressing these issues, our dashboard will be more robust and user-friendly.

## 7. Additional Input and Output Component: Car Type Dropdown
We introduced Car Type Dropdown (`car_types_dropdown`), which allows users to filter cars by type, enhancing detailed analysis.

### Implementation Details:
- **Input Component**: Dropdown listing various car types.
- **Output Component**: All charts in the detailed analysis section dynamically update based on selection.
- **Callback Mechanism**: A callback listens for `car_types_dropdown` changes, filtering data before updating visualizations.

### Justification for Adding Car Type Dropdown:
- Improves user control through refined data filtering.
- Enhances detailed analysis by enabling easier car type comparisons.
- Aligns with our goal of providing multiple filtering options for an enriched interactive experience.