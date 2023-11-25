import pytest

import iec62056.objects
import iec62056.parser
import iec62056.samples

samples = iec62056.samples.Samples()

@pytest.fixture
def parser():
    return iec62056.parser.Parser()


@pytest.mark.parametrize('sample_name', list(samples))
def test_sample_parses_succesfully(parser, sample_name):
    data = samples[sample_name]
    telegram = parser.parse(data.decode('ascii'))
    for k in telegram.keys():
        obj = telegram[k]
        assert isinstance(obj, iec62056.objects.COSEM)
        if isinstance(obj, iec62056.objects.Register):
            assert isinstance(obj.name, str)
            assert obj.value is not None
