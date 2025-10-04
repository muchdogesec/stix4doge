import uuid
import hashlib
import stix2
import os
import json

from stix2 import Bundle, Identity
from stix2.base import STIXJSONEncoder
from uuid import UUID

# Define UUID for generating UUIDv5s
namespace = UUID("1abb62b9-e513-5f55-8e73-8f6d7b55c237")

# Define values that are recycled between objects
created_by_ref = "identity--" + str(uuid.uuid5(namespace, f"dogesec"))
created = "2020-01-01T00:00:00.000Z"
modified = "2020-01-01T00:00:00.000Z"
identity_class = "system"
contact_information = "https://www.dogesec.com/contact/"
sectors = ["technology"]

# Marking references
object_marking_refs = [
    "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",  # TLP:CLEAR
    "marking-definition--" + str(uuid.uuid5(namespace, f"stix4doge"))  # stix4doge
]

github_link = "https://github.com/muchdogesec/"

# Create Identity SDOs
identities = []

identity_names = [
    "arango_cti_processor", 
    "sigma2stix", "dogesec", "stix2arango", "txt2stix",
    "yara2stix", "location2stix", "creditcard2stix",
    "feeds2stix", "stixify", "obstracts", "siemrules",
    "arango_cve_processor", "txt2detection", "ransomware2stix"
]

# Ensure the output directory for individual identity objects exists
identity_output_dir = "objects/identity"
if not os.path.exists(identity_output_dir):
    os.makedirs(identity_output_dir)

for identity_name in sorted(identity_names):  # Sorting the identity names to ensure order
    # Special case for dogesec: no created_by_ref and custom description
    if identity_name == "dogesec":
        identity_sdo = Identity(
            id="identity--" + str(uuid.uuid5(namespace, identity_name)),
            created=created,
            modified=modified,
            name=identity_name,
            description=github_link,  # Custom description for dogesec
            contact_information=contact_information,
            identity_class="organization",
            confidence=100,
            sectors=sectors,
            object_marking_refs=object_marking_refs,
        )
    else:
        identity_sdo = Identity(
            id="identity--" + str(uuid.uuid5(namespace, identity_name)),
            created_by_ref=created_by_ref,
            created=created,
            modified=modified,
            name=identity_name,
            description=github_link + identity_name,
            contact_information=contact_information,
            identity_class=identity_class,
            confidence=100,
            sectors=sectors,
            object_marking_refs=object_marking_refs,
        )
    
    identities.append(identity_sdo)
    
    # Save each identity as a pretty-printed JSON file in the objects/identity directory
    identity_file_path = os.path.join(identity_output_dir, f"{identity_name}.json")
    with open(identity_file_path, "w") as identity_file:
        json.dump(identity_sdo, identity_file, cls=STIXJSONEncoder, indent=4)

# Create the bundle directory if it doesn't exist
bundle_output_dir = "objects/bundles"
if not os.path.exists(bundle_output_dir):
    os.makedirs(bundle_output_dir)

# Sort the objects in the bundle by their IDs to ensure consistent order
identities = sorted(identities, key=lambda x: x['id'])

# Create a STIX bundle without a timestamp or dynamic metadata
bundle = {"type": "bundle", "objects": identities}

# Serialize the objects of the bundle to JSON string (excluding the bundle metadata like created timestamps)
bundle_objects_json_str = json.dumps(bundle['objects'], cls=STIXJSONEncoder, sort_keys=True)

# Generate the MD5 hash of the serialized bundle objects
md5_hash = hashlib.md5(bundle_objects_json_str.encode('utf-8')).hexdigest()

# Generate UUIDv5 based on the MD5 hash and the namespace
bundle_id = "bundle--" + str(uuid.uuid5(namespace, md5_hash))

# Create the final STIX bundle with the calculated ID
final_bundle = Bundle(id=bundle_id, objects=identities, allow_custom=True)

# Bundle file path
bundle_file_path = os.path.join(bundle_output_dir, "identities-bundle.json")

# Save the final bundle with the new ID, pretty-printed
with open(bundle_file_path, "w") as bundle_file_with_id:
    json.dump(final_bundle, bundle_file_with_id, cls=STIXJSONEncoder, indent=4)

print(f"STIX bundle with ID saved to {bundle_file_path}")
