def _slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", text).strip("_") or "output"


def _default_base_name(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc or parsed.path
    path = parsed.path.replace("/", "_")
    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    return _slugify(f"{host}{path}_{stamp}")