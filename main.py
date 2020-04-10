import pandas as pd
from flask_cors import CORS
from flask import Flask, render_template, jsonify

data = pd.read_csv("CTData.csv",encoding= 'unicode_escape')

app = Flask(__name__)
CORS(app)

col = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500"]

temp_stand ={'Chill' : 4 ,
             'Frozen': -20,
             'Banana': 14,
             'DF'    : -30}

@app.route('/temp_timeseries_day/<string:freight>/<string:box>/<string:month>/<string:day>')
def temp_timeseries_day(freight,box,month,day):
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

@app.route('/temp_timeseries_month/<string:freight>/<string:box>/<string:month>')
def temp_timeseries_month(freight,box,month):
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

@app.route('/humidity_timeseries_month/<string:freight>/<string:box>/<string:month>')
def humidity_timeseries_month(freight,box,month):
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

@app.route('/overall_product_detail/<string:name>')
def overall_product_detail(name):
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

@app.route('/freight/<string:status>')
def freight(status):
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

@app.route('/total_products_by_freight/<string:name>')
def total_products_by_freight(name):
    temp1 = data[data['Freight'] == name]
    temp = temp1['Product_Type'].value_counts()
    df = pd.DataFrame({'labels': temp.index, 'values': temp.values})
    a = 'pie_chart.html'
    b = 'Total Product Types in ' + name
    v = df.values[:, 1]
    lab = df.values[:, 0]
    return render_template(a, title=b, max=20, set=zip(v, lab, col))


@app.route('/sample_rest_api')
def sample_data():
    contacts = [
        {
          "id": 1,
          "name": "Leanne Graham",
          "username": "Bret",
          "email": "Sincere@april.biz",
          "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
              "lat": "-37.3159",
              "lng": "81.1496"
            }
          },
          "phone": "1-770-736-8031 x56442",
          "website": "hildegard.org",
          "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
          }
        },
        {
          "id": 2,
          "name": "Ervin Howell",
          "username": "Antonette",
          "email": "Shanna@melissa.tv",
          "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {
              "lat": "-43.9509",
              "lng": "-34.4618"
            }
          },
          "phone": "010-692-6593 x09125",
          "website": "anastasia.net",
          "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains"
          }
        },
        {
          "id": 3,
          "name": "Clementine Bauch",
          "username": "Samantha",
          "email": "Nathan@yesenia.net",
          "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
            "geo": {
              "lat": "-68.6102",
              "lng": "-47.0653"
            }
          },
          "phone": "1-463-123-4447",
          "website": "ramiro.info",
          "company": {
            "name": "Romaguera-Jacobson",
            "catchPhrase": "Face to face bifurcated interface",
            "bs": "e-enable strategic applications"
          }
        }
    ]
    return jsonify({'contacts': contacts})



app.run()