# NWCD2

ネットワークのセキュリティ状況をチェックするツールです。簡単なコマンドで脆弱性や設定ミスを確認できます。

## インストール

```bash
git clone https://github.com/viiiviii538/NWCD2.git
cd NWCD2
pip install -r requirements.txt
```

## 5分で試す

```bash
python main.py --target example.com
```

## APIサーバの起動

FastAPI を利用した API サーバを起動します。

```bash
uvicorn yourtool.api:app --host 127.0.0.1 --port 8787
```

## 開発手順

### 依存関係のインストール

```bash
pip install -r requirements-dev.txt
```

### テスト実行

```bash
pytest
```
