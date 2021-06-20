# miac
# python back

«Мы представляем вашему вниманию систему дистанционного мониторинга уровня артериального давления и пульса - Кардио-Контроль». 
Наше Web приложение позволит клиентам дистанционно отправлять данные с тонометров, контролировать частоту измерений, и правильность лечения. Также мы  предоставляем удобный интерфейс для взаимодействия с лечащим врачом.

# Настройка



1. Установите postgressql и создайте пользователя, пароль пользователя, базу данных пользователя, базу данных для проекта:
`sudo apt update`
`sudo apt install postgresql postgresql-contrib`
`sudo -u postgres psql`
`CREATE USER postgres WITH PASSWORD 'postgres';`
`ALTER ROLE postgres WITH LOGIN;`
`CREATE DATABASE monitoring_system OWNER postgres;`
`GRANT ALL PRIVILEGES ON DATABASE monitoring_system TO postgres;`

2. Настройте виртуальное окружение
3. Установите зависимости
4. Установите миграции
