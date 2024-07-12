from ExternalCatalog import ExternalCatalog

class ExternalCatalogAdapter(ExternalCatalog):
    def __init__(self, external_catalog: ExternalCatalog):
        super().__init__()
        self.external_catalog = external_catalog

    