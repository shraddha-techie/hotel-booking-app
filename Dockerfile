FROM python:3.12-slim

WORKDIR /app
COPY . /app

# yaha Streamlit install karo
RUN pip install --no-cache-dir streamlit

CMD ["streamlit", "run", "app.py", "--server.port=8502", "--server.address=0.0.0.0"]
