# Reflection for Milestone 4

## Additional Implementation/Refinement Since Milestone 3

The recent development efforts have been focused on:

- Improving the documentation of the charting functions and refining the user interface for better clarity and consistency.
- Originally, our dashboard had overlapping issues on narrow screens. Based on peer review feedback, we fixed the layout by setting the width of all charts to "container" to make them more responsive and prevent squishing, enhancing readability.
- Added a favicon and tab title to the dashboard, and adjusted the icon position in the header to better align with the original sketch.
- Updated currency switch logic to use `ctx` instead of number of clicks, making it more reliable and responsive after multiple clicks.
- UI and Labeling Updates:  Updated Total Speed to Top Speed (km/h) across all instances in the UI, including tooltips and charts.
- Developed tests for data processing functions and visualization output functions.
- Reduced latency and improving efficiency by caching and vectorizing operations.

## Differences from Proposal/Sketch

- Same as milestone 2 and 3, no updates.

## Known Issues and Corner Cases

- The gauges are not set to "container" width, as we found it challenging to adjust the text font size responsively. Hence, they may not be fully responsive, but they should still display properly on most screens.

## Deviations from DSCI 531 Best Practices

- Same as milestone 2 and 3, no updates.

## Overall Dashboard Reflection

- **Strengths**:
  - Well-structured and interactive UI that presents data effectively
	- Good balance of information density and clarity without overwhelming the user.
	- Efficient filtering and visualization updates for better exploration.

- **Limitations and Future Improvements**:
  - Further optimize the layout to adapt better to mobile and tablet screens.

## (Challenging) Set Up Tests and Write Docstrings

- Added detailed docstrings for all charting functions within the dashboard.  
- Documented parameters and return values for all chart-related functions to improve readability and ease of future modifications.  
- These updates ensure better maintainability and understanding of the charting logic for developers.  
- Test cases for data processing functions: extract_min_value, clean_capacity, categorize_car_type.
- Test cases for visualization output functions: max_speed_horsepower, empty data handling in visualization components, and schema verification for boxplots and histograms.
