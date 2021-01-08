from decouple import config
from google.cloud import storage
import os
import json

from src.build_graph import BuildGraph
from src.dao import GremlinSession


class TDT:
    def __init__(self):
        self.bucket_name = config('BUCKET_NAME')
        self.folder_name = config('FOLDER_NAME')
        self.destination_folder = config('DESTINATION_FOLDER')
        self._create_directory()
        self.gs = GremlinSession()

    def _create_directory(self):
        import pathlib
        pathlib.Path(self.destination_folder).mkdir(parents=True, exist_ok=True)

    def download_files(self):
        storage_client = storage.Client.create_anonymous_client()
        bucket = storage_client.bucket(self.bucket_name)
        blobs = bucket.list_blobs(prefix=self.folder_name)
        for blob in blobs:
            if blob.name.endswith(".json"):
                file_name = blob.name.replace("/", "_")
                blob.download_to_filename(self.destination_folder + "/" + file_name)

    def read_file(self):
        files = os.listdir(f"./{self.destination_folder}")
        for f in files:
            with open(f"{self.destination_folder}/" + f) as fp:
                data = json.load(fp)
                bg = BuildGraph(data)
                bg.construct_graph()
                self.gs.insert_vertices(bg.get_vertex())
                self.gs.insert_edges(bg.get_edges())

    def load_json(self):
        self.download_files()
        self.read_file()

