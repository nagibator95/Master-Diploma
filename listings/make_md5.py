def _dump_to_ascii_str(obj) -> str:
    """Dump object to ascii-encoded string."""
    return pickle.dumps(obj, PICKLE_ASCII_PROTO).decode()


def get_cache_key(func: Callable, prefix: str,
                  args: tuple, kwargs: dict) -> str:
    """Get unique key to be used as cache key in redis or smth."""
    dumped_args = _dump_to_ascii_str(args)
    dumped_kwargs = _dump_to_ascii_str(kwargs)
    key = f'{dumped_args}_{dumped_kwargs}'
    hashed_key = hashlib.md5(key.encode('ascii'))
    return f'{prefix}/{func.__name__}_{hashed_key.hexdigest()}'
