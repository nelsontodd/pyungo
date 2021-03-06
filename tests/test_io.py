from pyungo.io import Input, Output


def test_Input():
    inp = Input(name='a')
    assert inp.name == 'a'
    assert inp.value is None
    assert inp.is_arg is False
    assert inp.is_kwarg is False


def test_Input_arg():
    inp = Input.arg(name='a')
    assert inp.name == 'a'
    assert inp.value is None
    assert inp.is_arg is True
    assert inp.is_kwarg is False


def test_Input_kwarg():
    inp = Input.kwarg(name='a')
    assert inp.name == 'a'
    assert inp.value is None
    assert inp.is_arg is False
    assert inp.is_kwarg is True


def test_Input_constant():
    inp = Input.constant(name='a', value=2)
    assert inp.name == 'a'
    assert inp.value == 2
    assert inp.is_arg is False
    assert inp.is_kwarg is False
    assert inp.is_constant is True


def test_Output():
    out = Output('a')
    assert out.name == 'a'
    out.value = 2
    assert out._value == 2
    assert out.value == 2
