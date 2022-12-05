import pandas as pd

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    df = pd.read_csv(settings.BASE_DIR / 'data' / 'predictions.csv')

    best_features = [
        'ROA(C) before interest and depreciation before interest',
        'ROA(A) before interest and % after tax',
        'ROA(B) before interest and depreciation after tax',
        'Persistent EPS in the Last Four Seasons',
        'Per Share Net profit before tax (Yuan ¥)',
        'Debt ratio %',
        'Net worth/Assets',
        'Borrowing dependency',
        'Net profit before tax/Paid-in capital',
        'Working Capital to Total Assets',
        'Current Liability to Assets',
        'Retained Earnings to Total Assets',
        'Current Liability to Current Assets',
        'Liability-Assets Flag',
        'Gross Profit to Sales',
    ]

    last_index = request.POST.get('index')
    element = df.sample()
    index = element.index[0]

    while (index == last_index):
        element = df.sample()
        index = element.index[0]

    return render(request, 'index.html', {
        'index': index,
        'features': zip(best_features, element[best_features].values[0].round(2)),
        'y_true': element['y_true'].values[0],
        'y_pred': element['y_pred'].values[0],
    })
