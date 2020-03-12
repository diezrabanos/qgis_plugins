<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" version="3.10.2-A Coruña" minScale="1e+08" hasScaleBasedVisibilityFlag="0" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property key="WMSBackgroundLayer" value="false"/>
    <property key="WMSPublishDataSourceUrl" value="false"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <rasterrenderer classificationMax="20" band="1" type="singlebandpseudocolor" opacity="1" alphaBand="-1" classificationMin="3">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader classificationMode="1" clip="0" colorRampType="DISCRETE">
          <colorramp name="[source]" type="gradient">
            <prop k="color1" v="244,225,205,255"/>
            <prop k="color2" v="66,41,7,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.195913;209,189,166,255:0.460337;162,141,114,255:0.790865;103,80,48,255"/>
          </colorramp>
          <item alpha="255" label="&lt;= 3" color="#f4e1cd" value="3"/>
          <item alpha="255" label="3 - 8" color="#c0ab93" value="8"/>
          <item alpha="255" label="8 - 12" color="#968064" value="12"/>
          <item alpha="255" label="12 - 16" color="#6c5536" value="16"/>
          <item alpha="255" label=">20" color="#422907" value="20"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation saturation="0" colorizeGreen="128" colorizeStrength="100" colorizeOn="0" colorizeBlue="128" colorizeRed="255" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
