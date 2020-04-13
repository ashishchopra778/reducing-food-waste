import pandas as pd
from flask import Flask, render_template,request
app = Flask(__name__)
data = pd.read_csv("CTData.csv",encoding= 'unicode_escape')

app = Flask(__name__)

col = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500"]

temp_stand ={'Chill' : 4 ,
             'Frozen': -20,
             'Banana': 14,
             'DF'    : -30}

#@app.route('/temp_timeseries_day/<string:freight>/<string:box>/<string:month>/<string:day>')
@app.route('/temp_timeseries_day',methods=['GET'])
def temp_timeseries_day():
    freight = request.form.get("freight")
    box = request.form.get("box")
    month = request.form.get("month")
    day = request.form.get("day")
    
    name = freight+box+'.csv'
    tdata = pd.read_csv(name,encoding= 'unicode_escape')
    ttdata = pd.DataFrame()
    sample =  tdata[(tdata['Timestamp'].str[6:8] == day) & (tdata['Timestamp'].str[4:6] == month)]
    ttdata ['hours'] = sample.Timestamp.str[9:11]
    ttdata ['days'] = sample.Timestamp.str[6:8]
    ttdata ['Temp'] = sample['Temp']
    tempStand = data.loc[data['Freight_Box '] == int(box), 'Temp_Standard'].values[0]
    df = pd.DataFrame({'labels': ttdata['hours']+ ':00', 'values': ttdata['Temp']})
    a = 'line_chart.html'
    b = 'Temperature details inside freight' +freight + " - box " + box + " on "+str(day) + "/" + month
    v = df.values[:, 1]
    lab = df.values[:, 0]
    return render_template(a, title=b, max=temp_stand[tempStand], labels=lab, values=v, length = len(df))

#@app.route('/temp_timeseries_month/<string:freight>/<string:box>/<string:month>')
@app.route('/temp_timeseries_month',methods=['GET'])
def temp_timeseries_month():
    freight = request.form.get("freight")
    box = request.form.get("box")
    month = request.form.get("month")
    
    name = freight+box+'.csv'
    tdata = pd.read_csv(name,encoding= 'unicode_escape')
    ttdata = pd.DataFrame()
    sample =  tdata[(tdata['Timestamp'].str[4:6] == month)]
    ttdata ['hours'] = sample.Timestamp.str[9:11]
    ttdata ['days'] = sample.Timestamp.str[6:8]
    ttdata ['Temp'] = sample['Temp']
    monthlyData = ttdata.groupby('days').mean()
    tempStand = data.loc[data['Freight_Box '] == int(box), 'Temp_Standard'].values[0]
    df = pd.DataFrame({'labels': monthlyData.index+'/'+month+'/2020', 'values': monthlyData['Temp']})
    a = 'line_chart.html'
    b = 'Temperature details inside freight' +freight + " - box " + box + " in "+ month+"/2020"
    v = df.values[:, 1]
    lab = df.values[:, 0]
    return render_template(a, title=b, max=temp_stand[tempStand], labels=lab, values=v, length = len(df))

@app.route('/humidity_timeseries_month',methods=['GET'])
def humidity_timeseries_month():
    freight = request.form.get("freight")
    box = request.form.get("box")
    month = request.form.get("month")
    
    name = freight+box+'.csv'
    tdata = pd.read_csv(name,encoding= 'unicode_escape')
    ttdata = pd.DataFrame()
    sample =  tdata[(tdata['Timestamp'].str[4:6] == month)]
    ttdata ['hours'] = sample.Timestamp.str[9:11]
    ttdata ['days'] = sample.Timestamp.str[6:8]
    ttdata ['Humidity'] = sample['Humidity']
    monthlyData = ttdata.groupby('days').mean()
    df = pd.DataFrame({'labels': monthlyData.index+'/'+month+'/2020', 'values': monthlyData['Humidity']})
    a = 'line.html'
    b = 'Humidity details inside freight' +freight + " - box " + box + " in "+ month+"/2020"
    v = df.values[:, 1]
    lab = df.values[:, 0]
    return render_template(a, title=b, max=100, labels=lab, values=v)

@app.route('/overall_product_detail',methods=['GET'])
def overall_product_detail():
    name = request.form.get("name")
    
    sample =  data[(data['Product_Type'] == name)]
    print(sample)
    temp = sample['Temp_Standard'].value_counts()
    df = pd.DataFrame({'labels': temp.index, 'values': temp.values})
    a = 'bar_chart.html'
    b = 'Product details'
    v = df.values[:, 1]
    lab = df.values[:, 0]
    return render_template(a, title=b, max=30, labels=lab, values=v)


@app.route('/overall_status')
def overall_status():
    temp = data['Status'].value_counts()
    df = pd.DataFrame({'labels': temp.index, 'values': temp.values})
    a = 'bar_chart.html'
    b = 'Overall Progress Bar'
    v = df.values[:, 1]
    lab = df.values[:, 0]
    return render_template(a, title=b, max=150, labels=lab, values=v)

@app.route('/freight',methods=['GET'])
def freight():
    status = request.form.get("status")
    
    status_data = data[data['Status'] == status]
    temp = status_data['Product_Type'].value_counts()
    df = pd.DataFrame({'labels': temp.index, 'values': temp.values})
    a = 'pie_chart.html'
    b = 'Types of the products' + status
    v = df.values[:, 1]
    lab = df.values[:, 0]
    return render_template(a, title=b, max=20, set=zip(v, lab, col))

@app.route('/overall_product_details')
def overall_product_details():
    temp = data['Product_Type'].value_counts()
    df = pd.DataFrame({'labels': temp.index, 'values': temp.values})
    a = 'bar_chart.html'
    b = 'Total Product Types'
    v = df.values[:, 1]
    lab = df.values[:, 0]
    return render_template(a, title=b, max=50, labels=lab, values=v)

@app.route('/total_products_by_freight',methods=['GET'])
def total_products_by_freight():
    name = request.form.get("name")
     
    temp1 = data[data['Freight'] == name]
    temp = temp1['Product_Type'].value_counts()
    df = pd.DataFrame({'labels': temp.index, 'values': temp.values})
    a = 'pie_chart.html'
    b = 'Total Product Types in ' + name
    v = df.values[:, 1]
    lab = df.values[:, 0]
    return render_template(a, title=b, max=20, set=zip(v, lab, col))



app.run(debug = True, port = 5000)
