sudo apt install python3 -y
sudo apt install python3-pip -y
pip install pipenv
pipenv install
nohup pipenv run uvicorn main:app --host 0.0.0.0 --port 3934 &
