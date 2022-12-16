# neuralhoro
 Нейронная сеть, которая генерирует гороскоп, и телеграмм бот, который выводит сгенерированный гороскоп

#Парсер

В качестве датасета мы решили взять информацию с сайта [Rambler](https://horoscopes.rambler.ru/) с 2004 по 2021 год.
Полученные данные и сам парсер лежат на ветке Parser and data.

В итоге у нас получилось ~79 000 гороскопов на все знаки зодиака.

#Нейронка
В качестве нейронной сети нами было принято решение взять RuGPT-3 от Сбера и дообучить её на спарсенных данных.


#Telegramm-bot 


#Пример работы
Рыбам звезды советуют воздержаться от начинаний и новых начинаний, пока не сформированы предпосылки для успеха. Если вы
не готовы к рывку или у вас нет нужных ресурсов, можно пустить в ход таланты и умения, даруемые вам обстоятельствами. К
ночи ваше настроение может испортиться, станет менее стабильным, вероятен упадок сил.

Тельцам сегодня не стоит спешить с выводами. Если вы уверены в своей правоте и стойкой позиции, звезды советуют не
торопить события и дождаться благоприятного момента. Не стоит терять время, если вы заинтересованы в развитии партнерства
или хотите выступить в роли дипломата. День хорош для вступления в союз, для признания в правах, для закрепления вами
своих полномочий, для получения поддержки от авторитетных лиц или из нужных источников.

Козероги, избегайте резких движений, сегодня лучше действовать в удобном для вас стиле. В то же время, звезды советуют
вам быть внимательнее к деталям, иначе вы можете совершить фатальную ошибку. Не стоит спешить с выводами, лучше обдумать
всю картину происходящего и составить план действий. Нежелательны переговоры, особенно на деликатной территории.
Водолеям день добавит уверенности в себе, поможет выйти победителем из любого противостояния.

# Заключение
Впринцепе, нейронка натренировалась достаточно неплохо, хоть и под конец обучение loss составлял 1.6, однако иногда
тексты, которые выдает нейросеть, не очень могут быть или не очень "человечными" или переключаться с
одного знака зодиака, на другой(см. на 3 пример).