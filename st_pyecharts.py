import streamlit as st
import pandas as pd
import numpy as np
import requests
import base64


from pyecharts import options as opts
from pyecharts.charts import Bar
#from pyecharts.charts import Line
from streamlit_echarts import st_pyecharts

######################################

#df = pd.read_csv('df1.csv')

st.header('df categories')
df = pd.read_csv('directories_sample.csv')
st.dataframe(df)

######################################

st.header('df googletrends')
dfTrends = pd.read_csv('googletrends5years.csv')
#st.write(type(dfTrends))
#st.write(dfTrends.dtypes)
#dfTrends['Week'] = pd.to_datetime(dfTrends['Week'], format='%Y-%m')
dfTrends['Week'] = pd.to_datetime(dfTrends['Week']).dt.normalize()


st.write(dfTrends.dtypes)
st.dataframe(dfTrends)

######################################

TrendsDateList = dfTrends['Week'].tolist()
TrendsTerm01List = dfTrends.iloc[:,1].tolist()
TrendsTerm02List = dfTrends.iloc[:,2].tolist()
TrendsTerm03List = dfTrends.iloc[:,3].tolist()

######################################

# catList

catList = df['cat'].tolist()
catListShort = catList[:5]
RevenueList = df['number'].tolist()

#region 01

st.markdown('# Google Trends test 01')

from pyecharts.charts import Line

bTrends = (
    Line()
    #.add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_xaxis(
    TrendsDateList
)
        .add_yaxis(
    "Revenue in B$",
    TrendsTerm01List,
    #category_gap = "10%"
    #is_large = True,
    #is_show_background = True,
)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
     #   toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(bTrends)

############################

st.markdown('# LINE LINE WIP WIP - Google Trends test 02')

bTrends2  = (
     Line ()
    #.add_xaxis([ "SEO" , "PPC" , "Social Media" , "Display" , "Direct" , "Affiliates" , "Else" ])
    .add_xaxis(TrendsDateList)
    #.add_yaxis( "Business A" , [ 114 , 55 , 27 , 101 , 125 , 27 , 105 ])
    .add_yaxis( "Search Term A" , TrendsTerm01List)
    .add_yaxis( "Search Term B" , TrendsTerm02List)
    .add_yaxis( "Search Term C" , TrendsTerm03List)
  #  .add_yaxis( "Business B" , [ 57 , 134 , 137 , 129 , 145 , 60 , 49 ])
    .set_global_opts( title_opts = opts.TitleOpts( title = "Google Trends" ))
)
bTrends2.render()

st_pyecharts(bTrends2)

################################################


#RevenueList = [21.2, 20.4, 10.3, 6.08, 4, 2.2]

#TrendsDateList

b = (
    Bar()
    #.add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_xaxis(
    catListShort
)
        .add_yaxis(
    "Revenue in B$",
    RevenueList,
    category_gap = "10%"
    #is_large = True,
    #is_show_background = True,
)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
     #   toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)

#endregion 01

#region 02

st.markdown('# BAR CHART - Traffic (Business A vs B)')


bar  = (
     Bar ()
    .add_xaxis([ "SEO" , "PPC" , "Social Media" , "Display" , "Direct" , "Affiliates" , "Else" ])
    .add_yaxis( "Business A" , [ 114 , 55 , 27 , 101 , 125 , 27 , 105 ])
    .add_yaxis( "Business B" , [ 57 , 134 , 137 , 129 , 145 , 60 , 49 ])
    .set_global_opts( title_opts = opts.TitleOpts( title = "" ))
)
bar.render()

st_pyecharts(bar)

#endregion 02

st.markdown('# Stacked chart ')

#from pyecharts import options as opts
#from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
#    .add_xaxis(Faker.choose())
    .add_xaxis([ "shirt" , "sweater" , "tie" , "trousers" , "windbreaker" , "high heels" , "socks" ])
    .add_yaxis("a", Faker.values(), stack="stack1")
    .add_yaxis("b", Faker.values(), stack="stack1")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-c"))
#    .render("bar_stack0.html")
)

st_pyecharts(c)

