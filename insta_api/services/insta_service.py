import os
import requests

ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')
BASE_URL = os.getenv('INSTAGRAM_GRAPH_API_URL')

def get_instagram_feed():
    endpoint = f"{BASE_URL}me/media"
    params = {
        'fields': 'id,caption,media_type,media_url,permalink,thumbnail_url',
        'access_token': ACCESS_TOKEN,
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Instagram feed: {e}")
        return []
