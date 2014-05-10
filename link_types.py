import logging

LOGGER = logging.getLogger(__name__)


def inurl(needles, haystack, position='any'):
    """convenience function to make string.find return bool"""

    count = 0

    # lowercase everything to do case-insensitive search
    haystack2 = haystack.lower()

    for needle in needles:
        needle2 = needle.lower()
        if position == 'any':
            if haystack2.find(needle2) > -1:
                count += 1
        elif position == 'end':
            if haystack2.endswith(needle2):
                count += 1
        elif position == 'begin':
            if haystack2.startswith(needle2):
                count += 1

    # assessment
    if count > 0:
        return True
    return False


def sniff_link(url):
    """performs basic heuristics to detect what the URL is"""

    protocol = None
    link = url.strip()

    # heuristics begin
    if inurl(['service=CSW', 'request=GetRecords'], link):
        protocol = 'OGC:CSW'
    elif inurl(['service=SOS', 'request=GetObservation'], link):
        protocol = 'OGC:SOS'
    elif inurl(['service=WCS', 'request=GetCoverage'], link):
        protocol = 'OGC:WCS'
    elif inurl(['service=WFS', 'request=GetFeature'], link):
        protocol = 'OGC:WFS'
    elif inurl(['service=WMS', 'request=GetMap'], link):
        protocol = 'OGC:WMS'
    elif inurl(['service=WPS', 'request=Execute'], link):
        protocol = 'OGC:WPS'
    elif inurl(['arcims'], link):
        protocol = 'ESRI:ArcIMS'
    elif inurl(['arcgis'], link):
        protocol = 'ESRI:ArcGIS'
    elif inurl(['mpk'], link, 'end'):
        protocol = 'ESRI:MPK'
    elif inurl(['opendap'], link):
        protocol = 'OPeNDAP:OPeNDAP'
    elif inurl(['ncss'], link):
        protocol = 'UNIDATA:NCSS'
    elif inurl(['cdmremote'], link):
        protocol = 'UNIDATA:CDM'
    elif inurl(['gml'], link, 'end'):
        protocol = 'OGC:GML'
    elif inurl(['html', 'shtml', 'htm'], link, 'end'):
        protocol = 'WWW:LINK'
    # extra tests
    elif all([inurl(['census.gov/geo/tiger'], link),
              inurl(['zip'], link, 'end')]):
        protocol = 'ESRI:SHAPEFILE'
    elif inurl(['zip', 'tar.gz', 'tgz', 'gz', 'bz2'], link, 'end'):
        protocol = 'WWW:DOWNLOAD'
    else:
        LOGGER.info('No link type detected')

    return protocol
