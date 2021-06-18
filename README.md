# miac
# Настройка БД:
1. Установите postgressql и создайте пользователя, пароль пользователя, базу данных пользователя, базу данных для проекта:
`sudo apt update`
`sudo apt install postgresql postgresql-contrib`
`sudo -u postgres psql`
`CREATE USER postgres WITH PASSWORD 'postgres';`
`ALTER ROLE postgres WITH LOGIN;`
`CREATE DATABASE monitoring_system OWNER postgres;`
`GRANT ALL PRIVILEGES ON DATABASE monitoring_system TO postgres;`

