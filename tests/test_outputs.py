import os
import sys
import pytest
import pandas as pd
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.components.outputs import (
    max_speed_horsepower, 
    empty_warning_plot,
    plot_bar_chart,
    plot_grouped_histogram,
    plot_boxplot_price,
    plot_boxplot_horsepower,
    horsepower_price
)

def test_max_speed_horsepower():
    empty_df = pd.DataFrame()
    assert max_speed_horsepower(empty_df) == (None, None)
    
    test_df = pd.DataFrame({
        'total_speed': [200, 180, 220],
        'horsepower': [300, 250, 350]
    })
    max_speed, max_hp = max_speed_horsepower(test_df)
    assert max_speed == 220
    assert max_hp == 350

def test_empty_warning_plot():
    plot_dict = empty_warning_plot()
    assert isinstance(plot_dict, dict)
    assert 'mark' in plot_dict
    assert plot_dict['mark']['text'] == 'No data available'
    assert 'config' in plot_dict

def test_plot_boxplot_price():
    empty_df = pd.DataFrame()
    empty_plot = plot_boxplot_price(empty_df, 'company_names')
    assert isinstance(empty_plot, dict)
    assert 'mark' in empty_plot
    
    test_df = pd.DataFrame({
        'company_names': ['AUDI', 'BMW', 'Tesla'],
        'cars_prices_cad': [50000, 75000, 60000],
        'cars_prices_usd': [40000, 60000, 48000]
    })
    chart_dict = plot_boxplot_price(test_df, 'company_names', 'cars_prices_cad')
    assert isinstance(chart_dict, dict)
    assert '$schema' in chart_dict

def test_plot_boxplot_horsepower():
    empty_df = pd.DataFrame()
    empty_plot = plot_boxplot_horsepower(empty_df, 'company_names')
    assert isinstance(empty_plot, dict)
    assert 'mark' in empty_plot
    
    test_df = pd.DataFrame({
        'company_names': ['AUDI', 'BMW', 'Tesla'],
        'horsepower': [300, 400, 450],
        'cars_prices_cad': [50000, 75000, 60000]
    })
    chart_dict = plot_boxplot_horsepower(test_df, 'company_names')
    assert isinstance(chart_dict, dict)
    assert '$schema' in chart_dict