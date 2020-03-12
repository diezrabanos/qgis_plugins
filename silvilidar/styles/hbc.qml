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
            <prop k="color1" v="252,246,252,255"/>
            <prop k="color2" v="112,15,109,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.203125;223,199,223,255:0.502404;182,130,180,255:0.774038;144,67,141,255"/>
          </colorramp>
          <item alpha="255" label="&lt;= 3" color="#fcf6fc" value="3"/>
          <item alpha="255" label="3 - 8" color="#d3b2d2" value="8"/>
          <item alpha="255" label="8 - 12" color="#b27bb0" value="12"/>
          <item alpha="255" label="12 - 16" color="#91458f" value="16"/>
          <item alpha="255" label=">20" color="#700f6d" value="20"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation saturation="0" colorizeGreen="128" colorizeStrength="100" colorizeOn="0" colorizeBlue="128" colorizeRed="255" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
