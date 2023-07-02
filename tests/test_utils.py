from src import utils


def test_encryption_account():
    assert utils.encryption('Счет 64686473678894779589') == 'Счет **9589'
    assert utils.encryption('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert utils.encryption('Visa Platinum 8990922113665229') == 'Visa Platinum 8990 92** **** 5229'


def test_if_executed():
    assert utils.if_executed([{"state": "EXECUTED", "date": "2018-12-20T16:43:26.929246"}], 0) == []
    assert utils.if_executed([{"state": "EXECUTED", "date": "2018-12-20T16:43:26.929246"}], 1) == [{'date': '2018-12-20T16:43:26.929246', 'state': 'EXECUTED'}]
    assert utils.if_executed([{"state": "CANCELED", "date": "2018-12-20T16:43:26.929246"}], 1) == []
    assert utils.if_executed([{"state": "EXECUTED", "date": "2018-12-20T16:43:26.929246"},
                              {"state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}], 2) == [{'date': '2018-12-20T16:43:26.929246', 'state': 'EXECUTED'}]
