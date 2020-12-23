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
    <rasterrenderer opacity="1" alphaBand="-1" classificationMax="inf" type="singlebandpseudocolor" band="1" classificationMin="17">
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
        <colorrampshader clip="0" colorRampType="DISCRETE" classificationMode="3">
          <colorramp name="[source]" type="gradient">
            <prop k="color1" v="8,48,107,255"/>
            <prop k="color2" v="247,251,255,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.1;8,81,156,255:0.22;33,113,181,255:0.35;66,146,198,255:0.48;107,174,214,255:0.61;158,202,225,255:0.74;198,219,239,255:0.87;222,235,247,255"/>
          </colorramp>
          <item value="17" alpha="255" label="&lt;= 17" color="#08306b"/>
          <item value="35" alpha="255" label="17 - 35" color="#2879b9"/>
          <item value="57" alpha="255" label="35 - 57" color="#73b3d8"/>
          <item value="70" alpha="255" label="57 - 70" color="#c8ddf0"/>
          <item value="inf" alpha="255" label="> 70" color="#f7fbff"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation saturation="0" colorizeOn="0" colorizeBlue="128" colorizeStrength="100" colorizeGreen="128" grayscaleMode="0" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
