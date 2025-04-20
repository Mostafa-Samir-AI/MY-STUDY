---
author: Mostafa Samir Ali
tags:
  - AI
  - data_pre_processing
---

# Matplotlib
---

## 1. Introduction

This notebook serves as a complete guide to data visualization using Python's powerful libraries: **Matplotlib**, **Pandas**, and **NumPy**. It covers various types of plots and charts, demonstrating how to create, customize, and analyze them effectively. The notebook is structured into multiple sections corresponding to different video tutorials, each focusing on a specific type of visualization.

### Objectives:

- To understand the fundamentals of data visualization using Matplotlib.
- To learn how to handle and visualize data using Pandas.
- To explore advanced customization techniques for creating professional-grade plots.
- To provide practical examples and use cases for each plot type.

### Why Use Matplotlib?

Matplotlib is one of the most popular data visualization libraries in Python due to its versatility and ease of customization. It provides control over every aspect of a figure, making it a favorite among data scientists and analysts for creating publication-quality visuals.

### Key Libraries Used:

- **Matplotlib**: For creating static, animated, and interactive plots.
- **Pandas**: For data manipulation and analysis, particularly with CSV data.
- **NumPy**: For numerical operations, particularly for handling arrays and data ranges.

---

## 2. Video-wise Explanation

This section provides detailed explanations of each code block used in the notebook, corresponding to each video tutorial.

---

### Video 1: Creating and Customizing Plots

#### Overview:

This section introduces the basics of line plots using Matplotlib, focusing on customizing plots with labels, titles, legends, grid lines, and styles.

#### Code Explanation:

- **Basic Line Plot**:
    
    ```python
    plt.plot(ages_x , py_dev_y) 
    plt.title("Python Developers")
    plt.xlabel("Ages")
    plt.ylabel("Salary")
    plt.show()
    ```
    
    - `plt.plot()` creates a basic line plot.
    - `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` add context to the plot.
    - `plt.show()` displays the plot.
- **Multiple Line Plots with Labels and Legend**:
    
    ```python
    plt.plot(ages_x, py_dev_y, linewidth=3, label='Python')
    plt.plot(ages_x, js_dev_y, 'y*--', label='JavaScript')
    plt.plot(ages_x, dev_y, color='#444444', linestyle='-', marker='*', label='All Devs')
    plt.legend()
    plt.show()
    ```
    
    - Multiple plots are displayed in the same figure using different colors, markers, and line styles.
    - `plt.legend()` automatically uses the labels provided in each `plot()` call.

#### Customization Techniques:

- `plt.style.use('classic')`: Changes the overall look of the plot.
- `plt.grid()`: Adds grid lines for better readability.
- `plt.tight_layout()`: Adjusts padding to avoid overlapping elements.

#### Output Description:

The output displays three line plots for Python, JavaScript, and All Developers’ salaries, clearly distinguished by colors and markers.

#### Use Cases:

- Comparing trends over time or across categories.
- Analyzing salary trends among different developer roles.

---

### Video 2: Bar Chart and Analyzing Data from CSV

#### Overview:

This section demonstrates how to create grouped bar charts and how to analyze data from CSV files using Pandas.

#### Bar Chart:

- **Grouped Bar Chart**:
    
    ```python
    width = 0.25
    plt.bar(x_index-width, py_dev_y, label='Python', width=width)
    plt.bar(x_index, js_dev_y, label='JavaScript', width=width)
    plt.bar(x_index+width, dev_y, color='#444444', label='All Devs', width=width)
    plt.legend()
    plt.show()
    ```
    
    - `plt.bar()` is used to create vertical bar charts.
    - Bars are grouped by adjusting the position using `x_index` and `width`.
- **Working with CSV Data**:
    
    ```python
    data = pd.read_csv("matplotlib_data.csv")
    data["LanguagesWorkedWith"] = data["LanguagesWorkedWith"].apply(lambda x: x.split(";"))
    ```
    
    - `pd.read_csv()` reads the CSV file.
    - `.apply(lambda x: x.split(";"))` splits languages into a list for each respondent.

#### Output Description:

The grouped bar chart displays salary comparisons for Python, JavaScript, and All Developers side by side for each age group.

#### Use Cases:

- Visualizing categorical data distributions.
- Comparing multiple categories side by side.

---

### Video 3: Pie Chart

#### Overview:

Explores the creation of pie charts for representing parts of a whole.

#### Code Explanation:

```python
slices = [60, 40, 90]
plt.pie(slices, labels=["First", "Second", "Third"], wedgeprops={'edgecolor': 'black'})
plt.legend()
plt.show()
```

- `plt.pie()` creates a pie chart.
- `labels` adds categories to each slice.
- `wedgeprops` customizes the appearance of slices.

#### Best Practices:

- Use pie charts for a small number of categories.
- Avoid using pie charts when categories are numerous or values are similar.

---

### Video 4: Stack Plot

#### Overview:

Stack plots are used to visualize data composition over time.

#### Code Explanation:

```python
plt.stackplot(minutes, player1, player2, player3, labels=labels, zorder=2)
plt.legend(loc=(0.07, 0.05))
plt.show()
```

- `plt.stackplot()` shows the cumulative contribution of each category.
- `zorder=2` ensures the grid appears behind the plots.

#### Use Cases:

- Showing cumulative totals over time.
- Visualizing resource allocation or composition changes.

---

### Video 5: Filling Area on Line Plot

#### Overview:

This section explains how to fill areas under or between curves for enhanced visual emphasis.

#### Code Explanation:

```python
plt.fill_between(ages, python, all_dev, where=(python > all_dev), color="green", alpha=0.25, label="Above average")
```

- `plt.fill_between()` fills the area between two curves.
- `where` parameter allows conditional filling.
- `alpha` controls transparency.

#### Use Cases:

- Highlighting areas of interest, such as profit vs. loss.
- Emphasizing deviations from an average.

---
### Video 6: Histogram

#### Overview:

Histograms are used to visualize the distribution of data by grouping data into bins. This section demonstrates how to create histograms with custom bin sizes, labels, and additional statistical indicators like medians.

#### Code Explanation:

```python
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90]
med = 29
color = '#fc4f30'

plt.hist(data["Age"], bins=bins, edgecolor="black")
plt.axvline(med, color=color, label="Age Median")
plt.legend()
plt.show()
```

- `plt.hist()` is used to create the histogram.
    - `bins`: Defines the edges of each bin, controlling the distribution's granularity.
    - `edgecolor="black"` makes the separation between bins more visible.
- `plt.axvline()` adds a vertical line to indicate the median.
- `plt.legend()` labels the median line.

#### Customization Techniques:

- `plt.style.use("fivethirtyeight")`: Applies a modern, clean style to the plot.
- `plt.grid(visible=False)`: Disables grid lines for a cleaner look.

#### Output Description:

- Displays a histogram showing the age distribution.
- A red line marks the median, providing a quick visual reference for central tendency.

#### Use Cases and Practical Applications:

- Analyzing the frequency distribution of numerical data.
- Identifying patterns such as skewness or outliers.
- Comparing distributions between different groups (e.g., age distributions across job roles).

#### Best Practices:

- Ensure the number of bins is appropriate for the data size to avoid over-smoothing or over-segmentation.
- Use edge colors for better separation between bars.

#### Potential Pitfalls:

- Choosing inappropriate bin sizes can misrepresent the data distribution.
- Overlapping histograms can be hard to interpret; consider using transparency (`alpha`) or side-by-side bar plots.

---

### Video 7: Scatter Plot

#### Overview:

Scatter plots show the relationship between two variables, helping identify correlations or patterns. This section covers basic scatter plots and more advanced customizations, including color mapping, sizing, and log scaling.

#### Code Explanation:

```python
plt.scatter(x, y, 
            s=sizes, 
            c=colors, 
            cmap="Greens",
            marker="^", 
            edgecolors="black", 
            linewidths=1,
            alpha=0.5)
cbar = plt.colorbar()
cbar.set_label("Stars")
plt.show()
```

- `plt.scatter()` creates the scatter plot.
    - `s`: Controls the size of the markers.
    - `c`: Maps color to a numerical array, enhanced by `cmap`.
    - `cmap="Greens"` specifies the color palette.
    - `marker="^"` changes the marker style to triangles.
    - `alpha=0.5` adjusts transparency for overlapping points.
- `plt.colorbar()` adds a color legend to interpret the values mapped to colors.

#### Advanced Customization:

- **Color Mapping**:
    
    ```python
    plt.scatter(view_count, likes, c=ratio, cmap="summer")
    ```
    
    - Uses the `ratio` column for color intensity.
    - `cmap="summer"` applies a yellow-green color gradient.
- **Log Scaling**:
    
    ```python
    plt.xscale("log")
    plt.yscale("log")
    ```
    
    - Logarithmic scaling helps visualize data with large variances.
    - Useful for skewed distributions or when outliers dominate the plot.

#### Output Description:

- Displays a scatter plot with varying marker sizes and colors, reflecting additional dimensions in the data.
- Color bar legend aids interpretation of color mapping.

#### Use Cases:

- Identifying correlations between two numerical variables.
- Visualizing clusters or outliers.
- Displaying multi-dimensional data by encoding additional information using color and size.

#### Best Practices:

- Use transparency (`alpha`) when many points overlap.
- Ensure color gradients are interpretable for colorblind users.

#### Potential Pitfalls:

- Overlapping points may obscure data patterns.
- Inconsistent scaling can mislead interpretations, so use log scaling where appropriate.

---

### Video 8: Time Series Data

#### Overview:

Time series plots are essential for visualizing trends over time. This section demonstrates how to plot time series data from CSV files and format date labels for better readability.

#### Code Explanation:

```python
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

plt.plot_date(price_date, price_close, linestyle="solid")
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.show()
```

- `pd.to_datetime()` converts date strings to datetime objects.
- `data.sort_values('Date')` ensures dates are in chronological order.
- `plt.plot_date()` is specialized for time series plots, automatically placing dates on the x-axis.
- `plt.gcf().autofmt_xdate()` rotates date labels for better readability.
- `mpl_dates.DateFormatter()` customizes date display format.

#### Advanced Customization:

- **Date Format Customization**:
    
    ```python
    date_format = mpl_dates.DateFormatter('%b %d, %Y')
    plt.gca().xaxis.set_major_formatter(date_format)
    ```
    
    - Formats date as "Month Day, Year" (e.g., Jan 01, 2025).
- **Handling Missing Data**:
    - Interpolation or gap markers can be used to handle missing time points.

#### Output Description:

- Displays a line plot showing time series trends.
- Date labels are formatted for clarity and non-overlapping display.

#### Use Cases:

- Tracking changes over time (e.g., stock prices, website traffic).
- Analyzing seasonality or cyclical trends.
- Visualizing time-dependent correlations.

#### Best Practices:

- Always sort data chronologically to avoid misinterpretation.
- Use appropriate date formats and avoid clutter by rotating labels.

#### Potential Pitfalls:

- Gaps in data can mislead interpretations if not handled properly.
- Overlapping date labels can clutter the plot; use `autofmt_xdate()`.

---

### Video 9: Plotting Real-Time Data

#### Overview:

Real-time data visualization is essential for monitoring dynamic systems. This section demonstrates how to plot real-time data using Matplotlib’s `FuncAnimation`.

#### Code Explanation:

```python
def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()
```

- `FuncAnimation()` continuously calls the `animate()` function at specified intervals (`interval=1000` for 1-second updates).
- `plt.cla()` clears the axis for fresh updates without overlapping lines.
- Data is reloaded in each call, allowing real-time updates as the CSV file is modified.

#### Output Description:

- The plot updates dynamically, showing real-time changes for two channels.
- Ideal for monitoring live data feeds.

#### Use Cases:

- Real-time monitoring (e.g., stock prices, sensor data).
- Displaying live metrics (e.g., server load, network traffic).

#### Best Practices:

- Ensure data source updates at a rate matching the animation interval.
- Avoid overloading memory by clearing the axis each frame.

#### Potential Pitfalls:

- Rapid updates may cause flickering; adjust `interval` for smoother animations.
- Large datasets can slow down real-time plotting.

---

### Video 10: Subplots

#### Overview:

Subplots allow multiple plots to be displayed in one figure for easy comparison. This section explains how to organize and customize subplots using `plt.subplots()`.

#### Code Explanation:

```python
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
ax1.plot(ages, python, "--", label="Python")
ax2.plot(ages, all_dev, label="All Devs")
ax1.legend()
ax2.legend()
plt.tight_layout()
plt.show()
```

- `plt.subplots()` creates a figure with multiple subplots.
    - `nrows` and `ncols` control the grid layout.
    - `sharex=True` synchronizes x-axes for easier comparison.
- `ax1.plot()` and `ax2.plot()` plot data on individual subplots.

#### Use Cases:

- Comparing multiple data series or metrics.
- Visualizing related datasets side by side.

#### Best Practices:

- Use shared axes when comparing datasets on the same scale.
- Maintain consistent styles for clarity.

---

