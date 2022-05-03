import logging

#configuration
logging.basicConfig(level=logging.DEBUG, filename = "log.log", filemode = "w",
                    format="[ %(asctime)s ] - %(levelname)s - %(message)s")


x = 2

logging.info(f"the value of x is {x}")

try:
      1/0
except Exception as e:
      logging.error("ZeroDivisionError", exc_info=True)
      pass #for continue

try:
      1/0
except Exception as e:
      logging.exception("ZeroTest")
      
      


# logging.debug("debug")

# logging.info("info")

# logging.warning("warning")

# logging.error("error")

# logging.critical("critical")
