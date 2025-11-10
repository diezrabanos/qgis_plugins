================================================================================
GUÍA: CÓMO AÑADIR CAPTURAS DE PANTALLA A LA GUÍA DE USUARIO
Plugin: Silvilidar v1.0
================================================================================

📋 ARCHIVOS INCLUIDOS
================================================================================

1. ✓ Guia_Usuario_Silvilidar.html
   - Guía de usuario completa con placeholders para 15 capturas
   - Estructura lista para integrar las imágenes
   - Estilos CSS incluidos para visualización correcta

2. ✓ SCREENSHOTS_REQUERIDAS.txt
   - Lista completa de todas las capturas necesarias
   - Descripción detallada de cada una
   - Instrucciones de obtención

3. ✓ EDITOR_CAPTURAS.html
   - Página web auxiliar para gestionar capturas
   - Tabla resumen de todas las imágenes
   - Instrucciones paso a paso

4. ✓ reemplazar_capturas.py
   - Script Python para automatizar el reemplazo
   - Verifica archivos y realiza reemplazos automáticos
   - Crea copia de seguridad

================================================================================
⚡ INICIO RÁPIDO (5 PASOS)
================================================================================

PASO 1: Crear carpeta de capturas
   → Crea una carpeta llamada "screenshots" en el mismo directorio
     que Guia_Usuario_Silvilidar.html

PASO 2: Capturar las 15 imágenes
   → Sigue la lista en SCREENSHOTS_REQUERIDAS.txt
   → Captura cada ventana/diálogo del plugin
   → Guarda como PNG en la carpeta screenshots/
   → Usa nombres exactos: 01_ventana_principal.png, etc.

PASO 3: Opción A - Reemplazo automático (Recomendado)
   → Abre terminal/cmd en la carpeta del plugin
   → Ejecuta: python reemplazar_capturas.py
   → El script reemplazará todos los placeholders automáticamente

PASO 3: Opción B - Reemplazo manual
   → Abre Guia_Usuario_Silvilidar.html con un editor de texto
   → Busca todos los placeholders: (Reemplazar con: screenshots/XX_*.png)
   → Reemplaza cada uno manualmente con: <img src="screenshots/XX_*.png">
   → Guarda los cambios

PASO 4: Verificar en navegador
   → Abre Guia_Usuario_Silvilidar.html en tu navegador
   → Verifica que todas las imágenes se visualizan
   → Comprueba que los estilos se ven correctamente

PASO 5: ¡Listo!
   → La guía está lista para usar
   → Comparte la carpeta completa (con subcarpeta screenshots/)

================================================================================
📸 LISTA DE LAS 15 CAPTURAS NECESARIAS
================================================================================

INTERFAZ Y DIÁLOGOS (5 imágenes):
  01_ventana_principal.png          - Ventana principal del plugin
  02_dialogo_parametros.png         - Diálogo de Parámetros
  02b_dialogo_proyectar.png         - Diálogo de Proyectar
  02c_dialogo_salida.png            - Diálogo de Salida
  02d_dialogo_similares.png         - Diálogo de Búsqueda Similares

PROCESO Y ENTRADA (2 imágenes):
  03_qgis_capa_vectorial.png        - QGIS con capa vectorial cargada
  04_procesamiento_en_curso.png     - Ventana de progreso

RESULTADOS (8 imágenes):
  05_resultado_hm.png               - Raster HM visualizado
  05b_resultado_fcc.png             - Raster FCC visualizado
  05c_resultado_hbc.png             - Raster HBC visualizado
  05d_resultado_rc.png              - Raster RC visualizado
  06_teselas_clasificadas.png       - Teselas clasificadas
  07_zonas_similares.png            - Zonas similares encontradas
  08_histograma_similitud.png       - Gráfico de histogramas
  09_carpeta_salida.png             - Estructura de carpeta de salida

================================================================================
📹 CÓMO CAPTURAR CADA IMAGEN
================================================================================

Opción 1: Snipping Tool (Windows)
   1. Presiona Win+Shift+S
   2. Selecciona el área a capturar
   3. Se copia automáticamente al portapapeles
   4. Abre Paint o un editor de imágenes
   5. Pega (Ctrl+V) y guarda como PNG

Opción 2: Print Screen
   1. Abre la ventana que deseas capturar
   2. Presiona Print Screen
   3. Abre Paint (o Paint.NET, GIMP)
   4. Pega (Ctrl+V)
   5. Recorta si es necesario
   6. Guarda como PNG

Opción 3: Herramientas en línea
   1. Usa ShareX (software gratuito)
   2. Usa Greenshot (herramienta especializada)
   3. Usa Screenshot.guru o similares

================================================================================
✏️ EDITAR LAS IMÁGENES (Opcional)
================================================================================

Puedes mejorar las capturas:

Con Paint.NET (Gratuito):
   - Abre la imagen
   - Recorta bordes innecesarios
   - Ajusta brillo/contraste si es necesario
   - Guarda como PNG

Con GIMP (Gratuito, más potente):
   - Abre la imagen
   - File → Export As → PNG
   - Comprime si es necesario

================================================================================
🔄 USANDO EL SCRIPT DE REEMPLAZO (RECOMENDADO)
================================================================================

Requisitos: Python 3.6+

Pasos:
  1. Guarda todas las 15 imágenes en carpeta screenshots/
  2. Abre terminal/cmd en la carpeta del plugin
  3. Ejecuta: python reemplazar_capturas.py
  4. El script mostrará el progreso:
     ✓ Imagen encontrada
     ✗ Imagen faltante
     ⚠ Placeholder no encontrado
  5. Si hay errores, corrígelos y ejecuta de nuevo
  6. Se crea copia de seguridad del HTML automáticamente

Ejemplo de ejecución:
  $ python reemplazar_capturas.py
  ======================================================================
  🔄 Reemplazando placeholders de capturas...
  ======================================================================
  ✓ Reemplazado: screenshots/01_ventana_principal.png
  ✓ Reemplazado: screenshots/02_dialogo_parametros.png
  ...
  ======================================================================
  ✓ 15 placeholder(s) reemplazado(s)
  📁 Archivo guardado: Guia_Usuario_Silvilidar.html
  📁 Copia de seguridad: Guia_Usuario_Silvilidar.html.backup
  ======================================================================

================================================================================
📐 RECOMENDACIONES DE TAMAÑO Y FORMATO
================================================================================

Formato: PNG (mejor calidad) o JPG (más pequeño)

Dimensiones recomendadas:
  - Interfaz completa: 1000x700 px
  - Diálogos: 600x500 px
  - Mapas/Resultados: 1000x700 px

Tamaño de archivo:
  - Máximo: 500 KB por imagen
  - Óptimo: 100-300 KB
  - Para comprimir: TinyPNG.com, ImageOptim

Calidad:
  - DPI mínimo: 72
  - Texto legible: mínimo 100 px
  - Colores: RGB (no CMYK)

================================================================================
🐛 SOLUCIÓN DE PROBLEMAS
================================================================================

Problema: Las imágenes no aparecen en el navegador
Solución: Verifica que:
  ✓ La carpeta screenshots/ esté en el mismo directorio que HTML
  ✓ Los nombres de archivo sean exactos (mayúsculas/minúsculas)
  ✓ Las imágenes sean PNG válidas
  ✓ La ruta sea: src="screenshots/nombre.png"

Problema: El script Python no funciona
Solución: Verifica que:
  ✓ Tengas Python 3.6+ instalado
  ✓ Ejecutes desde la carpeta correcta
  ✓ Las imágenes existan en carpeta screenshots/
  Comando para verificar: python --version

Problema: Las imágenes se ven pequeñas o distorsionadas
Solución:
  ✓ Edita el CSS en Guia_Usuario_Silvilidar.html
  ✓ Busca: .screenshot img { max-width: 100%; height: auto; }
  ✓ Ajusta max-width según necesites

================================================================================
💡 MEJORAS OPCIONALES
================================================================================

1. Agregar números de figura
   - Modifica figcaption para incluir números automáticos
   - Ejemplo: "Figura 1: Ventana principal..."

2. Crear galería de imágenes
   - Usa JavaScript para lightbox (fancybox, etc.)
   - Permite ampliar imágenes al hacer clic

3. Responsive: Mejora para móviles
   - Ya está incluido en CSS media queries
   - Prueba en diferentes resoluciones

4. Versión PDF
   - Usa Print to PDF desde navegador
   - O herramientas como wkhtmltopdf

5. Traducción automática
   - Copia HTML y traduce con servicios online
   - Mantén estructura igual

================================================================================
📞 CONTACTO Y SOPORTE
================================================================================

Si tienes problemas o sugerencias:

1. Verifica SCREENSHOTS_REQUERIDAS.txt - tiene detalles de cada captura
2. Revisa EDITOR_CAPTURAS.html - tiene instrucciones visuales
3. Consulta el script reemplazar_capturas.py - tiene comentarios útiles
4. Lee este archivo README nuevamente - puede tener la respuesta

================================================================================
✅ CHECKLIST FINAL
================================================================================

Antes de distribuir la guía:

□ Creé carpeta screenshots/ en el directorio correcto
□ Capturé las 15 imágenes correctamente
□ Guardé todas como PNG con nombres exactos
□ Ejecuté el script reemplazar_capturas.py sin errores
□ O realicé los reemplazos manuales correctamente
□ Abrí Guia_Usuario_Silvilidar.html en navegador
□ Verifiqué que todas las imágenes aparecen
□ Comprobé que los estilos se ven correctamente
□ Verifiqué en móvil (tamaños responsive)
□ Guardé una copia de seguridad

================================================================================
📝 NOTAS FINALES
================================================================================

- La guía HTML es completamente funcional sin las imágenes
  (muestra placeholders si faltan)
- Es mejor tener capturas completas que no tener nada
- Puedes agregar imágenes gradualmente
- El script Python es reutilizable para actualizaciones futuras
- Mantén la estructura de carpetas intacta

================================================================================
¡Gracias por usar Silvilidar! 🎉
================================================================================

