import sys
import json
import logging
from jobsources.analysis.manager import Manager
import tempfile  # Import tempfile

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    if len(sys.argv) < 2:
        logger.error("Usage: uv run main.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    manager = Manager(logger=logger)
    mapping_object = manager.analyze_url(url, logger=logger)

    logger.info(json.dumps(mapping_object, indent=4))


if __name__ == "__main__":
    main()
