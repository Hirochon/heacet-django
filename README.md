# heacet-django
Djangoでバックエンド構築してみた。

# 概要
PythonのフレームワークDjangoを用いて、CRUD、検索、クエリ検索、バリデーション、ページネーション、リレーションシップを実装しました。

## 開発環境
- Python3.7.3
- Django2.2.6

## アプリケーションの使い方
こちらのアプリケーションは管理人登録をしなければ、ページネーションの関係で起動しません。なので管理人登録するためにmigrationを行う必要があります。セキュリティ上の問題で、gitignoreでDBとmigrationsを設定しているので、以下動作が必要となります。

1. 以下のコマンドを実行してください。
	1. python manage.py makemigrations heacet
	2. python manage.py migrate
2. 次に以下のコマンドにてIDとメールアドレス、パスワードを設定してください。
	1. python manage.py createsuperuser
3. localhost:8000/adminにアクセスしていただき、ログインを行ってください。
4. Nogizakasのデータを3人以上登録していただくと、アプリケーションを使用することができます。
