from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = toml.loads(content)
        dict_poetry = data['tool']['poetry']

        name = dict_poetry.get("name", "Unknown")
        description = dict_poetry.get("description", "No description")
        license = dict_poetry.get("license", "No license")
        authors = dict_poetry.get("authors", [])
        dependencies = dict_poetry.get("dependencies", [])
        dependencies_dev = dict_poetry.get("group", {}).get("dev", {}).get("dependencies", [])

        return Project(name, description, license, authors, dependencies, dependencies_dev)
