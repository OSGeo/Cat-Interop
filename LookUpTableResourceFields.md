# Fields for Metadata Property Lookup Resource #

This document describes the fields included in a csv file maintained in GitHub by a community of metadata users and sofware developers wishing to implement functioning software based on links provided in Metadata or other web documents.

The idea is to provide guidance on current practice and recommendations for the exact strings to be used in various information elements in JSON, XML, RDF etc. so that software developers know what strings to look for when parsing the documents and metadata or other content providers know what to put in the content elements in structured documents.

Note: this is a draft document, field names are proposed and open for discussion. Let's not get too tangled up in the wordsmithing; the field name should convey the intention of the field to most readers...

## Fields ##

**StringValue**: (*MANDATORY*, exactly 1, not nilable) The exact string that is used to populate a content element in a structured document. This is the preferred or recommended value that SHOULD be used in instance documents.

**Label**: (*MANDATORY*, exactly 1) free text label for what the value represents; this will be used to search/lookup values.

**Alias**: (optional, 0..*) Abbreviated or alternate version of the value that is known to be in use. May include multiple values, delimited by a '|' (pipe) character.

**RegisteredURI**: (optional, 0..*) an authoritative registered identifier for the same value (same meaning or intention). May include multiple values, delimited by a '|' (pipe) character.

**OnlineInformation**: (*MANDATORY*, 1..*, nilable) a URL that will get an HTML document provide information about the meaning and usage of the value. If no resource is available, use the value nil:missing. May include multiple values, delimited by a '|' (pipe) character.

**TargetField**: (optional, 0..*) scoped name of content elements for which the value is applicable. Names maybe scoped using well known namespace abbreviations, but recommended practice is to provide a binding between namespace abbreviations used here and namespace URIs in the Comment field. May include multiple values, delimited by a '|' (pipe) character.

**Owner**: (*MANDATORY*, exactly one, not nilable) Name of organization or person who is the steward for the value or originally defined the value.

**ResourceType**: (optional, 0..*) a term to categorize the kind of resource identified by the value. [we need an accompanying table to provide resource type definitions...]. May include multiple values, delimited by a '|' (pipe) character.

**Registrant**: (*MANDATORY*, exactly one, nilable) Name of person who added the value to this lookup table resource.

**Comment**: (optional, 0..1) Free text additional information.

###Usage###
[to do--we need to populate a seed table, coming soooooon...]

##Stewardship of this Lookup table##
Table will be maintained as CSV file in GitHUB/OsGeo/cat-interop repository.  

Discussion should be placed in the Issue Tracker for this repository.

All updates should be made through pull requests to help track changes and document provenance. Suggested updates or additions should include some rational in the comment with the pull request.

Pull requests will be processed by the repository owner. Requests should be held for at least a week to allow comment. Interested parties should comment on pull requests if there are issues. Silence is considered tacit approval.