import os
import shutil
import uuid
from uuid import UUID

import stix2
from stix4doge.bank_account import BankAccount

# create the directories

tmp_directories = [
    "tmp_object_store",
]

for directory in tmp_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# define UUID for generating UUIDv5s

namespace=UUID("1abb62b9-e513-5f55-8e73-8f6d7b55c237")

# Create bank account SCO

example_bankAccountSCO = BankAccount(
                    id="bank-account--"+ str(uuid.uuid5(namespace, f"GB33BUKB20201555555555")), # bank-account--fb76b7b8-8701-5d8b-a143-0283847f6638
                    bank="Big Bank",
                    country="GBR",
                    currency="GBP",
                    holder_name="DOGESEC",
                    iban_number="GB33BUKB20201555555555",
                    swift_code="DEMOGB22XXX",
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_bankAccountSCO
}

for directory, bankaccount_sco in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([bankaccount_sco])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/bank-account/bank-account--" + str(uuid.uuid5(namespace, f"GB33BUKB20201555555555")) + ".json", "objects/custom-object-examples/bank-account--" + str(uuid.uuid5(namespace, f"GB33BUKB20201555555555")) + ".json")

shutil.rmtree("tmp_object_store")
