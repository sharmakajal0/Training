FROM python:3.8
WORKDIR /code
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./requirements.txt /code/requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN /usr/local/bin/python -m pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./todoapp /code/todoapp
CMD ["uvicorn", "todoapp.app:app", "--host", "0.0.0.0", "--port", "80"]