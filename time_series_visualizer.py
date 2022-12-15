import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df.value > df.value.quantile(.025)) & (df.value < df.value.quantile(.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20,6))

    df.plot(ax=ax, legend=None, rot=0);
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date');

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_y_m = df.copy()
    df_y_m['Year'] = df_y_m.index.year
    # df_y_m['Month'] = df_y_m.index.strftime("%B")
    df_y_m['Month'] = df_y_m.index.month
    df_bar = df_y_m

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8,8))

    pd.pivot_table(df_bar.reset_index(),
                index='Year', 
                columns='Month', 
                values='value'
                ).plot(kind='bar', xlabel='Years', 
                        ylabel='Average Page Views', 
                        ax=ax);
    ax.legend(title='Months', 
            labels=[calendar.month_name[idx] for idx in range(1,13)]);

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
