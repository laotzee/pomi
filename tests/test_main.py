import pytest
import src.main as pomi

get_seconds_input = [
    ('1h', 3600),
    ('3m', 180),
    ('60s', 60),
    ('5', 5),
    ('p', pomi.CURRENT_P[1]),
    ('b', pomi.CURRENT_P[0]),
    ('j4s', None),            # matches suffix but not the rest
    ('lkdfs##$sd234', None),  # has symbols
    ('sdff33', None),         # alphanumeric but not properly formatted
    ('', None),               # empty input
]

get_percentage_input = [
    (100, 100, 10),
    (100, 50, 5),
    (100, 25, 2),
    (100, 99, 9),
]
update_val_input = [
    (70, 's', 10),
    (360, 'm', 6),
    (3789, 'h', 1),
]

str_to_secons_input = [
    (1, '200', 200),
    (60, '5', 300),
    (3600, '2', 7200),
]


@pytest.mark.parametrize('user_input, expected_output', get_seconds_input)
def test_get_seconds(user_input, expected_output):

    pomi.get_seconds(user_input)

def test_update_val():
    pass

@pytest.mark.parametrize('total_time, current_time, expected_output', get_percentage_input)
def test_get_percentage(total_time, current_time, expected_output):

    pomi.get_percentage(total_time, current_time)

@pytest.mark.parametrize('t, suffix, expected_output', update_val_input)
def test_update_val(t, suffix, expected_output):

    pomi.update_val(t, suffix)

@pytest.mark.parametrize('multiplier, time, expected_output', str_to_secons_input)
def test_str_to_seconds(multiplier, time, expected_output):

    pomi.str_to_seconds(multiplier, time)