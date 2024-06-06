from abc import ABC, abstractmethod
from typing import Dict

class IDecodable(ABC):
    @staticmethod
    @abstractmethod
    def decode_from_json(json_data: Dict) -> 'IDecodable':
        """
        Create an instance of the class from a JSON-serializable dictionary.
        """
        pass

    @abstractmethod
    def encode_to_json(self) -> Dict:
        """
        Convert the instance to a JSON-serializable dictionary.
        """
        pass