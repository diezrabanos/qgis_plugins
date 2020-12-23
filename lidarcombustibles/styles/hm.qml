<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" minScale="1e+08" version="3.10.2-A Coruña" maxScale="0" styleCategories="AllStyleCategories">
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
    <rasterrenderer opacity="1" classificationMin="3.5" band="1" type="singlebandpseudocolor" alphaBand="-1" classificationMax="inf">
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
          <colorramp name="[source]" type="cpt-city">
            <prop k="inverted" v="0"/>
            <prop k="rampType" v="cpt-city"/>
            <prop k="schemeName" v="cb/seq/BuGn_09"/>
            <prop k="variantName" v=""/>
          </colorramp>
          <item value="3.5" color="#dee4e0" alpha="255" label="&lt;= 3.5"/>
          <item value="5" color="#c2cfc6" alpha="255" label="3.5 - 5"/>
          <item value="7.5" color="#a6baad" alpha="255" label="5 - 7.5"/>
          <item value="12" color="#8aa593" alpha="255" label="7.5 - 12"/>
          <item value="16.5" color="#6f926e" alpha="255" label="12 - 16.5"/>
          <item value="20" color="#537b60" alpha="255" label="16.5 - 20"/>
          <item value="23" color="#376647" alpha="255" label="20 - 23"/>
          <item value="25" color="#1b512d" alpha="255" label="23 - 25"/>
          <item value="inf" color="#004614" alpha="255" label="> 25"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeStrength="100" colorizeOn="0" saturation="0" grayscaleMode="0" colorizeGreen="128" colorizeRed="255" colorizeBlue="128"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
