git clone https://github.com/pedrohilan/Library.git
cd library
mkdir static
virtualenv -p python3 venv
source /venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver