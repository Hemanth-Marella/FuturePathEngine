
import json
from pathlib import Path
from typing import Any,Dict,List


class JsonLoaderService:

    def __init__(self,data_directory = "BussinessLogic/JsonFiles"):

        self.data_directory = Path(data_directory)

    async def load_json(self, category: str, filename: str) -> Dict[str, Any]:
        """
        Load a single JSON file.

        Example:
            load_json("groups", "mpc")
            load_json("courses", "btech")
        """

        file_path = self.data_directory / category / f"{filename}.json"

        if not file_path.exists():
            raise FileNotFoundError(
                f"JSON file not found: {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def list_json_files(self, category: str) -> List[str]:
        """
        Return all JSON file names inside a category.

        Example:
            list_json_files("groups")
        """

        folder = self.data_directory / category

        if not folder.exists():
            return []

        return [
            file.stem
            for file in folder.glob("*.json")
        ]

    def category_exists(self, category: str) -> bool:
        """
        Check whether a category exists.
        """

        return (self.data_directory / category).exists()

    def file_exists(self, category: str, filename: str) -> bool:
        """
        Check whether a JSON file exists.
        """

        return (
            self.data_directory /
            category /
            f"{filename}.json"
        ).exists()