#  api-service

Данное приложение включает в себя REST API сервис, реализующий операции CRUD над сущностью USER. 

При инициализации приложения из конфиг-файла считываются настройки репозитория - использование  PostreSQL или Redis в качестве базы данных. Конфиденциальные данные хранятся в файле .env. 

Сам сервис реализован на фреймворке FastAPI и структурирован согласно ООП.
