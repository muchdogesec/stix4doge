import uuid
import hashlib
import stix2
import os
import json

from stix2 import Bundle, MarkingDefinition
from stix2.base import STIXJSONEncoder
from uuid import UUID

# Define UUID for generating UUIDv5s
namespace = UUID("1abb62b9-e513-5f55-8e73-8f6d7b55c237")

# Define values that are recycled between objects
created_by_ref = "identity--" + str(uuid.uuid5(namespace, f"dogesec"))
created = "2020-01-01T00:00:00.000Z"
definition_type = "statement"

# Marking references
object_marking_refs = [
    "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",  # TLP:CLEAR
    "marking-definition--" + str(uuid.uuid5(namespace, f"stix4doge"))  # stix4doge
]

github_link = "https://github.com/muchdogesec/"

# Create Marking Definition SMOs
marking_definitions = []

marking_names = [
    "yara2stix", "arango_cti_processor", "cve2stix", "cpe2stix", "stix2arango",
    "sigma2stix", "disarm2stix", "stix4doge", "cwe2stix", "txt2stix",
    "location2stix", "creditcard2stix", "stix2extensions", "feeds2stix",
    "siemrules", "arango_cve_processor", "txt2detection", "ransomware2stix",
    "organization2stix", "sector2stix"
]

# Ensure the output directory for individual marking definitions exists
marking_output_dir = "objects/marking-definition"
if not os.path.exists(marking_output_dir):
    os.makedirs(marking_output_dir)

for marking_name in sorted(marking_names):  # Sorting the marking names to ensure order
    # Special case for dogesec: no created_by_ref and custom statement
    if marking_name == "dogesec":
        marking_smo = MarkingDefinition(
            id="marking-definition--" + str(uuid.uuid5(namespace, marking_name)),
            created=created,
            definition_type=definition_type,
            definition={
                "statement": github_link  # Just the base URL for dogesec
            },
            object_marking_refs=object_marking_refs
        )
    else:
        marking_smo = MarkingDefinition(
            id="marking-definition--" + str(uuid.uuid5(namespace, marking_name)),
            created_by_ref=created_by_ref,
            created=created,
            definition_type=definition_type,
            definition={
                "statement": f"This object was created using: {github_link}{marking_name}"
            },
            object_marking_refs=object_marking_refs
        )
    
    marking_definitions.append(marking_smo)
    
    # Save each marking definition as a pretty-printed JSON file in the objects/marking-definition directory
    marking_file_path = os.path.join(marking_output_dir, f"{marking_name}.json")
    with open(marking_file_path, "w") as marking_file:
        json.dump(marking_smo, marking_file, cls=STIXJSONEncoder, indent=4)

# Create the bundle directory if it doesn't exist
bundle_output_dir = "objects/bundles"
if not os.path.exists(bundle_output_dir):
    os.makedirs(bundle_output_dir)

# Sort the objects in the bundle by their IDs to ensure consistent order
marking_definitions = sorted(marking_definitions, key=lambda x: x['id'])

# Create a STIX bundle without a timestamp or dynamic metadata
bundle = {"type": "bundle", "objects": marking_definitions}

# Serialize the objects of the bundle to JSON string (excluding the bundle metadata like created timestamps)
bundle_objects_json_str = json.dumps(bundle['objects'], cls=STIXJSONEncoder, sort_keys=True)

# Generate the MD5 hash of the serialized bundle objects
md5_hash = hashlib.md5(bundle_objects_json_str.encode('utf-8')).hexdigest()

# Generate UUIDv5 based on the MD5 hash and the namespace
bundle_id = "bundle--" + str(uuid.uuid5(namespace, md5_hash))

# Create the final STIX bundle with the calculated ID
final_bundle = Bundle(id=bundle_id, objects=marking_definitions, allow_custom=True)

# Bundle file path
bundle_file_path = os.path.join(bundle_output_dir, "marking-definitions-bundle.json")

# Save the final bundle with the new ID, pretty-printed
with open(bundle_file_path, "w") as bundle_file_with_id:
    json.dump(final_bundle, bundle_file_with_id, cls=STIXJSONEncoder, indent=4)

print(f"Marking Definitions STIX bundle with ID saved to {bundle_file_path}")
