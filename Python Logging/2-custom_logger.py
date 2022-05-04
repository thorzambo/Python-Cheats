from cgitb import handler
import logging

logger = logging.getLogger(__name__)

handler = logging.FileHandler('test.log')
formatter = logging.Formatter("[ %(asctime)s ] - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("test custom logger")
