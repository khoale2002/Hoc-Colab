import pandas as pd
result = pd.read_csv('khoa.csv')
print(result.head(10))
pdi = 'https://www.stats.govt.nz/assets/Uploads/Business-price-indexes/Business-price-indexes-September-2020-quarter/Download-data/business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.csv'
data = pd.read_csv(pdi)
print(data.head(10))
js = 'https://data.cese.nsw.gov.au/data/dataset/027493b2-33ad-3f5b-8ed9-37cdca2b8650/resource/af20d17c-a7ac-4251-af75-e5ae66573e92/download/collections.json'
data1 = pd.read_json(js)
print(data1.head(10))

