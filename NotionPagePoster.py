import requests

# トークンとページIDを設定
token = 'your-integration-token'
page_id = 'your-page-id'

# ヘッダーに認証情報を設定
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

# 投稿したい本文をJSON形式で定義
data = {
    "parent": {"page_id": page_id},
    "properties": {
        "title": {
            "title": [
                {
                    "text": {
                        "content": "Your Page Title"
                    }
                }
            ]
        }
    },
    "children": [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Your main content here."
                        }
                    }
                ]
            }
        }
    ]
}

# APIリクエストを送信
response = requests.post('https://api.notion.com/v1/pages', headers=headers, json=data)

# レスポンスを表示
print(response.text)
