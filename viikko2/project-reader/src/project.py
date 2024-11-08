class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors_str = '\n'.join([f"- {author}" for author in self.authors]) if self.authors else '-'
        dependencies_str = '\n'.join([f"- {dep}" for dep in self.dependencies]) if self.dependencies else '-'
        dev_dependencies_str = '\n'.join([f"- {dep}" for dep in self.dev_dependencies]) if self.dev_dependencies else '-'

        # Return the formatted string
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\nAuthors:\n{authors_str}"
            f"\nDependencies:\n{dependencies_str}"
            f"\nDevelopment dependencies:\n{dev_dependencies_str}"
        )
