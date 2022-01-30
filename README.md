# genjwtkey

This package is a generator of assertion key pair for LINE Bot.

このパッケージは、LINEボットで利用可能な、アサーション用のキーペアを生成します。

## Requirements

You need to install rust, because cryptography packages needs rust to build its own.

cryptographyパッケージの利用に、Rustのインストールが必要です。

---------

## installation

``` pip install genjwtkey ```

## quick start

``` python -m genjwtkey ```

Two file outputs

- ./publick_key.json
- ./private_key.json
