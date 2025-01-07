
import pytest
from main import read_config, check_health, calculate_availability

def test_read_config():
    config = read_config('config.yaml')
    assert len(config) > 0

def test_check_health():
    endpoints = [{'url': 'https://fetch.com/', 'method': 'GET'}]
    result = check_health(endpoints)
    assert result['https://fetch.com/'] in ['UP', 'DOWN']

def test_calculate_availability():
    health_log = {
        'fetch.com': ['UP', 'DOWN', 'UP'],
        'fetchrewards.com': ['UP', 'UP']
    }
    availability = calculate_availability(health_log)
    assert availability['fetch.com'] == 67
    assert availability['fetchrewards.com'] == 100
