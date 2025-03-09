# Reflection for Milestone 3

## Features Implemented Since Milestone 2

- **Structural Improvements**: Used tabs for better navigation between sections.
  - **Company Overview tab**: Bar charts and histograms for company-wise information.
  - **Detailed Analysis tab**: Scatter plots, box plots, and interactive comparisons.
  - **About tab**: Added an "About" section explaining the motivation, purpose, and key features to enhance user understanding.
- **Remove Redundant Inputs**:
  - Removed input boxes for speed and seats to reduce clutter.
  - Removed the price slider due to outliers, using input boxes for price range selection only.
- **Enhance Slider Display**: Ensured sliders always display selected values.
- **Consistent Sidebar Length**: Previously, the sidebar in the Company Overview was full width, unlike in Detailed Analysis. We made the sidebar length consistent across sections to improve layout.
- **Currency Switch Highlighting**: Updated currency switch buttons to highlight the selected option.
- **Consistent Colors Across Related Visualizations**:
  - **Consistent Colors Between Boxplots**: Previously, the Horsepower Boxplot had opacity, while the Price Boxplot did not. We fixed this inconsistency by removing opcaity for both.
  - **Consistent Colors Between Bar chart and Histogram**: The bar chart and histogram in the Company Overview section now also use the same color scheme for consistency.
- **Add Spacing Between Radio Buttons**: Previously, there was no spacing between radio buttons. We have now added spacing to improve the interface.

## Features Unimplemented In Feedback

- **Fix Overflow Boxes at 100%**: Resolved as a result of removing input boxes.

## Differences from Proposal/Sketch

- **Introduction of Tabs**: We added tabs to organize the dashboard, improving navigation and reducing information overload.
- **Removal of Redundant Inputs**: We removed the input boxes for speed and seats to reduce clutter.
- **Enhanced Slider Display**: The slider will always display the selected values.

## Known Issues and Corner Cases

- **Currency Switch Resets Price Range**: Currency switch resets the price range to default, which may be inconvenient for users.
- No other corner cases have been identified.

## Deviations from DSCI 531 Best Practices

- Same as milestone 2, no updates.

## Overall Dashboard Reflection

- **Strengths**:
  - The dashboard is well-organized with tabs and fully functional.
  - Visualizations are clear and informative, giving a comprehensive view of the data.
  - The "About" section clearly explains the dashboard's purpose and features.

- **Limitations and Future Improvements**:
  - The visual appearance, including the background color and the input widgets design, could be improved for better aesthetics.
  - The dashboard performance is not optimal with our large dataset; optimization techniques are needed to ensure a smooth user experience.

## (Challenging) Inspiration from Another Group

- We were inspired by [Group 1](https://github.com/UBC-MDS/DSCI-532_2025_1_cookie-dash)'s use of gauges to display summary statistics. This approach enhances the user experience by providing a quick, visual overview of key metrics, making it easier for users to interpret important data at a glance. So instead of using a summary card with plain text, we implemented two gauges to show the maximum total speed and horsepower for selected companies.
