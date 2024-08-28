import uuid
import stix2
import os
import shutil
import json

from stix2 import Bundle
from stix2.base import STIXJSONEncoder
from stix2 import MarkingDefinition
from stix2 import FileSystemStore
from uuid import UUID

namespace=UUID("1abb62b9-e513-5f55-8e73-8f6d7b55c237")

# define values that are recycled between objects

### dogesec

created_by_ref="identity--" + str(uuid.uuid5(namespace, f"dogesec")) # this creates identity--9779a2db-f98c-5f4b-8d08-8ee04e02dbb5
created="2020-01-01T00:00:00.000Z"
modified="2020-01-01T00:00:00.000Z"
definition_type="statement"

### mitre TLP:CLEAR and stix4doge

object_marking_refs=[
    "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487", # this is TLP:CLEAR
    "marking-definition--" + str(uuid.uuid5(namespace, f"stix4doge")) # marking-definition--97ba4e8b-04f6-57e8-8f6e-3a0f0a7dc0fb
]

# Create Marking Definition SMOs
## https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.common.html

### yara2stix

yara2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"yara2stix")), # marking-definition--2e51a631-99d8-52a5-95a6-8314d3f4fbf3
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/yara2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### arango_cti_processor

arango_cti_processor_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"arango_cti_processor")), # marking-definition--2e51a631-99d8-52a5-95a6-8314d3f4fbf3
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/arango_cti_processor"
                        },
                        object_marking_refs=object_marking_refs
                    )

### cve2stix

cve2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"cve2stix")), # marking-definition--562918ee-d5da-5579-b6a1-fae50cc6bad3
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/cve2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### cpe2stix

cpe2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"cpe2stix")), # marking-definition--5e6fc5ec-e507-52e7-8465-cf5ffc47138a
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/cpe2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### stix2arango

stix2arango_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"stix2arango")), # marking-definition--72e906ce-ca1b-5d73-adcd-9ea9eb66a1b4
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/stix2arango"
                        },
                        object_marking_refs=object_marking_refs
                    )

### sigma2stix

sigma2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"sigma2stix")), # marking-definition--860f4c0f-8c26-5889-b39d-ce94368bc416
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/sigma2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### disarm2stix

disarm2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"disarm2stix")), # marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/disarm2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### stix4doge

stix4doge_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"stix4doge")), # marking-definition--97ba4e8b-04f6-57e8-8f6e-3a0f0a7dc0fb
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/stix4doge"
                        },
                        object_marking_refs=object_marking_refs
                    )

### cwe2stix

cwe2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"cwe2stix")), # marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/cwe2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### txt2stix

txt2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"txt2stix")), # marking-definition--f92e15d9-6afc-5ae2-bb3e-85a1fd83a3b5
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/txt2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### location2stix

location2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"location2stix")), #marking-definition--674a16c1-8b43-5c3e-8692-b3d8935e4903
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/location2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### creditcard2stix

creditcard2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"creditcard2stix")), #marking-definition--d287a5a4-facc-5254-9563-9e92e3e729ac
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/creditcard2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### stix2extensions

stix2extensions_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"stix2extensions")), # marking-definition--60c0f466-511a-5419-9f7e-4814e696da40
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/stix2extensions"
                        },
                        object_marking_refs=object_marking_refs
                    )

### feed2stix

feeds2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"feeds2stix")), # marking-definition--a1cb37d2-3bd3-5b23-8526-47a22694b7e0
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/feeds2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### Ransomware Knowledgebase

ransomware_kb_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"ransomware_kb")), # marking-definition--221c1248-e62e-56e5-bbfb-7d5efc477271
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/muchdogesec/ransomware_kb"
                        },
                        object_marking_refs=object_marking_refs
                    )

from utils import Generator
generator = Generator("objects/marking-definition")
generator.add_item("cpe2stix", cpe2stix_MarkingDefinitionSMO)
generator.add_item("arango_cti_processor", arango_cti_processor_MarkingDefinitionSMO)
generator.add_item("cve2stix", cve2stix_MarkingDefinitionSMO)
generator.add_item("cwe2stix", cwe2stix_MarkingDefinitionSMO)
generator.add_item("disarm2stix", disarm2stix_MarkingDefinitionSMO)
generator.add_item("sigma2stix", sigma2stix_MarkingDefinitionSMO)
generator.add_item("stix2arango", stix2arango_MarkingDefinitionSMO)
generator.add_item("stix4doge", stix4doge_MarkingDefinitionSMO)
generator.add_item("txt2stix", txt2stix_MarkingDefinitionSMO)
generator.add_item("yara2stix", yara2stix_MarkingDefinitionSMO)
generator.add_item("location2stix", location2stix_MarkingDefinitionSMO)
generator.add_item("creditcard2stix", creditcard2stix_MarkingDefinitionSMO)
generator.add_item("stix2extensions", stix2extensions_MarkingDefinitionSMO)
generator.add_item("feeds2stix", feeds2stix_MarkingDefinitionSMO)
generator.add_item("ransomware_kb", ransomware_kb_MarkingDefinitionSMO)
generator.save_all()