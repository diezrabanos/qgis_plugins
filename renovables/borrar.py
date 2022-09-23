from borrar2 import mivariable
print(mivariable)
myfile=open (r"C:\Users\dierabfr\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\renovables\archivoconcapas.txt")
myline = myfile.readline()
while myline:
    exec(myline)
    myline = myfile.readline()#para pasar a la siguiente 
print(parcelas)

texto='mivariable=589'
exec(texto)
print(mivariable)


