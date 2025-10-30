#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
全 .ipynb の先頭に「Open in Colab」バッジを挿入します。
- 既に先頭に Colab バッジがある場合はスキップ
- URL は GitHub 上のパスを URL エンコードして生成
- --dry-run: 変更せずに結果を表示
- --backup: .bak を作ってから上書き

対象リポジトリ（例）:
  https://github.com/trainocate-japan/openai_api_app
の 'main' ブランチを前提にしています（必要に応じて --branch で変更可）
"""

import argparse
from pathlib import Path
import shutil
import sys
from urllib.parse import quote
import nbformat as nbf

def build_badge_md(repo_owner: str, repo_name: str, branch: str, nb_rel_path: str) -> str:
    """
    ノートブックのリポジトリ内相対パスから、Colab バッジの Markdown を作成
    """
    # URL エンコード（スラッシュは残す）
    encoded_path = quote(nb_rel_path, safe="/")
    colab_url = f"https://colab.research.google.com/github/{repo_owner}/{repo_name}/blob/{branch}/{encoded_path}"
    badge_img = "https://colab.research.google.com/assets/colab-badge.svg"
    return f'[![Open In Colab]({badge_img})]({colab_url})'

def has_badge_in_first_cell(nb) -> bool:
    """
    先頭セルに Colab バッジが既にあるかどうかを雑に判定
    """
    if not nb.cells:
        return False
    first = nb.cells[0]
    if first.cell_type != "markdown":
        return False
    src = first.source.lower()
    # 画像URLか "open in colab" 文字列のどちらかがあればある程度OKとみなす
    return ("colab-badge.svg" in src) or ("open in colab" in src)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".", help="リポジトリのルートディレクトリ（デフォルト: 現在のディレクトリ）")
    parser.add_argument("--owner", default="trainocate-japan", help="GitHub オーナー（ユーザー/組織）")
    parser.add_argument("--repo", default="openai_api_app", help="GitHub リポジトリ名")
    parser.add_argument("--branch", default="main", help="対象ブランチ名（デフォルト: main）")
    parser.add_argument("--dry-run", action="store_true", help="変更せずに結果だけ表示")
    parser.add_argument("--backup", action="store_true", help="上書き前に .bak を作成")
    parser.add_argument("--verbose", action="store_true", help="詳細ログを表示")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    if not root.exists():
        print(f"[ERROR] repo-root が見つかりません: {root}", file=sys.stderr)
        sys.exit(1)

    ipynb_files = sorted(root.rglob("*.ipynb"))

    if not ipynb_files:
        print("[INFO] ノートブックが見つかりませんでした。")
        return

    modified = 0
    skipped = 0
    errors = 0

    for nb_path in ipynb_files:
        # .ipynb_checkpoints 配下はスキップ
        if ".ipynb_checkpoints" in nb_path.parts:
            continue

        try:
            nb = nbf.read(nb_path, as_version=4)
        except Exception as e:
            errors += 1
            print(f"[ERROR] 読み込み失敗: {nb_path} ({e})", file=sys.stderr)
            continue

        if has_badge_in_first_cell(nb):
            skipped += 1
            if args.verbose:
                print(f"[SKIP] 既にバッジあり: {nb_path}")
            continue

        # ルートからの相対パスを生成（Windows 対応で '/' 区切りに）
        rel_path = nb_path.relative_to(root).as_posix()
        badge_md = build_badge_md(args.owner, args.repo, args.branch, rel_path)

        # 先頭に Markdown セルを挿入
        badge_cell = nbf.v4.new_markdown_cell(badge_md)
        nb.cells.insert(0, badge_cell)

        if args.dry_run:
            print(f"[DRY-RUN] 追加予定: {nb_path}")
            continue

        # バックアップ
        if args.backup:
            backup_path = nb_path.with_suffix(nb_path.suffix + ".bak")
            try:
                shutil.copy2(nb_path, backup_path)
            except Exception as e:
                errors += 1
                print(f"[ERROR] バックアップ失敗: {nb_path} -> {backup_path} ({e})", file=sys.stderr)
                continue

        try:
            nbf.write(nb, nb_path)
            modified += 1
            print(f"[OK] バッジ追加: {nb_path}")
        except Exception as e:
            errors += 1
            print(f"[ERROR] 書き込み失敗: {nb_path} ({e})", file=sys.stderr)

    if args.dry_run:
        print("\n[DRY-RUN] 実行結果サマリ（実ファイルは変更していません）")
        print(f"  対象ノートブック数: {len(ipynb_files)}")
        print(f"  変更予定: {len(ipynb_files) - skipped}")
        print(f"  スキップ（既にバッジあり）: {skipped}")
        print(f"  読み込み/書き込みエラー: {errors}")
    else:
        print("\n実行結果サマリ")
        print(f"  処理対象: {len(ipynb_files)}")
        print(f"  追加: {modified}")
        print(f"  スキップ（既にバッジあり）: {skipped}")
        print(f"  エラー: {errors}")

if __name__ == "__main__":
    main()
