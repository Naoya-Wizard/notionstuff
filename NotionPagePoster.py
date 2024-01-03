"""
このPythonスクリプトは、Notion APIを利用して特定のNotionページにコンテンツを追加するためのものです。スクリプトは以下の主要な部分から構成されています：

1. Notion APIの設定:
   - Notion APIにアクセスするためのAPIキー（NOTION_API_KEY）と、コンテンツを追加する対象のページID（NOTION_PAGE_ID）を定義しています。

2. APIリクエストのヘッダー設定:
   - Notion APIにリクエストを送る際に必要なヘッダー情報（認証トークン、コンテントタイプ、使用するAPIのバージョン）を設定しています。

3. コンテンツ投稿関数（post_content_to_notion）の定義:
   - この関数は、指定されたタイトル、テキストコンテンツ、および複数の画像URLを用いて、Notionページに新しいコンテンツを追加するためのものです。
   - 複数の画像URLが提供された場合、それらの画像もページに追加されます。

4. 実際のコンテンツ投稿処理:
   - 最後に、上述の関数を使って、実際にコンテンツ（画像が複数ある場合とない場合）をNotionページに追加しています。

このコードを使用する際には、個々のAPIキーとページIDを安全に管理し、公開しないよう注意する必要があります。
"""

import requests
import json

# Notion APIの設定
NOTION_API_KEY = 'your_notion_api_key'
NOTION_PAGE_ID = 'your_notion_page_id'
NOTION_API_URL = 'https://api.notion.com/v1/pages'

# Notion APIヘッダー
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def post_content_to_notion(title, content, image_urls=None):
    children = [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": content
                        }
                    }
                ]
            }
        }
    ]

    if image_urls:
        for url in image_urls:
            children.append(
                {
                    "type": "image",
                    "image": {
                        "type": "external",
                        "external": {
                            "url": url
                        }
                    }
                }
            )

    data = {
        "parent": {"page_id": NOTION_PAGE_ID},
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        },
        "children": children
    }

    response = requests.post(NOTION_API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("コンテンツがNotionに追加されました。")
    else:
        print("エラーが発生しました。", response.text)

# 画像が複数ある場合
image_urls = ["https://www.example.com/image1.png", "https://www.example.com/image2.png", "https://www.example.com/image3.png"]
post_content_to_notion("タイトル", "コンテンツ", image_urls)

# 画像がない場合の例
post_content_to_notion("タイトル", "コンテンツ")
