update:
	 git pull https://github.com/EfremovEgor/icits.ru.git
	 python3 icSubmissionWebsite/manage.py collectstatic --no-input 
	 sudo systemctl restart gunicorn