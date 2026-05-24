"""Surf Valkyrie Codex provider profile."""

from providers import register_provider
from providers.base import ProviderProfile

valkyrie_codex = ProviderProfile(
    name="valkyrie-codex",
    aliases=("valkyrie", "valkyrie_codex", "valkyrie-openai"),
    display_name="Valkyrie Codex",
    description="Surf Valkyrie /codex gateway.",
    api_mode="codex_responses",
    env_vars=("VALKYRIE_API_KEY",),
    base_url="https://valkyrie.ask.surf/codex",
    auth_type="api_key",
    supports_health_check=False,
    fallback_models=("gpt-5.5",),
    default_headers={
        "x-rip-entrypoint": "ccfy-hermes",
    },
)

register_provider(valkyrie_codex)
