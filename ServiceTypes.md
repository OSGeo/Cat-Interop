There is an [OGC URN policy document](http://www.opengeospatial.org/ogcUrnPolicy) which recommends that
the "serviceType" have the following node designations:
```
    "urn:ogc:serviceType" ":" name ":" version ":" [binding] [":" profile]
```
In the Geoportal Server metadata editor, the following are used:
```
urn:x-esri:specification:ServiceType:ArcIMS
urn:x-esri:specification:ServiceType:ArcGIS
urn:ogc:dataFormat:GML:2.0
urn:ogc:dataFormat:GML:2.1.1
urn:ogc:dataFormat:GML:2.1.2
urn:ogc:dataFormat:GML:3.0
urn:ogc:dataFormat:GML:3.1.1
urn:ogc:serviceType:CatalogueService:2.0.1:CORBA
urn:ogc:serviceType:CatalogueService:2.0.1:HTTP
urn:ogc:serviceType:CatalogueService:2.0.1:HTTP:ebRIM
urn:ogc:serviceType:CatalogueService:2.0.1:HTTP:EO
urn:ogc:serviceType:CatalogueService:2.0.1:HTTP:FGDC-CSDGM
urn:ogc:serviceType:CatalogueService:2.0.1:HTTP:ISO19115/19119
urn:ogc:serviceType:CatalogueService:2.0.1:Z39.50
urn:ogc:serviceType:CatalogueService:2.0.1:Z39.50:GEOProfile
urn:ogc:serviceType:CatalogueService:2.0.1:Z39.50:SRU
urn:ogc:serviceType:CatalogueService:2.0.2:CORBA
urn:ogc:serviceType:CatalogueService:2.0.2:HTTP
urn:ogc:serviceType:CatalogueService:2.0.2:HTTP:ebRIM
urn:ogc:serviceType:CatalogueService:2.0.2:HTTP:EO
urn:ogc:serviceType:CatalogueService:2.0.2:HTTP:FGDC-CSDGM
urn:ogc:serviceType:CatalogueService:2.0.2:HTTP:ISO19115/19119
urn:ogc:serviceType:CatalogueService:2.0.2:Z39.50
urn:ogc:serviceType:CoordinateTransformationService:1.0
urn:ogc:serviceType:CoordinateTransformationService:1.0:COM
urn:ogc:serviceType:CoordinateTransformationService:1.0:CORBA
urn:ogc:serviceType:CoordinateTransformationService:1.0:Java
urn:ogc:serviceType:GridCoverage:1.0:COM
urn:ogc:serviceType:GridCoverage:1.0:CORBA
urn:ogc:serviceType:OpenLSCoreServices:1.0
urn:ogc:serviceType:OpenLSCoreServices:1.0:SOAP
urn:ogc:serviceType:OpenLSCoreServices:1.1
urn:ogc:serviceType:KML:2.2
urn:ogc:serviceType:SimpleFeatureAccess:1.0:CORBA
urn:ogc:serviceType:SimpleFeatureAccess:1.1:OLE/COM
urn:ogc:serviceType:SimpleFeatureAccess:1.1:SQL
urn:ogc:serviceType:SimpleFeatureAccess:1.2:SQL
urn:ogc:serviceType:SensorObservationService:1.0
urn:ogc:serviceType:WebCoverageService:1.0
urn:ogc:serviceType:WebCoverageService:1.1.0
urn:ogc:serviceType:WebFeatureService:1.0
urn:ogc:serviceType:WebFeatureService:1.1
urn:ogc:serviceType:WebMapService:1.0
urn:ogc:serviceType:WebMapService:1.1
urn:ogc:serviceType:WebMapService:1.1.1
urn:ogc:serviceType:WebMapService:1.3.0
urn:ogc:serviceType:WebMapService:Post:0.0.3
urn:ogc:serviceType:WebProcessingService:0.4
```
I like this structure, and would like to propse a few more that would be managed by Unidata:
```
urn:unidata:serviceType:OPeNDAP:2.0.0
urn:unidata:serviceType:NetcdfSubsetService:1.0.0
urn:unidata:serviceType:CdmRemote:0.1.0
```

Perhaps there is a better way to build this list, but just wanted to get this down here...
