# blinkstick-test
test app for python blinkstick api

  * checkout the blinkstick api to this directory (you should end up with a subdirectory called blinkstick-python)
    * git clone https://github.com/elfman03/blinkstick-python.git
    * This is a version of the python library modified to work with python 3
  * attach device
  * run python bs.py
  
  NOTE:  I have seen my device stop working and misdetect.  Usually this is while querying the color.  The test app attempts to create a safe way to set and query color which so far seems to kick the blinkstick back into a working state
