git clone https://github.com/pedrohilan/Library.git </br>
cd Library </br>
mkdir static </br>
virtualenv -p python3 venv  ||  python -m venv venv </br>
source /venv/bin/activate  ||  venv/Scripts/Activate </br>
pip install -r requirements.txt </br>
python manage.py migrate </br>
python manage.py runserver </br>
