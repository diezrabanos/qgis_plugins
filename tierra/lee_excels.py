import xlrd
ruta=r"C:\Users\dierabfr\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\tierra\prueba.xls"
libroentrada=xlrd.open_workbook(ruta)
hojaentrada=libroentrada.sheet_by_index(0)

print(hojaentrada.nrows)
print(hojaentrada.ncols)

print(hojaentrada.cell_value(1,0))

columna1=[]
columna2=[]
fila1=[]
for x in range(1,hojaentrada.ncols):
    fila1.append(hojaentrada.cell_value(0,x))

for y in range(1,hojaentrada.nrows):
    columna1.append(hojaentrada.cell_value(y,0))
    columna2.append(libroentrada.cell_value(y,1))

print(columna1)
print(columna2)
