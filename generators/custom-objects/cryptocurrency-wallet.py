import uuid
import stix2
import os
import shutil


from uuid import UUID

from stix4doge.cryptocurrency_wallet import CryptocurrencyWallet
# create the directories

tmp_directories = [
    "tmp_object_store",
]

for directory in tmp_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# define UUID for generating UUIDv5s -- this is the OASIS namespace for SCOs https://github.com/oasis-open/cti-python-stix2/blob/master/stix2/base.py#L29

namespace=UUID("00abedb4-aa42-466c-9c01-fed23315a9b7")

# Create CryptocurrencyWallet SCO

example_CryptocurrencyWalletSCO = CryptocurrencyWallet(
                    id="cryptocurrency-wallet--"+ str(uuid.uuid5(namespace, f"1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY")),
                    address="1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY",
                    
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_CryptocurrencyWalletSCO
}

for directory, cryptocurrency_wallet_sco in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([cryptocurrency_wallet_sco])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/cryptocurrency-wallet/cryptocurrency-wallet--" + str(uuid.uuid5(namespace, f"1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY")) + ".json", "objects/custom-object-examples/cryptocurrency-wallet--" + str(uuid.uuid5(namespace, f"1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY")) + ".json")

shutil.rmtree("tmp_object_store")