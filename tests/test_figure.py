from src.figure import Figure
import pytest

def test_create_figure():
    assert Figure()

def test_figure_attrs():
    figure = Figure()
    assert figure.name == "Figure"
    assert figure.area == None
    assert figure.perimeter == None

def test_figure_add_area():
    figure1 = Figure()
    figure2 = Figure()
    assert figure1.add_area(figure2)

def test_square_add_area_with_errors():
    with pytest.raises(Exception):
        figure1 = Figure()
        figure1.add_area(1)