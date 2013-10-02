from pandas import DataFrame, MultiIndex
 
# MongoDB document-like, JSON-like dictionary:
dic = {1 : [{'keyword1': { 'conversions1': 2,  'cost1': 1}}],
       2 : [{'keyword1': { 'value': 3 },
             'keyword2': { 'nan': 4 }}],
       3 : [{'keyword2': {'value': 5}}] }


# Converting dictionary to Pandas Series:
tuples = []
values = []

for i, key in enumerate(dic):
    for j, value in enumerate(dic[key]):
        for k, keyword in enumerate(value):
            for l, attr in enumerate(value[keyword]):
                tuples.append((key, keyword, attr))
                values.append(dic[key][j][keyword][attr])

names = ['dates', 'keywords', 'attributes']

# MultiIndex'ed Series
s = DataFrame(values, index=MultiIndex.from_tuples(tuples, names=names))[0]
type(s); s

# DataFrames
df = s.unstack(['keywords','attributes']); type(df); df
df1 = s.ix[:,'keyword1'].unstack('attributes'); type(df1); df1
df2 = s.ix[:,:,'value'].unstack('keywords'); type(df2); df2
