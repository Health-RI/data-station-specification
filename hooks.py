"""MkDocs hooks for locale-aware configuration."""


def on_config(config):
    """Swap the auto_append glossary file based on the current build locale."""
    i18n_plugin = config.get("plugins", {}).get("i18n")
    if i18n_plugin is None:
        return config

    current_language = getattr(i18n_plugin, "current_language", None)
    if current_language is None:
        return config

    # Find the pymdownx.snippets extension config
    for ext in config.get("markdown_extensions", []):
        if hasattr(ext, "getConfigs"):
            # markdown extension objects
            pass

    # MkDocs stores mdx_configs separately
    snippets_config = config.get("mdx_configs", {}).get("pymdownx.snippets", {})
    if snippets_config and current_language == "en":
        snippets_config["auto_append"] = ["includes/woordenlijst.en.md"]
    elif snippets_config:
        snippets_config["auto_append"] = ["includes/woordenlijst.md"]

    return config
