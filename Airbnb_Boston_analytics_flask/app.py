from flask import Flask,render_template
from mapboxgl.utils import df_to_geojson
import pandas as pd
#import settings

app = Flask(__name__)
#app.config.from_pyfile(settings)
#app.config.from_envvar('APP_CONFIG_FILE', silent=True)


MAPBOX_ACCESS_KEY = 'pk.eyJ1IjoiYWthc2hrYXRha2FtIiwiYSI6ImNqdWFhdm1vdjAwc2E0ZXBybWVoYnpudXIifQ.Hg7eCb28MfSE83llnpRlhg'

@app.route('/')
def hello_world():
    listings = pd.read_csv('data/sentiment_data.csv',parse_dates=True)
    listings.head(10)

    data = df_to_geojson(listings, properties=[ 'listing_id', 'name', 'neighbourhood_cleansed','compound','pos', 'neg','color'], lat='latitude',
                         lon='longitude', precision=10)

    return render_template('index.html', ACCESS_KEY=MAPBOX_ACCESS_KEY, feature_data=data)


if __name__ == '__main__':
    app.run()
