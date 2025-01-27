import json
import sys

from pathlib import Path


class ManifestEditor:
    def __init__(self):
        self.manifest_dict = json.load(open(Path('../target/manifest.json')))

    @staticmethod
    def filter_large_raw_sql(node, max_lines=500):
        raw_sql = node.get('raw_sql')
        if raw_sql.count('\n') > max_lines:
            node['raw_sql'] = ''.join(raw_sql.split('\n')[0:max_lines])
        else:
            pass
        return node

    def slim_manifest(self):

        new_nodes = {name: self.filter_large_raw_sql(node) for name, node in self.manifest_dict["nodes"].items()}
        self.manifest_dict["nodes"] = new_nodes

    def write_new_manifest(self):
        f = open('../target/manifest.json', 'w')
        f.write(json.dumps(self.manifest_dict))
        f.close()


    def main(self):
        self.slim_manifest()
        self.write_new_manifest()

editor = ManifestEditor()
editor.main()
