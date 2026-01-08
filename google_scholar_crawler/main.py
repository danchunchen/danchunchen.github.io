#!/usr/bin/env python3
"""
Google Scholar Citation Crawler
Fetches citation data from Google Scholar and saves to JSON files.
"""

from scholarly import scholarly
import json
from datetime import datetime
import os
import sys


def main():
    # 从环境变量获取 Google Scholar ID
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')

    if not scholar_id:
        print("Error: GOOGLE_SCHOLAR_ID environment variable not set")
        sys.exit(1)

    print(f"Fetching data for Google Scholar ID: {scholar_id}")

    try:
        # 获取作者信息
        author = scholarly.search_author_id(scholar_id)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

        # 添加更新时间
        author['updated'] = str(datetime.now())

        # 将出版物转换为字典格式（以 author_pub_id 为键）
        author['publications'] = {
            pub['author_pub_id']: pub
            for pub in author['publications']
        }

        # 创建输出目录
        os.makedirs('results', exist_ok=True)

        # 保存完整数据
        with open('results/gs_data.json', 'w', encoding='utf-8') as f:
            json.dump(author, f, ensure_ascii=False, indent=2, default=str)

        # 保存 shields.io 格式数据（用于徽章）
        shieldio_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(author.get('citedby', 0)),
            "color": "blue"
        }
        with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as f:
            json.dump(shieldio_data, f, ensure_ascii=False)

        print(f"Successfully fetched data:")
        print(f"  Name: {author.get('name', 'N/A')}")
        print(f"  Total citations: {author.get('citedby', 'N/A')}")
        print(f"  h-index: {author.get('hindex', 'N/A')}")
        print(f"  Publications: {len(author.get('publications', {}))}")

    except Exception as e:
        print(f"Error fetching Google Scholar data: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
