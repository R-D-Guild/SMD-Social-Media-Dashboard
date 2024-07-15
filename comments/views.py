from django.shortcuts import render
from .forms  import FilterYtForm
from django.shortcuts import render
from django.http import JsonResponse
from .forms import DatePickerForm
from .models import YourModel  # Replace with your actual model
import pandas as pd
import plotly.express as px
import plotly.io as pio

import requests
import pandas as pd


# Create your views here.
def Home(request):
    return render(request, 'dashboard.html')
def Posting(request):
    return render(request, 'posting.html')

def youtube_view(request):
    form = DatePickerForm()
    context = {'form': form}

    if request.method == 'POST':
        form = DatePickerForm(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['date1']
            date2 = form.cleaned_data['date2']

            df = fetch_youtube_data(YOUTUBE_API_KEY, CHANNEL_ID, date1, date2)

            # Create the graphs
            views_fig = px.line(df, x='date', y='views', title='Views Over Time')
            subs_fig = px.line(df, x='date', y=['subscribersGained', 'subscribersLost'], title='Subscribers Over Time')
            interactions_fig = px.line(df, x='date', y=['likes', 'comments'], title='Interactions Over Time')

            # Convert the graphs to HTML
            views_html = pio.to_html(views_fig, full_html=False)
            subs_html = pio.to_html(subs_fig, full_html=False)
            interactions_html = pio.to_html(interactions_fig, full_html=False)

            context.update({
                'views_graph': views_html,
                'subs_graph': subs_html,
                'interactions_graph': interactions_html
            })

    return render(request, 'youtube.html', context)

def fetch_youtube_data(api_key, channel_id, start_date, end_date):
    base_url = 'https://www.googleapis.com/youtube/v3'
    metrics = ['views', 'subscribersGained', 'subscribersLost', 'likes', 'comments']
    data = {metric: [] for metric in metrics}
    data['date'] = []

    params = {
        'part': 'statistics',
        'channelId': channel_id,
        'key': api_key,
    }

    response = requests.get(f"{base_url}/channels", params=params).json()
    
    # Normally, you should fetch daily data, but YouTube API v3 does not provide such granularity.
    # Instead, you can fetch data for a range and calculate the deltas yourself.
    # For more granular data, consider YouTube Analytics API.

    # Simulate daily data for the sake of example
    current_date = start_date
    while current_date <= end_date:
        for metric in metrics:
            data[metric].append(response['items'][0]['statistics'].get(metric, 0))
        data['date'].append(current_date.strftime('%Y-%m-%d'))
        current_date += pd.DateOffset(days=1)

    return pd.DataFrame(data)
