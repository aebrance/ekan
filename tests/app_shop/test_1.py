import pytest
import random

# # los metodos también deben comenzar con test_, aunque no es obligatorio
# def test_a():
#     assert 1 == 1


# # @pytest.mark.marca_1
# def test_b():
#     assert 1 == 1


# permite realizar acciones previas a los test
@pytest.fixture  # este decorador permite definir un fixture
def fixture_1(scope="session"):  # con scope="sesion" sólo se ejecuta una vez por sesion
    print("Se está ejecutando el fixture #1 antes del test")
    yield random.randint(0, 3)
    print("Se está ejecutando el fixture #1 después del test")


@pytest.mark.marca_1
def test_c(fixture_1):
    y = fixture_1
    x = 2
    print(f"Valor a comparar desde fixture_1: {y}")
    assert y != 0


@pytest.mark.marca_1
def test_d(fixture_1):
    y = fixture_1
    x = 2
    print(f"Valor a comparar desde D: {y}")
    assert y == 0
