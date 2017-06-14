import quandl
quandl.ApiConfig.api_key = 'cZ_QsSLJCuVgr3cyz5__'
data = quandl.get_table('WIKI/PRICES', date = { 'gte': '2000-01-01', 'lte': '2017-04-21' })
print(data.tail())
# Taking only one asset
A_table = data[data["ticker"]=="A"]
# Finding unique assets
data["ticker"].unique()