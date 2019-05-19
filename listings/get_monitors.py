@monitor_cacher
def get_runs(problem_id: int = None, user_ids: Iterable = None,
             time_after: int = None, time_before: int = None):
    """"""
    query = db.session.query(Run) \
        .join(SimpleUser, SimpleUser.id == Run.user_id)

    if problem_id is not None:
        query = query.filter(Run.problem_id == problem_id)

    if user_ids is not None:
        query = query.filter(SimpleUser.id.in_(user_ids))

    if time_after is not None:
        time_after = datetime.datetime.fromtimestamp(time_after)
        query = query.filter(Run.create_time > time_after)
    if time_before is not None:
        time_before = datetime.datetime.fromtimestamp(time_before)
        query = query.filter(Run.create_time < time_before)

    load_only_fields = [
        'id',
        'user_id',
        'create_time',
        'ejudge_score',
        'ejudge_status',
        'ejudge_test_num'
    ]

    runs = query.order_by(Run.id) \
                .options(joinedload(Run.user)
                         .load_only('id', 'firstname', 'lastname')) \
                .options(Load(Run).load_only(*load_only_fields))

    schema = RunSchema(many=True)
    data = schema.dump(runs.all())
    return data.data