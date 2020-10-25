1. some data
2. We are in the __main__
   2020-10-24 17:57:27.429626
   linux

3. Using command `python3 . -h`
   usage: . [-h] [-o OPT] [-l]

Приклад передачі аргументів у Python програму.

optional arguments:
  -h, --help            show this help message and exit
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.
  -l, --logs            Якщо виконати команду з цим параметром будуть
                        виводитись логи.
4. Using command `python3 . -o "some text"`
   We are in the __main__
   2020-10-24 18:06:46.430001
   linux
   З консолі було передано аргумент
   ========== >> some text << ==========
5. Using command `python3 . --logs`
   2020-10-24 18:08:27,597 root INFO: Тут буде просто інформативне повідомлення
   2020-10-24 18:08:27,606 root WARNING: Це Warning повідомлення
   2020-10-24 18:08:27,607 root ERROR: Це повідомлення про помилку
6. Writting home_work
7. Writting my_func() in modules/common.py
8. Writting log_func() in __main__.py   


