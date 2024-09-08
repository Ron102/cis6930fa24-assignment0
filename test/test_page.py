import pytest
import json
from unittest.mock import patch, Mock
import main
import requests

url = 'https://api.fbi.gov/wanted/v1/list'

mock_data = {
        "items": [
            {"title": "ISIAH TERRELL BILLY", "subjects": ["Seeking Information"], "field_offices": ["albuquerque"]}
        ]
    }


@patch('requests.get')
def test_download(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    response = requests.get(url)
    assert response.status_code == 200


@patch('requests.get')
def test_title(mock_get):
    mock_response = Mock()
    mock_response.content = json.dumps(mock_data)
    mock_get.return_value = mock_response
    
    with patch('builtins.print') as mock_print:
        main.api_call(page=1)
        mock_title = "ISIAH TERRELL BILLY"
        mock_print.assert_any_call(f"{mock_title}þSeeking Informationþalbuquerque")


@patch('requests.get')
def test_subjects(mock_get):
    mock_data = {
        "items": [
            {"title": "ISIAH TERRELL BILLY", "subjects": ["Seeking Information", "Indian Country", "Navajo"], "field_offices": ["albuquerque"]}
        ]
    }
    
    mock_response = Mock()
    mock_response.content = json.dumps(mock_data)
    mock_get.return_value = mock_response

    with patch('builtins.print') as mock_print:
        main.api_call(page=1)
        mock_subjects = ["Seeking Information", "Indian Country", "Navajo"]
        mock_output = f"ISIAH TERRELL BILLYþ{','.join(mock_subjects)}þalbuquerque"
        mock_print.assert_any_call(mock_output)


@patch('requests.get')
def test_field_offices(mock_get):
    mock_response = Mock()
    mock_response.content = json.dumps(mock_data)
    mock_get.return_value = mock_response

    with patch('builtins.print') as mock_print:
        main.api_call(page=1)
        mock_field_offices = ["albuquerque"]
        mock_output = f"ISIAH TERRELL BILLYþSeeking Informationþ{','.join(mock_field_offices)}"
        mock_print.assert_any_call(mock_output)


@patch('requests.get')
def test_thorn(mock_get):
    mock_response = Mock()
    mock_response.content = json.dumps(mock_data)
    mock_get.return_value = mock_response
    
    with patch('builtins.print') as mock_print:
        main.api_call(page=1)
        mock_output = "ISIAH TERRELL BILLYþSeeking Informationþalbuquerque"
        mock_print.assert_called_once_with(mock_output)


if __name__ == "__main__":
    pytest.main()
