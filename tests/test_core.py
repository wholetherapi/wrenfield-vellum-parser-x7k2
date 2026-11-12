from src.vellum_parser.core import Record, run


def test_run_deduplicates_records():
    records = [Record('b', {}), Record('a', {}), Record('a', {})]
    result = list(run(records))
    assert [item.key for item in result] == ['a', 'b']
