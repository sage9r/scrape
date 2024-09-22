echo " BUILD START"
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip3 install -r requirements.txt
python3 manage.py migrate 
python3 manage.py collectstatic
echo "from django.contrib.auth.models import User; User.objects.create_superuser('sager', 'sagarkafle39@gmail.com', 'time1234!')" | python3 manage.py shell
echo " BUILD END"