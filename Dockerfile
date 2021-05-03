from python:3.9.1
copy . /app
RUN pip install bs4 && pip install requests
WORKDIR /app
VOLUME /app/dados/fornecedores
CMD python webscrip.py
