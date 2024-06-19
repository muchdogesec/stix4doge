import uuid
import stix2
import os
import shutil


from uuid import UUID
from stix4doge.bank_card import BankCard
# create the directories

tmp_directories = [
    "tmp_object_store",
]

for directory in tmp_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# define UUID for generating UUIDv5s

namespace=UUID("1abb62b9-e513-5f55-8e73-8f6d7b55c237")

# Create bank-card SCO

example_bankCardSCO = BankCard(
                    id="bank-card--"+ str(uuid.uuid5(namespace, f"4242424242424242")), # bank-card--9ce64b19-095d-5187-a56b-79a82ae4066f
                    format="credit",
                    number="4242424242424242",
                    scheme="VISA",
                    issuer_name="Big Bank",
                    issuer_country="GBR",
                    holder_name="DOGESEC",
                    valid_from="01/99",
                    valid_to="01/00",
                    security_code="999",
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_bankCardSCO
}

for directory, bankcard_sco in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([bankcard_sco])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/bank-card/bank-card--" + str(uuid.uuid5(namespace, f"4242424242424242")) + ".json", "objects/custom-object-examples/bank-card--" + str(uuid.uuid5(namespace, f"4242424242424242")) + ".json")

shutil.rmtree("tmp_object_store")