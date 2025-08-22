import logging
from src.jobsources.analysis.manager import Manager


def test_manager_instantiation():
    logger = logging.getLogger(__name__)
    manager = Manager(logger=logger)
    assert manager is not None
