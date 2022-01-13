from pleiades_amphitheaters.amphitheaters_data import AmphitheaterData
from pleiades_amphitheaters.pleiades_data import PleiadesData
from pprint import pprint
from gzip import decompress
from json import loads
from requests import get

class CompareAmphitheatersData:
    def get_intersection(self):
        #=====Amphitheaters Data=====
        parser = AmphitheaterData()
        d = parser.read_data()
        #print(type(d))
        features = d['features']
        amphitheaters_uri = []
        for f in range(0, len(features)):
            amphitheaters_uri.append(features[f]['properties']['pleiades'])
        #print(amphitheaters_uri)
        
        #=====Pleiades Data=====
        pleiades_url = "http://atlantides.org/downloads/pleiades/json/pleiades-places-latest.json.gz"
        pleiades_data = loads(decompress(get(pleiades_url).content))
        pleiades_graph = pleiades_data['@graph']
        pleiades_uri = []
        for g in range(0,len(pleiades_graph)):
            pleiades_uri.append(pleiades_graph[g]['uri'])
        #print(pleiades_uri)

        #=====Finding the match======
        match = set(amphitheaters_uri) & set(pleiades_uri)
        # print("The length of amphitheaters_uri is " + str(len(amphitheaters_uri))) #267
        # print("The length of pleiades_uri is " + str(len(pleiades_uri)))
        # print(len(match)) #257
        match_list = list(match)
        return match_list

extract = CompareAmphitheatersData()
final_list = extract.get_intersection()
print(final_list)







