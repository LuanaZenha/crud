#Etapa de runtime (rápida para dev)

FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \ PYTHONBUFFERED=1 \ PIP_NO_CACHE_DIR=1
WORKDIR /app
COPY requirements.txt .

# Opcional
RUN python -m pip install --upgrade pip

# Instalar as dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar o app por último para aproveitar o cache

COPY app ./app

# Documenta a porta usada pela aplicação dentro do container
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]