import ee
import sys
import json
import os
from google.oauth2 import service_account

def main(latitude, longitude):
    SCOPES = ['https://www.googleapis.com/auth/earthengine']

    #credentials_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
 
    credentials = service_account.Credentials.from_service_account_file(
     'privatekey.json', scopes=SCOPES)
   
    ee.Initialize(credentials)
    point = ee.Geometry.Point([longitude, latitude])

    landsatSR = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2") \
        .filterBounds(point) \
        .filterDate('2021-01-01', '2021-12-31') \
        .sort('CLOUD_COVER') \
        .first()

    if landsatSR:
        #landsat_info = landsatSR.getInfo()
        image_id = landsatSR.id().getInfo()
        cloud_cover = landsatSR.get('CLOUD_COVER').getInfo()
        date_time = landsatSR.date().format('YYYY-MM-dd HH:mm:ss').getInfo()
        satellite = landsatSR.get('SPACECRAFT_ID').getInfo()
        WRS_PATH = landsatSR.get('WRS_PATH').getInfo()
        WRS_ROW = landsatSR.get('WRS_ROW').getInfo()
        TARGET_WRS_PATH = landsatSR.get('TARGET_WRS_PATH').getInfo()
        TARGET_WRS_ROW = landsatSR.get('TARGET_WRS_ROW').getInfo()
        cloud_cover_land = landsatSR.get('CLOUD_COVER_LAND').getInfo()
        Image_quality = landsatSR.get('IMAGE_QUALITY_TIRS').getInfo()
        ST_BAND10 = landsatSR.get('TEMPERATURE_MAXIMUM_BAND_ST_B10').getInfo()
        
        metadata = {
            'image_id': image_id,
          # 'landsat_info': landsat_info,
            'latitude': latitude,
            'longitude': longitude,
            'cloud_cover': cloud_cover*100,
            'satellite': satellite,
            'date_time': date_time,
            'wrspath': WRS_PATH,
            'wrsrow': WRS_ROW,
            'target_wrspath': TARGET_WRS_PATH,
            'target_wrsrow': TARGET_WRS_ROW,
            'cloud_cover_land': cloud_cover_land*100,
             'Image_quality': Image_quality,
            # 'surface_temp_b10': ST_BAND10,
            # 'surface_temp_b11': surface_temp_b11
        }
        
        print(json.dumps(metadata, indent=4))
    else:
        print(json.dumps({'error': 'No Landsat Surface Reflectance image found for the given location and date.'}))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python earth_engine.py <latitude> <longitude>")
        sys.exit(1)

    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    main(latitude, longitude)