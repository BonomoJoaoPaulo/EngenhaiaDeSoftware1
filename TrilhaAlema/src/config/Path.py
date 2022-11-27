import os

class Path:
    src_path = os.path.join(os.getcwd(), "TrilhaAlema", "src")

    @staticmethod
    def relative_to_assets(path: str) -> str:
        return os.path.join(Path.src_path, "Assets", path)
    