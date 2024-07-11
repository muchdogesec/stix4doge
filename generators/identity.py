import uuid
import stix2
import os
import shutil
import json

from stix2 import Bundle
from stix2.base import STIXJSONEncoder
from stix2 import Identity
from stix2 import FileSystemStore
from uuid import UUID

# define UUID for generating UUIDv5s

namespace=UUID("1abb62b9-e513-5f55-8e73-8f6d7b55c237")

# define values that are recycled between objects

### dogesec identity

created_by_ref="identity--" + str(uuid.uuid5(namespace, f"dogesec")) # this creates identity--9779a2db-f98c-5f4b-8d08-8ee04e02dbb5
created="2020-01-01T00:00:00.000Z"
modified="2020-01-01T00:00:00.000Z"
identity_class="system"
contact_information="https://www.dogesec.com/contact/"
sectors=[
	"technology"
]

### mitre TLP:CLEAR and stix4doge

object_marking_refs=[
    "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487", # this is TLP:CLEAR
    "marking-definition--" + str(uuid.uuid5(namespace, f"stix4doge")) # marking-definition--97ba4e8b-04f6-57e8-8f6e-3a0f0a7dc0fb
]

github_link="https://github.com/muchdogsec/"

# Create Identity SDOs
## https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.sdo.html

### arango_cti_processor

arango_cti_processor_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"arango_cti_processor")), #identity--2e51a631-99d8-52a5-95a6-8314d3f4fbf3
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="arango_cti_processor",
                        description=github_link+"arango_cti_processor",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### cve2stix

cve2stix_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"cve2stix")), # identity--562918ee-d5da-5579-b6a1-fae50cc6bad3
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="cve2stix",
                        description=github_link+"cve2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### stix2arango

stix2arango_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"stix2arango")), # identity--72e906ce-ca1b-5d73-adcd-9ea9eb66a1b4
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="stix2arango",
                        description=github_link+"stix2arango",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### sigma2stix

sigma2stix_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"sigma2stix")), # identity--860f4c0f-8c26-5889-b39d-ce94368bc416
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="sigma2stix",
                        description=github_link+"sigma2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### disarm2stix

disarm2stix_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"disarm2stix")), # identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="disarm2stix",
                        description=github_link+"disarm2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### dogesec

dogesec_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"dogesec")), # identity--9779a2db-f98c-5f4b-8d08-8ee04e02dbb5
                        created=created,
                        modified=modified,
                        name="dogesec",
                        description=github_link,
                        contact_information= contact_information,
                        identity_class="organization",
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### cwe2stix

cwe2stix_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"cwe2stix")), # identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="cwe2stix",
                        description=github_link+"cwe2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### txt2stix

txt2stix_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"txt2stix")), # identity--f92e15d9-6afc-5ae2-bb3e-85a1fd83a3b5
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="txt2stix",
                        description=github_link+"txt2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### yara2stix

yara2stix_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"yara2stix")), #identity--2c741473-e0f1-5f0a-a044-ae2a368ad0c6
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="yara2stix",
                        description=github_link+"yara2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### location2stix

location2stix_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"location2stix")), #identity--674a16c1-8b43-5c3e-8692-b3d8935e4903
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="location2stix",
                        description=github_link+"location2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### ransomwhere2stix

ransomwhere2stix_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"ransomwhere2stix")), # identity--904ac99b-7539-5de7-9ffa-23186f0e07b6
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="ransomwhere2stix",
                        description=github_link+"ransomwhere2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### creditcard2stix

creditcard2stix_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"creditcard2stix")), # identity--d287a5a4-facc-5254-9563-9e92e3e729ac
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="creditcard2stix",
                        description=github_link+"creditcard2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

### feeds2stix

feeds2stix_IdentitySDO = Identity(
                        id="identity--" + str(uuid.uuid5(namespace, f"feeds2stix")), # identity--a1cb37d2-3bd3-5b23-8526-47a22694b7e0
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="feeds2stix",
                        description=github_link+"feeds2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
                        object_marking_refs=object_marking_refs
                    )

from utils import Generator
generator = Generator("objects/identity")
generator.add_item("arango_cti_processor", arango_cti_processor_IdentitySDO)
generator.add_item("cve2stix", cve2stix_IdentitySDO)
generator.add_item("cwe2stix", cwe2stix_IdentitySDO)
generator.add_item("disarm2stix", disarm2stix_IdentitySDO)
generator.add_item("sigma2stix", sigma2stix_IdentitySDO)
generator.add_item("dogesec", dogesec_IdentitySDO)
generator.add_item("stix2arango", stix2arango_IdentitySDO)
generator.add_item("txt2stix", txt2stix_IdentitySDO)
generator.add_item("yara2stix", yara2stix_IdentitySDO)
generator.add_item("location2stix", location2stix_IdentitySDO)
generator.add_item("ransomwhere2stix", ransomwhere2stix_IdentitySDO)
generator.add_item("creditcard2stix", creditcard2stix_IdentitySDO)
generator.add_item("feeds2stix", feeds2stix_IdentitySDO)
generator.save_all()

print("Done.")