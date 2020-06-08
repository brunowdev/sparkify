import numpy as np

import plotly
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as plotly_offline
import plotly.figure_factory as ff

import chart_studio.plotly as py

plotly_offline.init_notebook_mode(connected=False)

columns_abs_values = [
    {'male': 'male'},
    {'paid': 'paid'},
    {'canceled': 'churn'},
    {'n_upgrades': 'upgrades'},
    {'n_downgrades': 'downgrades'},
    {'n_actions': 'actions'},
    {'n_days':'Number of observed days'},
    {'n_ads': 'ads'},
    {'n_added_to_playlist': 'playlist added'},
    {'n_dislikes': 'dislikes'},
    {'n_errors': 'errors'},
    {'n_friends': 'friends'},
    {'n_help': 'help'},
    {'n_home': 'home'},
    {'n_likes': 'likes'},
    {'n_sess': 'sessions'},
    {'n_songs': 'songs by session'}, 
    {'n_settings': 'settings'}, 
    {'n_ads_over_songs':'ads vs. songs'},
    {'n_dislikes_over_songs':'dislikes over songs'},
    {'n_likes_over_dislikes':'likes vs. dislikes'},
    {'n_likes_over_songs':'likes vs. songs'},
    {'time_window':'observed time'},
    {'time_window_over_playback_time':'observed time vs. playback time'},
    
]

columns_avg_values = [
    {'male': 'male'},
    {'paid': 'paid'},
    {'canceled': 'churn'},
    {'session_avg_actions': 'actions'},
    {'session_avg_added_playlist': 'playlist added'},
    {'session_avg_ads': 'ads'},
    {'session_avg_dislikes': 'dislikes'},
    {'session_avg_errors': 'errors'},
    {'session_avg_friends': 'friends'},
    {'session_avg_help': 'help'},
    {'session_avg_home': 'home'},
    {'session_avg_likes': 'likes'},
    {'session_avg_playback': 'average time playing songs'},
    {'session_avg_settings': 'settings'},
    {'session_avg_songs': 'songs played by session'},
    {'time_window': 'intervals'},
    {'session_avg_time_away': 'time away'}
]

def get_abs_column_names():
    return list(map(lambda c: list(c.keys())[0], columns_abs_values))

def get_avg_column_names():
    return list(map(lambda c: list(c.keys())[0], columns_avg_values))

def plot_churn_histogram(df):

    t1 = go.Histogram(
        x = df[df.canc == 0].canc, 
        opacity = 0.75,
        name = 'Active users',
        marker = {
            'color': 'green', 
            'opacity': 0.5
        }
    )

    t2 = go.Histogram(
        x=df[df.canc == 1].canc,
        opacity=0.75,
        name='Churn users',
        marker = {
            'color': 'red', 
            'opacity': 0.5
        }
    )

    data = [t1, t2]
    layout = go.Layout(barmode = 'overlay')
    fig = go.Figure(data = data, layout = layout)
    
    fig.data[0].marker.line.width = 0
    fig.data[1].marker.line.width = 0
    
    fig.update_layout(
        title = {
            'text': 'Subscriptions',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }, 
        xaxis_title = 'Subscription', 
        yaxis_title = 'Total',
        autosize = True,
        xaxis_tickangle = 0,
        bargap = 0.1,
        xaxis=dict(
            ticktext=["Active", "Churn"],
            tickvals=[0, 1],
            tickmode = "array", 
        ),
        legend_title = '<b> Subscription </b>',
        legend = dict(
            traceorder = 'normal',
            bgcolor = 'LightSteelBlue',
            bordercolor = 'Black',
            borderwidth = 0
        ),
        margin = dict(t = 100),
        width = 1000,
        height = 500
    )

    fig.update_yaxes(automargin=True)
    fig.show()

def plot_churn_by_gender(df):
    fig = px.histogram(
        df, 
        x = 'canc',  
        facet_col = 'male', 
        histfunc = 'count',
        barmode = 'overlay', 
        color = 'canc', 
        color_discrete_sequence = ['red', 'green'], 
    )

    fig.update_layout(
        title = 'Distribution of the samples', 
        xaxis_title = 'Subscription', 
        yaxis_title = 'Total',
        xaxis_tickangle = 0,
        bargap = 0.1,  
        xaxis = dict(
            title_text = 'Females',
            ticktext = ['Active', 'Churn'],
            tickvals = [0, 1]
        ),
        xaxis2 = dict(
            title_text = 'Males',
            ticktext = ['Active', 'Churn'],
            tickvals = [0, 1]
        ),
        annotations = [
           {
              'text' : ''
           },
           {
              'text' : '',
           }
        ]
    )

    fig.update_layout(
        title = {
            'text': 'Distribution of the samples',
            'y': .9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        } 
    )

    fig.data[0].name = 'Churn'
    fig.data[2].name = 'Active'
    
    format_label = lambda gender, x = '{x}', y = '{y}': f'Subscription = %{x}<br>Gender = {gender}<br>Total = %{y}'

    fig.data[0].hovertemplate = format_label('Female')
    fig.data[3].hovertemplate = format_label('Male')
    fig.data[1].hovertemplate = format_label('Male')
    fig.data[2].hovertemplate = format_label('Female')

    fig.update_layout(
        legend = dict(
            traceorder = 'normal',
            bgcolor = 'LightSteelBlue',
            bordercolor = 'Black',
            borderwidth = 0
        ),
        margin = dict(t = 100),
        width = 1000,
        height = 500
    )
    fig.update_layout(legend_title = '<b> Subscription </b>') 
    fig.update_yaxes(automargin=False)
    
    fig.show()

def plot_churn_by_subscription_type(df):
    fig = px.histogram(
        df, 
        x = 'canc',  
        facet_col = 'paid', 
        histfunc = 'count',
        barmode = 'overlay', 
        color = 'canc', 
        color_discrete_sequence = ['red', 'green'], 
    )

    fig.update_layout(
        title = {
            'text': 'Churn by subscription type (<b>paid</b> or <b>free</b>)',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }, 
        xaxis_title = 'Subscription', 
        yaxis_title = 'Total',
        xaxis_tickangle = 0,
        bargap = 0.1,  
        xaxis = dict(
            title_text = 'Free',
            ticktext = ['Active', 'Churn'],
            tickvals = [0, 1]
        ),
        xaxis2 = dict(
            title_text = 'Paid',
            ticktext = ['Active', 'Churn'],
            tickvals = [0, 1]
        ),
        annotations = [ { 'text' : '' } ] * 2
    )

    fig.data[0].name = 'Churn'
    fig.data[2].name = 'Active'
    
    format_label = lambda gender, x = '{x}', y = '{y}': f'Subscription = %{x}<br>Type = {gender}<br>Total = %{y}'

    fig.data[0].hovertemplate = format_label('Free')
    fig.data[3].hovertemplate = format_label('Paid')
    fig.data[1].hovertemplate = format_label('Paid')
    fig.data[2].hovertemplate = format_label('Free')

    fig.update_layout(
        legend = dict(
            traceorder = 'normal',
            bgcolor = 'LightSteelBlue',
            bordercolor = 'Black',
            borderwidth = 0
        ),
        legend_title = '<b> Subscription </b>',
        margin = dict(t = 100),
        width = 1000,
        height = 500
    ) 
    
    fig.update_yaxes(automargin = False)
    fig.show()

def feature_corr_or_empty(value, min_to_show = .1, max_to_show = .99):
    _value = np.around(value, 2) #'' if (value < min_to_show or value > max_to_show) else value
    #if value > .75 and _value != '':
    #    _value = f'<b>{_value}</b>'
    return _value

def plot_heatmap(df, column_map, title):

    columns_names = list(map(lambda c: list(c.keys())[0], column_map))
    columns_aliases = list(map(lambda c: list(c.values())[0], column_map))
    
    df_corr = df[columns_names].corr() 
    corr_values = np.around(df_corr.values, 2)
    
    z = corr_values[::-1]
    x = columns_aliases
    y = x[::-1] 

    annotations = np.vectorize(feature_corr_or_empty, cache = False)(z)

    fig = ff.create_annotated_heatmap(z, x, y, annotation_text = annotations, colorscale = 'VIRIDIS')

    fig.update_layout(
        title = {
            'text': title,
            'y': 1,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'pad': dict(t = 50)
        }, 
        xaxis = dict(
            automargin = True
        ),
        yaxis = dict(
            automargin = True
        ),
        xaxis_tickangle = 330,
        autosize = True,
        margin = dict(t = 130),
        width = 1000,
        height = 1000
    )
    
    fig.show()

def plot_feature_corr_for_avg_values(df):    
    return plot_heatmap(df, columns_avg_values, 'Features and their correlation<br><i>(considering the mean average for each feature)</i><br>')

def plot_feature_corr_for_values(df):
    return plot_heatmap(df, columns_abs_values, 'Features and their correlation<br><i>(considering the total for each feature)</i><br>')    