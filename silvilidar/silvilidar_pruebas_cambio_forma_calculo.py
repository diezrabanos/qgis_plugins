def calculo(expresion, capa):
    calc = QgsRasterCalculator(expresion,
                               os.path.join(carpeta, troncoresumido + '_' + capa + '.tif'),
                               'GTiff',
                               layerglobal.extent(),
                               layerglobal.width(),
                               layerglobal.height(),
                               entries)

    calc.processCalculation()
    del (calc)
calculo('(fccp@1 <= ' + str(fccbaja) + ') * 1 ', 'C1')

##formula de excel de alejandro
#if( "fccp@1" <=0 , 0 , if( "fccp@1" <10 , 1 , if( "hmp@1" <2 , 11 , if( "hmp@1" <3.5 , 2 , if( "hmp@1" <5 , if( "rcp@1"  <=40 , if( "fccp@1" >50 , 51 , 61) , 17) , if( "hmp@1" <=7.5 , if( "rcp@1"  <=50 , if( "fccp@1" >55 , 52 , 62) , if( "hmp@1" - "hmp@1" * "rcp@1"  /100<=3 , 3 , 4)) , if( "hmp@1" <=12 , if( "hmp@1" - "hmp@1" * "rcp@1"  /100<=5.5 , if( "rcp@1"  <=60 , if( "fccp@1" >57.5 , 77 , 7) , 7) , if( "rcp@1"  >=35 , if( "hmp@1" * "rcp@1"  /100>3.25 , if( "fccp@1" >57.5 , if( "fccp@1" >=(0.1167* "fccp@1" +3.6667)*( "hmp@1" ^1.04328809)*( "hmp@1" * "rcp@1"  /100)^(-0.49505946) , 81 , if( "fccp@1" >=95 , 81 , 10)) , 7) , 7) , if( "fccp@1" >=95 , 9 , if( "fccp@1" >57.5 , 77 , 10)))) , if( "hmp@1" <=16.5 , if( "hmp@1" - "hmp@1" * "rcp@1"  /100<=5.5 , 111 , if( "rcp@1"  >=35 , if( "hmp@1" * "rcp@1"  /100>3.25 , if( "fccp@1" >57.5 , if( "fccp@1" >=(0.1167* "fccp@1" +3.6667)*( "hmp@1" ^1.04328809)*( "hmp@1" * "rcp@1"  /100)^(-0.49505946) , 82 , if( "fccp@1" >=95 , 82 , 111)) , 111) , 111) , if( "fccp@1" >=95 , 121 , 141))) , if( "rcp@1"  <=17 , if( "fccp@1" >=95 , 13 , 15) , if( "rcp@1"  <35 , if( "fccp@1" >=95 , 122 , 142) , 112))))))))))
#if( fccp@1 <=0 , 0 , if( fccp@1 <10 , 1 , if( hmp@1 <2 , 11 , if( hmp@1 <3.5 , 2 , if( hmp@1 <5 , if( rcp@1  <=40 , if( fccp@1 >50 , 51 , 61) , 17) , if( hmp@1 <=7.5 , if( rcp@1  <=50 , if( fccp@1 >55 , 52 , 62) , if( hmp@1 - hmp@1 * rcp@1  /100<=3 , 3 , 4)) , if( hmp@1 <=12 , if( hmp@1 - hmp@1 * rcp@1  /100<=5.5 , if( rcp@1  <=60 , if( fccp@1 >57.5 , 77 , 7) , 7) , if( rcp@1  >=35 , if( hmp@1 * rcp@1  /100>3.25 , if( fccp@1 >57.5 , if( fccp@1 >=(0.1167* fccp@1 +3.6667)*( hmp@1 ^1.04328809)*( hmp@1 * rcp@1  /100)^(-0.49505946) , 81 , if( fccp@1 >=95 , 81 , 10)) , 7) , 7) , if( fccp@1 >=95 , 9 , if( fccp@1 >57.5 , 77 , 10)))) , if( hmp@1 <=16.5 , if( hmp@1 - hmp@1 * rcp@1  /100<=5.5 , 111 , if( rcp@1  >=35 , if( hmp@1 * rcp@1  /100>3.25 , if( fccp@1 >57.5 , if( fccp@1 >=(0.1167* fccp@1 +3.6667)*( hmp@1 ^1.04328809)*( hmp@1 * rcp@1  /100)^(-0.49505946) , 82 , if( fccp@1 >=95 , 82 , 111)) , 111) , 111) , if( fccp@1 >=95 , 121 , 141))) , if( rcp@1  <=17 , if( fccp@1 >=95 , 13 , 15) , if( rcp@1  <35 , if( fccp@1 >=95 , 122 , 142) , 112))))))))))