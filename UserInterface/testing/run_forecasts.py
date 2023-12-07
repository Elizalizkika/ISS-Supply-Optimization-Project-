from flask import Flask, render_template, request, jsonify
#from q2q3 import create_table #update when folder name changes
from q2q3_food import create_table_food
from q2q3_oxygen import create_table_oxygen
from q2q3_water import create_table_water
from acy_inserts import create_table_acy
from filter_inserts import create_table_fi
from kto import create_table_kto
from nitrogen import create_table_nitrogen
from pretreat_tanks import create_table_pt
from urine_receptacle import create_table_ur
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.offline as pyo
import io
import base64
import os

#app = Flask(__name__)  
app = Flask(__name__, static_url_path='/static')

@app.route('/')

def index():
    message = f'Select Consumable'

    return render_template('forecast.html', message=message)

@app.route('/run_script', methods=['POST']) #METHODS WITH AN S

def run_script(): #name of this function is where route goes
    #consumable = request.form.get('consumable_name')
    consumable = request.form['consumable_name']
    if consumable == 'Water':
        #table_data = create_table_water(consumable)
        #return render_template('forecast.html', table_data=table_data, consumable=consumable)
        info = create_table_water(consumable)
        unit = 'L'
    elif consumable == 'Oxygen':
        info = create_table_oxygen(consumable)
        unit = 'lbs'
    elif consumable == 'US Food BOBs':
        info = create_table_food(consumable)
        unit = 'BOBs'
    elif consumable == 'ACY Inserts':
        info = create_table_acy(consumable)
        unit = 'Inserts'
    elif consumable == 'Filter Inserts':
        info = create_table_fi(consumable)
        unit = 'Inserts'
    elif consumable == 'KTO':
        info = create_table_kto(consumable)
        unit = 'KTOs'
    elif consumable == 'Nitrogen':
        info = create_table_nitrogen(consumable)
        unit = 'lbs'
    elif consumable == 'Pretreat Tanks':
        info = create_table_pt(consumable)
        unit = 'Pretreat Tanks'
    elif consumable == 'Urine Receptacle':
        info = create_table_ur(consumable)
        unit = 'Receptacles'

    message = f'Consumable selected: {consumable}'
    table_d = info[0]
    docking_days = info[3]
    need_to_send_list = info[4]
    #make plot ----------------
    fig = px.scatter(x=docking_days, y=need_to_send_list, color=docking_days, color_continuous_scale='Viridis', title='Consumables Needed')
    fig.update_layout(xaxis_title='Docking Days', yaxis_title='Amount Needed')
    fig.update_layout(template='plotly_dark')
    #fig.update_layout(plot_bgcolor='rgba(15, 15, 15, 0.7)', paper_bgcolor='rgba(15, 15, 15, 0.9)')
    #Generate standalone HTML
    plot_html = pyo.plot(fig, include_plotlyjs=False, output_type='div', show_link=False)

    fig2 = px.line(x=docking_days, y=need_to_send_list)
    fig2.update_layout(xaxis_title='Docking Days', yaxis_title='Amounts')
    fig2.update_layout(template='plotly_dark')
    line_html = fig2.to_html(include_plotlyjs=True, full_html=False)

    fig3 = px.bar(x=docking_days, y=need_to_send_list, title='Consumables')
    fig3.update_layout(xaxis_title='Docking Days', yaxis_title='Amounts')
    fig3.update_layout(template='plotly_dark')
    bar_html = fig3.to_html(include_plotlyjs=True, full_html=False)


    #plot end----------------
    g_date = info[1]
    greatest_qty = info[2]
    greatest_date = f'Date with highest consumable amount: {g_date}'
    qty = f'The greatest amount of consumable needed: {greatest_qty} {unit}'
    table_data = table_d.to_html(classes='table', index=False)
    percent_diff_q = f'Difference percentage between the next two years and the historical usage:'
    percent_d = info[5]
    percent_diff = f'{percent_d}%'
    days_rem = info[6]

    return render_template('forecast.html', message=message, table_data=table_data,
                            consumable=consumable, greatest_date=greatest_date,
                            qty=qty, plot_html=plot_html,bar_html=bar_html,
                            percent_diff_q=percent_diff_q, percent_diff=percent_diff,
                            days_rem=days_rem)
    
 


if __name__ == '__main__':
    app.run(debug=True)







#cut out not necessary 
'''
       #table_data = create_table_oxygen(consumable)
        #return render_template('forecast.html', table_data=table_data, consumable=consumable)
        info = create_table_oxygen(consumable)
        table_d = info[0]
        docking_days = info[3]
        need_to_send_list = info[4]
        #make plot ----------------
        fig = px.scatter(x=docking_days, y=need_to_send_list, color=docking_days, color_continuous_scale='Viridis', title='Consumables Needed')
        fig.update_layout(xaxis_title='Docking Days', yaxis_title='Amount Needed')
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor='rgba(15, 15, 15, 0.7)', paper_bgcolor='rgba(15, 15, 15, 0.9)')
        #Generate standalone HTML
        plot_html = pyo.plot(fig, include_plotlyjs=False, output_type='div', show_link=False)

        fig2 = px.line(x=docking_days, y=need_to_send_list)
        fig2.update_layout(xaxis_title='Docking Days', yaxis_title='Amounts')
        fig2.update_layout(template='plotly_dark')
        line_html = fig2.to_html(include_plotlyjs=True, full_html=False)


        #plot end----------------
       
        g_date = info[1]
        greatest_qty = info[2]
        greatest_date = f'Date with highest consumable amount: {g_date}'
        qty = f'The greatest amount of consumable needed: {greatest_qty}'
        table_data = table_d.to_html(classes='table', index=False)
        return render_template('forecast.html', table_data=table_data,
                                consumable=consumable, greatest_date=greatest_date,
                                qty=qty, plot_html=plot_html, line_html=line_html)
    elif consumable == 'US Food BOBs':
        #table_data = create_table_food(consumable)
        info = create_table_food(consumable)
        table_d = info[0]
        docking_days = info[3]
        need_to_send_list = info[4]
        #make plot ----------------
        fig = px.scatter(x=docking_days, y=need_to_send_list, color=docking_days, color_continuous_scale='Viridis', title='Consumables Needed')
        fig.update_layout(xaxis_title='Docking Days', yaxis_title='Amount Needed')
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor='rgba(15, 15, 15, 0.7)', paper_bgcolor='rgba(15, 15, 15, 0.9)')
        #Generate standalone HTML
        plot_html = pyo.plot(fig, include_plotlyjs=False, output_type='div', show_link=False)

        fig2 = px.line(x=docking_days, y=need_to_send_list)
        fig2.update_layout(xaxis_title='Docking Days', yaxis_title='Amounts')
        fig2.update_layout(template='plotly_dark')
        line_html = fig2.to_html(include_plotlyjs=True, full_html=False)

        #plot end----------------
        g_date = info[1]
        greatest_qty = info[2]
        greatest_date = f'Date with highest consumable amount: {g_date}'
        qty = f'The greatest amount of consumable needed: {greatest_qty}'
        table_data = table_d.to_html(classes='table', index=False)
        return render_template('forecast.html', table_data=table_data,
                                consumable=consumable, greatest_date=greatest_date,
                                qty=qty, plot_html=plot_html, line_html=line_html)

'''