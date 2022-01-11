#Pleiades JSON serialization for an individual Pleiades place resource

from pleiades_amphitheaters.data import DataFetcher

class PleiadesData(DataFetcher):

    def read_data(
        self,
        uri: str
    ):
        return DataFetcher.read_data(self, uri=uri)
