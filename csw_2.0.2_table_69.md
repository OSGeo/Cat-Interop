From OGC CSW_2.0.2:
##10.12.4.2 ResourceType parameter
The ResourceType parameter references a document that defines the structure of the
resource being harvested. For high interoperability, this resource should be an XML
document, and the ResourceType parameter string value should be a URI that references
the structure of that XML document (i.e., its XML Schema namespace identifier URI). If
a server can harvest resources in the schema of an information model it supports, the
ResourceType URI should be the same as the outputSchema parameter URI defined for
the GetRecords operation.

Table 69 defines a set of URIs that may be used to identify well know metadata formats.
CSW implementations and CSW application profiles may support other values of the
ResourceType parameter for harvesting additional artifact types. If creating new
ResourceType URNs is needed, the format of the values may be
`urn:ogc:def:resourceType:CSW:token`, where token is a placeholder for a value that
denotes the specific resource type.

Table 69 — URIs for well known metadata standards
URI Description
```
http://www.opengis.net/wms : WMS capability document, all current versions
http://www.opengis.net/wfs : WFS capability document, versions 1.0 and 1.1
http://www.opengis.net/wfs/1.2.0 : WFS capability document, version 1.2
http://www.opengis.net/wcs : WCS capability document, version 1.0
http://www.opengis.net/wcs/1.1 : WCS capability document, version 1.1
http://www.opengis.net/cat/csw : CSW capability document, versions 2.0.0 and 2.0.1
http://www.opengis.net/cat/csw/2.0.2 : CSW capability document, version 2.0.2
http://www.fgdc.gov/metadata/csdgm : Content Standard for Digital Geospatial Metadata (CSDGM), Vers. 2 (FGDC-STD-001-1998)
http://www.auslig.gov.au/dtd/anzmeta-1.3.dtd : Australian Spatial Data Infrastructure Standard
http://www.isotc211.org/schemas/2005/gmd/ : ISO19139 document
http://metadata.dod.mil/mdr/ns/DDMS/1.3/ : DEPARTMENT OF DEFENSE DISCOVERY
```
