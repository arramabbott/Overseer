import pygeoip
import os
class PyKMLWriter(object):
    """description of class"""
    def __init__(self):
        pass

    def write(self, ip_set):
        gi = pygeoip.GeoIP('<Location_of_GeoLiteCity.bat_file\\GeoLiteCity.dat')
        with open("<Location_you_want_kml_file_saved_to\\<Name_of_file>.kml",'w+') as kml_file:
            kml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n')
            for ip in ip_set:
                try:
                    record = gi.record_by_addr(ip)
                except:
                    record = None 
                if record is not None:
                    longitude = record['longitude']
                    latitude = record['latitude']
                    kml_file.write("<Placemark>\n<name>"+ip+"</name>\n<Point>\n<coordinates>\n")
                    kml_file.write(str(longitude)+","+str(latitude)+"\n")
                    kml_file.write("</coordinates>\n</Point>\n</Placemark>\n")
            kml_file.write("</Document>\n</kml>")
            kml_file.close()
            os.startfile(kml_file.name)

            

