SELECT key FROM
    monitor_cahce_meta
WHERE
    invalidate_args LIKE '%пользователь=1%'
AND invalidate_args LIKE '%задача=1%'