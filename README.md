# End-to-End-CI-CD-Pipeline
This repo is created to get a hands on experience building a very simple end to end pipeline right from creating APIs using FastAPI, testing using PyTests, containerizing using Docker and automating app deployment using GitHub Actions.


To run the code locally, run the following lines of code in the terminal:
``` bash
python -m venv venv  # create a virtual environment (venv)
source venv/bin/activate # activate the venv

pip install -r requirements.txt  # install all the required libraries from requirements.txt file
uvicorn app.main:app --reload # start the uvicorn server

```

Now open a new tab in your browser and enter: http://127.0.0.1:8000

If all the tests pass, you should be able to see:
``` markdown
## CI/CD Demo App
If tests pass, this page gets deployed 🚀
```
