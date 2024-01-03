"""
Pythonを使用してNotion APIにアクセスし、特定のページにコンテンツを投稿するためのものです。Notion APIキーとページIDを設定し、リクエストヘッダーを構成しています。post_content_to_notion関数は、指定されたタイトル、コンテンツ、およびオプションの画像URLを使用してNotionページに新しいコンテンツを投稿します。最後に、この関数を使用して実際のコンテンツを投稿しています。






"""

import requests
import json

# Notion APIの設定
# ここでは、APIキーとページIDを指定しています。
# APIキーとページIDは秘匿情報なので、実際のコードでは安全に保管し、公開しないように注意してください。
NOTION_API_KEY = 'your_notion_api_key'
NOTION_PAGE_ID = 'your_notion_page_id'
NOTION_API_URL = 'https://api.notion.com/v1/pages'

# Notion APIヘッダー
# ここでは、APIリクエストに必要なヘッダー情報を設定しています。
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Notionページにコンテンツを投稿する関数
def post_content_to_notion(title, content, image_url=None):
    # ここではNotionに投稿するためのデータ構造を定義しています。
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

    # もし画像URLが提供されている場合、画像ブロックを追加します。
    if image_url:
        children.append(
            {
                "type": "image",
                "image": {
                    "type": "external",
                    "external": {
                        "url": image_url
                    }
                }
            }
        )

    # ここで、Notion APIに送信するデータを構築しています。
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

    # ここで、作成したデータを用いてNotion APIにリクエストを送信しています。
    response = requests.post(NOTION_API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("コンテンツがNotionに追加されました。")
    else:
        print("エラーが発生しました。", response.text)

# コンテンツと画像の追加（画像あり）
# ここでは、タイトル、コンテンツ、画像URLを指定して、Notionに投稿しています。
post_content_to_notion("タイトル", "コンテンツ", "https://www.example.com/image.png")

# コンテンツのみの追加（画像なし）
# ここでは、タイトルとコンテンツのみを指定して、Notionに投稿しています。
post_content_to_notion("タイトル", "コンテンツ")
