update:
	 git pull https://github.com/EfremovEgor/icits.ru.git
	 python3 src/manage.py collectstatic --no-input 
	 python3 src/manage.py migrate 
	 sudo systemctl restart gunicorn