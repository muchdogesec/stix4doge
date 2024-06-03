import uuid
import stix2
import os
import shutil


from uuid import UUID

from stix4doge.phone_number import Phonenumber
# create the directories

tmp_directories = [
    "tmp_object_store",
]

for directory in tmp_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# define UUID for generating UUIDv5s

namespace=UUID("1abb62b9-e513-5f55-8e73-8f6d7b55c237")

# Create PhoneNumber SCO

example_PhoneNumberSCO = Phonenumber(
                    id="phone-number--"+ str(uuid.uuid5(namespace, f"07890129093")),
                    number="4407890129093",
                    country="GBR",
                    connection="Mobile",
                    provider="Big Network"
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_PhoneNumberSCO
}

for directory, phone_number_sco in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([phone_number_sco])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/phone-number/phone-number--" + str(uuid.uuid5(namespace, f"07890129093")) + ".json", "objects/custom-object-examples/phone-number--" + str(uuid.uuid5(namespace, f"07890129093")) + ".json")

shutil.rmtree("tmp_object_store")