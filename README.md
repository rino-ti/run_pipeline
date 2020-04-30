# run_pipeline
Python script, to execute another sub pipeline, while waiting for it to be finished.

# requirements:
- python3
  - import gitlab
  - import time, timeit
  - import sys
  

In the project I'm calling, I use variables, in this case, the parent project, which calls this script has to pass the variables, so, as an example I declared them with the same name that I will use external.
