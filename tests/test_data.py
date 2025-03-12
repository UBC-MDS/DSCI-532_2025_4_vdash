import os
import sys
import pytest
import pandas as pd
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data import extract_min_value, clean_capacity, categorize_car_type

def test_extract_min_value():
    assert extract_min_value("150") == 150.0
    assert extract_min_value("150 hp") == 150.0
    assert extract_min_value("200 km/h") == 200.0
    assert extract_min_value("150-200") == 150.0
    assert extract_min_value("$50,000") == 50000.0
    assert pd.isna(extract_min_value(None))
    assert extract_min_value("invalid") is None

def test_clean_capacity():
    assert clean_capacity('1,000"') == '1000'
    assert clean_capacity('2,500') == '2500'
    
    assert clean_capacity(1000) == 1000
    assert clean_capacity(None) is None

def test_categorize_car_type():
    test_row = {
        'cars_names': 'Test Car',
        'fuel_types': 'gas',
        'seats': 4,
        'horsepower': 300,
        'total_speed': 200,
        'performance_0_100_km/h': 5,
        'engines': 'v6'
    }
    
    sports_row = test_row.copy()
    sports_row['horsepower'] = 500
    sports_row['seats'] = 2
    assert categorize_car_type(sports_row) == 'sports'
    
    coupe_row = test_row.copy()
    coupe_row['cars_names'] = 'Test Coupe'
    coupe_row['seats'] = 2
    coupe_row['horsepower'] = 250
    assert categorize_car_type(coupe_row) == 'coupe'
    
    sedan_row = test_row.copy()
    sedan_row['seats'] = 5
    sedan_row['horsepower'] = 150
    assert categorize_car_type(sedan_row) == 'sedan'