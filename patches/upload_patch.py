import json
import os
from typing import Dict, Optional

from google.cloud import firestore

db = firestore.Client(
    project=os.getenv("GCP_PROJECT"),
)

PATCH_FILE = os.getenv("PATCH_FILE")


class PatchOptions(object):
    def __init__(self, options: Optional[Dict]):
        self.options = options if options is not None else {}

    @property
    def skip_if_id_present(self) -> Optional[bool]:
        return self.options.get("skip_if_id_present")


class PatchCountries(object):
    def __init__(self, options: PatchOptions, countries_patch_data):
        self.options = options
        self.countries_patch_data = countries_patch_data

    def patch(self):
        for p in self.countries_patch_data:
            doc_id = p.get("id")
            name = p.get("name")
            country_ref = db.collection("countries").document(doc_id)
            country_doc = country_ref.get()
            if country_doc.exists:
                if self.options.skip_if_id_present:
                    print(f"Skipping countries/{doc_id}")
                    continue
                country_ref.set({"name": name})
            else:
                print(f"Adding countries/{doc_id}")
                country_ref.set({"name": name})


def main():
    with open(PATCH_FILE, "r") as patch_file_raw:
        patch_data = json.load(patch_file_raw)
    if patch_data["published"]:
        print(f"File {PATCH_FILE} is already published.")
    patch_options = PatchOptions(patch_data.get("options"))
    patch_countries = PatchCountries(patch_options, patch_data.get("countries"))
    patch_countries.patch()


if __name__ == '__main__':
    main()
