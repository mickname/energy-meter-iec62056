from collections.abc import Mapping, Iterator
import pathlib

SAMPLE_DIR = pathlib.Path(__file__).parent / pathlib.Path('sample_data')

class Samples(Mapping):
    """Load sample data bytes from various devices.
    """
    def __init__(self) -> None:
        self.sample_names: set[str] = set(sample.stem for sample in SAMPLE_DIR.glob('*.raw'))
        self.sample_data: dict[str, bytes] = {}

    def __getitem__(self, sample_name: str) -> bytes:
        try:
            return self.sample_data[sample_name]
        except KeyError:
            if sample_name not in self.sample_names:
                raise ValueError(f'Invalid sample name {sample_name}')

            with open(SAMPLE_DIR / pathlib.Path(sample_name).with_suffix('.raw'), 'rb') as f:
                data = f.read()

            self.sample_data[sample_name] = data
            return data

    def __iter__(self) -> Iterator[str]:
        for name in self.sample_names:
            yield name

    def __len__(self) -> int:
        return len(self.sample_names)
