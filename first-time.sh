# Este script deve ser executado logo as máquinas estiverem prontas.
# Caso o docker no Windows esteja parando, tente reiniciar o serviço Lxssmanager.

echo "Criando as migrações."
python manage.py makemigrations

echo "Migrando..."
python manage.py migrate

echo "Criando o super usuário."
python manage.py createsuperuser --noinput

# gunicorn alurareceita.wsgi --bind 0.0.0.0:80