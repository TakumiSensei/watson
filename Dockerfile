FROM python:3.11

WORKDIR /workspaces/watson

# requirements.txtから必要なライブラリをインストール
RUN pip install -r requirements.txt
