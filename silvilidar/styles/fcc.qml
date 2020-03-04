<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" hasScaleBasedVisibilityFlag="0" version="3.10.2-A Coruña" maxScale="1000" styleCategories="AllStyleCategories">
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
    <rasterrenderer opacity="1" alphaBand="-1" classificationMax="100" type="singlebandpseudocolor" band="1" classificationMin="0">
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
        <colorrampshader clip="0" colorRampType="DISCRETE" classificationMode="2">
          <colorramp name="[source]" type="gradient">
            <prop k="color1" v="241,238,246,255"/>
            <prop k="color2" v="152,0,67,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.25;215,181,216,255:0.5;223,101,176,255:0.75;221,28,119,255"/>
          </colorramp>
          <item value="20" alpha="255" label="&lt;= 20" color="#f1eef6"/>
          <item value="40" alpha="255" label="20 - 40" color="#d7b5d8"/>
          <item value="60" alpha="255" label="40 - 60" color="#df65b0"/>
          <item value="80" alpha="255" label="60 - 80" color="#dd1c77"/>
          <item value="inf" alpha="255" label="> 80" color="#980043"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation saturation="0" colorizeOn="0" colorizeBlue="128" colorizeStrength="100" colorizeGreen="128" grayscaleMode="0" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
