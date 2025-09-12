# NWCD2

ネットワークのセキュリティ状況をチェックするツールです。簡単なコマンドで脆弱性や設定ミスを確認できます。

## インストール

```bash
git clone https://github.com/viiiviii538/NWCD2.git
cd NWCD2
pip install -r requirements.txt
```

## セットアップ手順

依存関係のインストールや仮想環境の作成は `setup.sh` で自動化されています。

```bash
./setup.sh
```

このスクリプトは Python 仮想環境の作成と pip の更新を行い、`requirements.txt` と `requirements-dev.txt` が存在すればそれらをインストールします。

## 5分で試す

```bash
python main.py --target example.com
```

## APIサーバーの起動

```bash
uvicorn yourtool.api:app --host 127.0.0.1 --port 8787
```

### エンドポイント

- `POST /scan`
  - リクエスト: `{"target": "example.com"}`
  - レスポンス: `{"status": "ok", "target": "example.com"}`

## 開発手順

### 依存関係のインストール

```bash
pip install -r requirements-dev.txt
```

### テスト実行

```bash
pytest
```
