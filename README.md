# DZ_2
# Игра ЛОТО
Правила игры:<br/>
На двух карточках в трёх рядах и девяти колонках расположены 15 случайных чисел по 5 в ряду; разряд десятков цифр соответствует номеру колонки слева, считая с нуля; 90 помещается в последнюю колонку. Игра состоит в том, что играющие закрывают на картах номера, от 1 до 90.<br/>
После начала игры на экране выводятся 2 карточки, одна игрока, вторая компьютера, а также информация о выпавшем номере и осташемся в мешке количестве боченков.<br/>
<br/>
<pre>
Текущий бочонок: 87 Осталось в мешке: 89<br/>

############# Человек #############
  3  11      38  45              90
             36      52  62  79  86
         28      44  58  65  75    
###################################
############ Компьютер ############
  6  19  25      49  57            
     11  24  38      59          88
  3          36          62  75  84
###################################
</pre>
<br/>
После этого игроку предлагается ввести "y", если число присутсвует в его карточке или "n", если отсутсвует. Игра продолжается до тех пор, пока в одной из карточек не закроются все числа. Тот игрок, который первый закроет все числа в своей карточке становится победителем.<br/>
<br/>
Тестирование:<br/>
<pre>
$ pytest -v
=========================test session starts==========================
platform win32 -- Python 3.8.1, pytest-5.3.2, py-1.8.1, pluggy-0.13.1 -- c:\users\sa\appdata\local\programs\python\python38\python.exe
cachedir: .pytest_cache
rootdir: C:\web_python\DZ_2
plugins: mock-1.13.0
collected 11 items                                                                                                                  
tests/test_engine.py::test_set_card_len_array_collumn PASSED    [  9%]
tests/test_engine.py::test_set_card_len_array_row PASSED        [ 18%]
tests/test_engine.py::test_set_card_number_sum PASSED           [ 27%]
tests/test_engine.py::test_set_card_number_row_sum PASSED       [ 36%]
tests/test_engine.py::test_set_card_number_col_sum PASSED       [ 45%]
tests/test_engine.py::test_set_card_number_range PASSED         [ 54%]
tests/test_engine.py::test_search_score PASSED                  [ 63%]
tests/test_engine.py::test_search_remove_keg PASSED             [ 72%]
tests/test_engine.py::test_search_replace_keg PASSED            [ 81%]
tests/test_engine.py::test_get_keg_sum PASSED                   [ 90%]
tests/test_engine.py::test_get_keg_range PASSED                 [100%]
</pre>
