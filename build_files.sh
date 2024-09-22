echo " BUILD START"
python3 -m venv env
sudo apt install nginx
sudo cp nginx.conf /etc/nginx/conf.d/
sudo systemctl restart nginx
source env/bin/activate
pip install --upgrade pip
pip3 install -r requirements.txt
python3 manage.py migrate 
python3 manage.py collectstatic
echo "from django.contrib.auth.models import User; User.objects.create_superuser('sager', 'sagarkafle39@gmail.com', 'time1234!')" | python3 manage.py shell
gunicorn scrape.wsgi:application --bind 0.0.0.0:8000 
echo " BUILD END"