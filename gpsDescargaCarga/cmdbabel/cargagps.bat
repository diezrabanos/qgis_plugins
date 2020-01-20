set parametro=%1
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -w -i gpx -f %parametro% -o garmin -F usb:
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -t -i gpx -f %parametro% -o garmin -F usb:
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -w -i gpx -f %parametro% -o garmin -F COM1
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -t -i gpx -f %parametro% -o garmin -F COM1
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -w -i gpx -f %parametro% -o garmin -F COM2
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -t -i gpx -f %parametro% -o garmin -F COM2
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -w -i gpx -f %parametro% -o garmin -F COM3
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -t -i gpx -f %parametro% -o garmin -F COM3
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -w -i gpx -f %parametro% -o garmin -F COM4
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -t -i gpx -f %parametro% -o garmin -F COM4
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -w -i gpx -f %parametro% -o garmin -F COM5
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -t -i gpx -f %parametro% -o garmin -F COM5
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -w -i gpx -f %parametro% -o garmin -F COM6
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -t -i gpx -f %parametro% -o garmin -F COM6
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -w -i gpx -f %parametro% -o garmin -F COM7
"C:/Program Files/QGIS 3.10/bin/gpsbabel.exe" -t -i gpx -f %parametro% -o garmin -F COM7
