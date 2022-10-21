pip install pipenv
pipenv install
pipenv shell
nohup uvicorn main:app --host 0.0.0.0 --port 3934 &