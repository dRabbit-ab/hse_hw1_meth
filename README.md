# hse_hw1_meth

## Ссылка на колаб

https://colab.research.google.com/drive/1E5iu9mjO0C80N4C8pTGs8jUXBAJRb8B-?usp=sharing

## Основная часть

### Задание 1

Слева я показал графики из отчета к одному из прошлых домашних заданий, справа к текущему

На графиках ниже мы можем видеть, что качество чтений довольно высокое
<p float="left">
  <img src="https://user-images.githubusercontent.com/79662580/154859853-73df444f-da96-49ea-94bf-33dc38776260.png"  width="300" />
  <img src="https://user-images.githubusercontent.com/79662580/154859862-36aab7a8-8b6c-4d79-809d-e40c3942402f.png"  width="300" />
</p>

Качество чтений довольно высокое, однако падает под конец, тем не менее в целом это приемлемо
<p float="left">
  <img src="https://user-images.githubusercontent.com/79662580/154859866-7b94c1df-9fb3-4afb-af67-82a26edee8a7.png"  width="300" />
  <img src="https://user-images.githubusercontent.com/79662580/154859869-aa6e73a3-166a-45a6-802f-be8681aaaa04.png"  width="300" />
</p>

Можно увидеть повышенное содержание тимина и пониженное цитозина. Заметим, что в теории содержание обоих элементов должно быть примерно равным 25%. Однако мы видим ситуацию, где содержание тимина выше теоритического примерно на 10-15%, а содежание цитозина меньше теоритического примерно на те же 10-15%. Возможно такая ситуация может быть связана с особенностями секвенирования
<p float="left">
  <img src="https://user-images.githubusercontent.com/79662580/154859876-f9243337-94dd-4c24-a379-38f0bb4ab7a0.png"  width="300" />
  <img src="https://user-images.githubusercontent.com/79662580/154859880-bdc69a3c-6349-4ea4-968e-bc452dfa4b24.png"  width="300" />
</p>

Распределение значений сильно отличается от теоретического для нашей последовательности. Выделяются харкатерные два пика, на примере прошлого отчета мы такого не наблюдаем
<p float="left">
  <img src="https://user-images.githubusercontent.com/79662580/154859894-4bdb4f72-1bd7-4e12-9483-cca69bca3ede.png"  width="300" />
  <img src="https://user-images.githubusercontent.com/79662580/154859900-a5a136f5-1830-4139-b848-ec518c2de228.png"  width="300" />
</p>

### Задание 2

#### Статистика

|          | 11347700-11367700 | 40185800-40195800 |  Дуплицировано, % |
| -------- | ----------------- | ----------------- | ----------------- |
| 8 cell   | 1090              | 464               | 18.31%            |
| epiblast | 2328              | 1062              | 2.92%             |
| icm      | 1456              | 630               | 9.08%             |

#### M-bias plot

| [8 cell](https://github.com/dRabbit-ab/hse_hw1_meth/blob/main/data/SRR5836473_1_bismark_bt2_PE_report.html) | [ICM](https://github.com/dRabbit-ab/hse_hw1_meth/blob/main/data/SRR3824222_1_bismark_bt2_PE_report.html) | [epiblast](https://github.com/dRabbit-ab/hse_hw1_meth/blob/main/data/SRR5836475_1_bismark_bt2_PE_report.html) |
| ----------------- | ----------------- | ----------------- |
|![Bismark M-bias Read 1 473](https://user-images.githubusercontent.com/79662580/154861385-37a145db-6097-4c4c-bccc-424e6a515e2a.png) |![Bismark M-bias Read 1 4222](https://user-images.githubusercontent.com/79662580/154861396-6a820a43-2d70-40ae-bd7d-a23f14c18c3e.png) | ![Bismark M-bias Read 1 475](https://user-images.githubusercontent.com/79662580/154861408-6a985666-c5e0-4117-8b35-3031a2633b7f.png) |
|![Bismark M-bias Read 2 473](https://user-images.githubusercontent.com/79662580/154861430-986ec78b-153b-44b3-9e15-e0b7e0eaf533.png)|![Bismark M-bias Read 2 4222](https://user-images.githubusercontent.com/79662580/154861435-b11e71cd-6552-463a-ba76-4d320be92854.png)|![Bismark M-bias Read 2 475](https://user-images.githubusercontent.com/79662580/154861436-41afa56a-86af-4ed0-a2a9-dad6cd364085.png)|

#### Гистограммы распределения метилирования цитозинов

| 8 cell | ICM |  epiblast |
| ----------------- | ----------------- | ----------------- |
|![8_cell_hist](https://user-images.githubusercontent.com/79662580/154861898-04ca97ef-ca5d-45e2-afd5-f2b0f0feee63.png)|![icm_hist](https://user-images.githubusercontent.com/79662580/154861903-a53cf295-69a7-4b9d-a096-0678853fbd3c.png)|![epiblast_hist](https://user-images.githubusercontent.com/79662580/154861907-065d681c-16c4-473c-9d33-28236049cebf.png)|
