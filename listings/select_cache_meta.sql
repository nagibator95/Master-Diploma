SELECT key FROM
    monitor_cahce_meta
WHERE
    invalidate_args LIKE '%polzovatel=1%'
AND invalidate_args LIKE '%zada4a=1%'