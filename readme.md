# Проект автоматизации тестирования API для сервиса REQRES.IN

<img width="1087" alt="image" src="https://user-images.githubusercontent.com/109241600/205449027-eb2ebe81-593c-4fb7-b1c3-23468c3f5179.png">
<a href="https://reqres.in" target="_blank">REQRES.IN</a> - это сервис, который имитирует реальные сценарии использования REST API.

## Содержание
+ [Технологии и инструменты](#Технологии)
+ [Тест-кейсы](#Тесты)
+ [Запуск автотестов из Jenkins](#Jenkins) 
+ [Оповещение о результатах через Telegram-бот](#Telegram) 
+ [Отчеты о прохождении тестов Allure report](#Allure) 
+ [Интеграция с Allure TestOPS](#TestOPS) 
+ [Интеграция с Jira](#Jira) 



<a name="Технологии">

## Технологии и инструменты, использованные в проекте
<p align="center">
<img width="6%" title="PyCharm" src="reqres_tests/utils/images/pycharm.svg">
<img width="6%" title="Python" src="reqres_tests/utils/images/python.svg">
<img width="6%" title="Pytest" src="reqres_tests/utils/images/pytest.svg">
<img width="6%" title="Requests" src="reqres_tests/utils/images/requests.png">
<img width="6%" title="GitHub" src="reqres_tests/utils/images/GitHub.svg">
<img width="6%" title="Rest" src="reqres_tests/utils/images/rest-assured.svg">
<img width="6%" title="Jenkins" src="reqres_tests/utils/images/Jenkins.svg">  
<img width="6%" title="AllureReport" src="reqres_tests/utils/images/Allure_Report.svg">  
<img width="6%" title="AllureTestOPS" src="reqres_tests/utils/images/Allure_TO.svg"> 
<img width="6%" title="Telegram" src="reqres_tests/utils/images/Telegram.svg">  
<img width="6%" title="Jira" src="reqres_tests/utils/images/jira.svg"> 
</p>



<a name="Тесты">

## Тест-кейсы
###### Авторизация:
  - Успешная авторизация
  - Неуспешная авторизация (не указан пароль)
###### Действия с пользователем:
  - Добавление пользователя
  - Изменение данных пользователя
  - Удаление пользователя



<a name="Jenkins">

## Запуск автотестов из Jenkins
Для удаленного запуска автотестов в <a href="https://jenkins.autotests.cloud/view/мои%20задачи/job/002-annazukowska-python-reqres-api/" target="_blank">Jenkins</a> создана задача (job), настроена и связана с репозиторием в GitHub.

<img width="1165" alt="image" src="https://user-images.githubusercontent.com/109241600/205457963-63e67bb7-ea07-45b1-86ad-e46f76322bb8.png">



<a name="Telegram">

## Уведомление о результатах тестирования через Telegram-бот
После завершения тестов приходит такое оповещение в Telegram с помощью заранее созданного Telegram-бота, привязанного к задаче в Jenkins.

<img width="365" alt="image" src="https://user-images.githubusercontent.com/109241600/205478808-6766df9c-786a-4350-bf7d-a23b8af7e053.png">



<a name="Allure">

## Отчеты о прохождении тестов Allure report
После завершения тестов также формируются отчеты <a href="https://jenkins.autotests.cloud/view/мои%20задачи/job/002-annazukowska-python-reqres-api/26/allure/#behaviors/c2aab3ca885b96191db7369b6e011b58/88db428ef8b1f909/history" target="_blank">Allure report</a>, которые можно посмотреть со страницы задачи в Jenkins.

<img width="1384" alt="image" src="https://user-images.githubusercontent.com/109241600/206015670-7fdc5435-5c0f-47fb-a0d2-958a9a696529.png">
<img width="1433" alt="image" src="https://user-images.githubusercontent.com/109241600/205479511-776f70cc-4b7c-400c-a1a4-37c1243c9be8.png">



<a name="TestOPS">

## Интеграция с Allure TestOPS
Настроена интеграция Jenkins с Allure TestOPS.
При первом после интеграции прохождении тестов в Jenkins, в Allure TestOPS были автоматически созданы такие тест-кейсы:
<img width="1436" alt="image" src="https://user-images.githubusercontent.com/109241600/205479711-64b90846-bb3a-40fe-99bb-6a80c239544b.png">

Можно посмотреть историю выполненных прогонов:
<img width="1435" alt="image" src="https://user-images.githubusercontent.com/109241600/205479800-0a64d2b1-8392-486f-9ec5-2f082e61d889.png">
<img width="1435" alt="image" src="https://user-images.githubusercontent.com/109241600/205480162-37354093-dc73-42d7-9a8f-654c6baaef05.png">



<a name="Jira">

## Интеграция с Jira
Настроена интеграция Allure TestOPS с Jira. К задаче в Jira привязаны тест-кейсы и прогон с результатами тестирования из Allure TestOPS.

<img width="973" alt="image" src="https://user-images.githubusercontent.com/109241600/205480051-66eb900a-aed3-4ba6-b2d5-9dcc908e1884.png">
<img width="976" alt="image" src="https://user-images.githubusercontent.com/109241600/205480067-0d952b85-01eb-4cb3-9f3f-1878077833ce.png">
