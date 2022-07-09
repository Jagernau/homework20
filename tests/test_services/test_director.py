from unittest.mock import MagicMock
import pytest


from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


#Фикстура

@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    #Искуственная бд
    tarkovsky = Director(id=1, name='tarkovsky')
    spilberg = Director(id=2, name='spilberg')
    tarantino = Director(id=3, name='tarantino')

    director_dao.get_one = MagicMock(return_value=tarkovsky)
    director_dao.get_all = MagicMock(return_value=[tarkovsky, spilberg, tarantino])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


