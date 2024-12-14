# Buffer_analysis
# import arcpy
# import arcpy.mapping
# arcpy.env.workspace=r'C:\Python27\ArcGIS10.8\PythonProject1\Input'
# arcpy.env.overwriteOutput=True
# shape_data=arcpy.ListFeatureClasses()
# print (shape_data)
# point_data=r'C:\Python27\ArcGIS10.8\PythonProject1\Input\points.shp' # point_data=shape_data[4]
# buffer_distance="100 Meters"
# buffer_output=r"C:\Python27\ArcGIS10.8\PythonProject1\output\Point_Buffer.shp"
# arcpy.Buffer_analysis(point_data,buffer_output,buffer_distance,dissolve_option='All')
# print ("Buffer analysis Successful")
#
# pdf_output=r'C:\Python27\ArcGIS10.8\PythonProject1\Buffer output map\point_buffer_map.pdf'
#
# mxd_path= r'C:\Python27\ArcGIS10.8\PythonProject1\map\blank_map.mxd'
# mxd=arcpy.mapping.MapDocument(mxd_path)
# df=arcpy.mapping.ListDataFrames(mxd)[0]
# point_layar=arcpy.mapping.Layer(buffer_output)
# arcpy.mapping.AddLayer(df,point_layar,add_position="TOP")
# arcpy.mapping.ExportToPDF(mxd,pdf_output)


#Intersection
# import arcpy
# import arcpy.mapping
# arcpy.env.workspace=r'C:\Python27\ArcGIS10.8\PythonProject1\Input'
# arcpy.env.overwriteOutput=True
# shape_data=arcpy.ListFeatureClasses()
# print (shape_data)
# point_data=r'C:\Python27\ArcGIS10.8\PythonProject1\Input\buildings.shp' # point_data=shape_data[4]
# buffer_distance="1000 Meters"
# road=r"C:\Python27\ArcGIS10.8\PythonProject1\Input\roads.shp"
# buffer_output=r"C:\Python27\ArcGIS10.8\PythonProject1\output\Point_Buffer.shp"
# arcpy.Buffer_analysis(point_data,buffer_output,buffer_distance,dissolve_option='All')
# print ("Buffer analysis Successful")
#
# pdf_output=r'C:\Python27\ArcGIS10.8\PythonProject1\Buffer output map\road_buffer_map.pdf'
#
# mxd_path= r'C:\Python27\ArcGIS10.8\PythonProject1\map\blank_map.mxd'
# intersect_out=r"C:\Python27\ArcGIS10.8\PythonProject1\output\intersection.shp"
# arcpy.Intersect_analysis([buffer_output,road],intersect_out)
# print ("Intersection analysis Successful")
#
# mxd=arcpy.mapping.MapDocument(mxd_path)
#
# df=arcpy.mapping.ListDataFrames(mxd)[0]
# buffer_layar=arcpy.mapping.Layer(buffer_output)
# interaction_layar=arcpy.mapping.Layer(intersect_out)
#
# arcpy.mapping.AddLayer(df,buffer_layar,add_position="TOP")
# arcpy.mapping.AddLayer(df,interaction_layar,add_position='TOP')
# arcpy.mapping.ExportToPDF(mxd,pdf_output)
#
