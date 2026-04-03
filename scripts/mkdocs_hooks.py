import posixpath
import re
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Link, Navigation, Section
from mkdocs.structure.pages import Page


translated_page_uris: set[str] = set()


def on_files(files: Files, *, config: MkDocsConfig, **kwargs: Any) -> Files:
    translated_english_pages = []
    src_uris = set(files.src_uris)
    global translated_page_uris
    translated_page_uris = {src_uri for src_uri in src_uris if src_uri.endswith(".ja.md")}
    for file in files.documentation_pages():
        src_uri = file.src_uri
        if src_uri.endswith(".ja.md") or not src_uri.endswith(".md"):
            continue
        japanese_src_uri = src_uri.removesuffix(".md") + ".ja.md"
        if japanese_src_uri in src_uris:
            translated_english_pages.append(file)
    for file in translated_english_pages:
        files.remove(file)
    return files


def _rewrite_markdown_link_target(target: str, current_src_uri: str) -> str:
    parts = urlsplit(target)
    if (
        parts.scheme
        or parts.netloc
        or not parts.path
        or not parts.path.endswith(".md")
    ):
        return target
    current_dir = posixpath.dirname(current_src_uri)
    normalized_target = posixpath.normpath(posixpath.join(current_dir, parts.path))
    japanese_target = normalized_target.removesuffix(".md") + ".ja.md"
    if japanese_target not in translated_page_uris:
        return target
    relative_target = posixpath.relpath(japanese_target, current_dir or ".")
    if not relative_target.startswith("."):
        relative_target = f"./{relative_target}"
    return urlunsplit(
        ("", "", relative_target, parts.query, parts.fragment)
    )


def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, **kwargs: Any
) -> str:
    return re.sub(
        r"(?P<prefix>\[[^\]]+\]\()(?P<target>[^)\s]+\.md(?:#[^)]+)?)(?P<suffix>\))",
        lambda match: (
            f"{match.group('prefix')}"
            f"{_rewrite_markdown_link_target(match.group('target'), page.file.src_uri)}"
            f"{match.group('suffix')}"
        ),
        markdown,
    )


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
                if first_child.file.src_path.endswith(("index.md", "index.ja.md")):
                    # Read the source so that the title is parsed and available
                    first_child.read_source(config=config)
                    new_title = first_child.title or new_title
            # Creating a new section makes it render it collapsed by default
            # no idea why, so, let's just modify the existing one
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
