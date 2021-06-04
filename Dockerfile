FROM python:3.8.0

RUN apt-get update \
  && apt-get upgrade -y \
  # imageのサイズを小さくするためキャッシュを削除
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  # pipのアップグレード
  && pip install --upgrade pip

# 作業ディレクトリの変更
WORKDIR /home/python

# ライブラリのインストール
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt
COPY . ${PWD}
