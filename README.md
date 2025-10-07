# Housing Data Analysis

This project analyzes a housing dataset to explore price trends for houses with specific bedroom counts, using Python and Pandas. It demonstrates data cleaning, filtering, and visualization skills for AI/ML data preparation.

## Tasks Performed
- **Loaded Data**: Opened a housing CSV file using Pandas.
- **Formatted Prices**: Converted `price` column to float with one decimal place (e.g., 376000.0) for readability.
- **Calculated Statistics**: Computed minimum, maximum, and average prices for houses with 3, 4, or 5 bedrooms.
- **Cleaned Data**: Removed duplicate rows to ensure accurate analysis.
- **Filtered Expensive Houses**: Selected the top 3 most expensive houses for each bedroom count (3, 4, or 5) using `groupby` and `nlargest`.
- **Visualized Data**: Created a bar plot of average prices by bedroom count using Matplotlib.

## Insights
- Analyzed 4140  houses with 3-5 bedrooms after removing 2 duplicates.
- Minimum price: 34900.0; Maximum price: 755000.0; Average price: 180921.2.
- Top 3 most expensive houses per bedroom count identified, e.g., highest 3-bedroom house at $755000.0.
- Visualization shows price trends across bedroom counts.

## Files
- `house_price_analysist.ipynb`: Jupyter Notebook with full analysis.
- `top_expensive_houses.csv`: Top 3 expensive houses per bedroom count.
- `avg_price_by_bedrooms.png`: Bar plot of average prices.

## Tools
- Python, Pandas, Matplotlib, Jupyter Notebook (Anaconda)

*Project completed as part of Week 1 training for Junior AI/ML Engineer roles, using skills from freeCodeCamp’s Python for Data Science course.*
