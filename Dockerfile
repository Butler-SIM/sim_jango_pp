FROM python:3.9.0

RUN echo "[### [Butler-sim] ###]"

RUN mkdir /root/.ssh/

ADD ./.ssh/id_rsa /root/.ssh/id_rsa

RUN echo "12-23 update"

RUN chmod 600 /root/.ssh/id_rsa

RUN touch /root/.ssh/knwon_hosts

RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

WORKDIR /home/

RUN git clone git@github.com:Butler-SIM/sim_jango_pp.git

WORKDIR /home/sim_jango_pp/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install mysqlclient

#RUN python3 manage.py migrate

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=server_settings.settings.deploy && python manage.py migrate --settings=server_settings.settings.deploy && gunicorn server_settings.wsgi --env DJANGO_SETTINGS_MODULE=server_settings.settings.deploy --bind 0.0.0.0:8000"]
#gunicorn app.wsgi:application --bind 0.0.0.0:8000 --reload && daphne -b 0.0.0.0 -p 8089 app.asgi:application

#new organization main branch dockerfile
