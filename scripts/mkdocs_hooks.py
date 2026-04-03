import html
import json
from typing import Any

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Link, Navigation, Section
from mkdocs.structure.pages import Page


site_files: Files | None = None


def generate_renamed_section_items(
    items: list[Page | Section | Link], *, config: MkDocsConfig
) -> list[Page | Section | Link]:
    new_items: list[Page | Section | Link] = []
    for item in items:
        if isinstance(item, Section):
            new_title = item.title
            new_children = generate_renamed_section_items(item.children, config=config)
            first_child = new_children[0]
            if isinstance(first_child, Page):
                if first_child.file.src_path.endswith("index.md"):
                    # Read the source so that the title is parsed and available
                    first_child.read_source(config=config)
                    new_title = first_child.title or new_title
            # Creating a new section makes it render it collapsed by default
            # no idea why, so, let's just modify the existing one
            # new_section = Section(title=new_title, children=new_children)
            item.title = new_title
            item.children = new_children
            new_items.append(item)
        else:
            new_items.append(item)
    return new_items


def on_nav(
    nav: Navigation, *, config: MkDocsConfig, files: Files, **kwargs: Any
) -> Navigation:
    new_items = generate_renamed_section_items(nav.items, config=config)
    return Navigation(items=new_items, pages=nav.pages)


def on_files(files: Files, *, config: MkDocsConfig, **kwargs: Any) -> Files:
    global site_files
    site_files = files
    return files


def _get_translation_src_uri(src_uri: str, target_lang: str) -> str:
    if target_lang == "ja":
        if src_uri.endswith(".ja.md"):
            return src_uri
        return src_uri.removesuffix(".md") + ".ja.md"
    if target_lang == "en":
        if src_uri.endswith(".ja.md"):
            return src_uri.removesuffix(".ja.md") + ".md"
        return src_uri
    raise ValueError(f"Unsupported language: {target_lang}")


def on_page_context(
    context: dict[str, Any],
    *,
    page: Page,
    config: MkDocsConfig,
    **kwargs: Any,
) -> dict[str, Any]:
    if site_files is None:
        return context

    src_uri = page.file.src_uri
    is_japanese_page = src_uri.endswith(".ja.md")

    english_file = site_files.get_file_from_path(_get_translation_src_uri(src_uri, "en"))
    japanese_file = site_files.get_file_from_path(
        _get_translation_src_uri(src_uri, "ja")
    )

    context["language_alternates"] = [
        {
            "lang": "en",
            "name": "English",
            "link": english_file.url if english_file else page.file.url,
            "selected": not is_japanese_page,
            "available": True,
        },
        {
            "lang": "ja",
            "name": "日本語" if japanese_file else "日本語 (未翻訳)",
            "link": japanese_file.url if japanese_file else None,
            "selected": is_japanese_page,
            "available": japanese_file is not None,
        },
    ]
    return context


def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, **kwargs: Any
) -> str:
    if site_files is None:
        return markdown

    src_uri = page.file.src_uri
    is_japanese_page = src_uri.endswith(".ja.md")

    english_file = site_files.get_file_from_path(_get_translation_src_uri(src_uri, "en"))
    japanese_file = site_files.get_file_from_path(
        _get_translation_src_uri(src_uri, "ja")
    )

    language_alternates = [
        {
            "lang": "en",
            "name": "English",
            "link": english_file.url if english_file else page.file.url,
            "selected": not is_japanese_page,
            "available": True,
        },
        {
            "lang": "ja",
            "name": "日本語" if japanese_file else "日本語 (未翻訳)",
            "link": japanese_file.url if japanese_file else None,
            "selected": is_japanese_page,
            "available": japanese_file is not None,
        },
    ]

    payload = html.escape(json.dumps(language_alternates, ensure_ascii=False), quote=True)
    marker = (
        f'<div id="language-switcher-data" '
        f'data-language-alternates="{payload}" hidden></div>\n\n'
    )
    return marker + markdown
