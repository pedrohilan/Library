git clone https://github.com/pedrohilan/Library.git </br>
cd Library </br>
mkdir static </br>
virtualenv -p python3 venv  ||  python -m venv venv </br>
source /venv/bin/activate  ||  venv/Scripts/Activate </br>
pip install -r requirements.txt </br>
python manage.py migrate </br>
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())" </br>
<b>"create file named .env and write 'SECRET_KEY=<--result of above code-->'"</b> </br>
python manage.py runserver </br>