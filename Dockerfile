FROM python:3.11

WORKDIR /workspaces/watson

# requirements.txtから必要なライブラリをインストール
COPY . .
RUN pip install -r requirements.txt

# ポート開放 (uvicornで指定したポート)
EXPOSE 8080

# 実行
CMD python app/main.py