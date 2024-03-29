
from dataclasses import dataclass

@dataclass
class Urls:
    """Urls for downloading the data from the Agreste website"""

    main :str = """https://agreste.agriculture.gouv.fr/agreste-web/download/service/SV-Acc%C3%A8s%20micro%20donn%C3%A9es%20RICA/RicaMicrodonn%C3%A9es2022.zip"""
    history:str="""https://agreste.agriculture.gouv.fr/agreste-web/download/service/SV-Acc%C3%A8s%20micro%20donn%C3%A9es%20RICA/RicaMicroDonn%C3%A9es2000-2005.zip"""
