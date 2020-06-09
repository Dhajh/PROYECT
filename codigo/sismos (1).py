import pandas
import folium

sismos = pandas.read_csv('SSNMX_catalogo_20190601_20200608.csv')
mexico = folium.Map(location=[23.000, -102.000], zoom_start = 4)


for r in sismos[0:30046].iterrows():
      m = r[1]['Magnitud']
      f = r[1]['Fecha']
      if (m > 4.5):col = 'red'
      if (m > 3.5 and m < 4.5):col = 'orange'
      if (m < 3.5):col = 'green'
      info = "Mag:" + str(m) + " Fecha:" + f
      folium.Marker((r[1]['Latitud'],r[1]['Longitud']), popup = info,icon =folium.Icon( col,icon='info-sign')).add_to(mexico)


mexico.save('map.html')
