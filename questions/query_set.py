def set_builder(filter_set):
    query_set = filter_set.values(
        'branch__name', 'subject__subject_name', 'exam__name', 'year', 'semester', 'paper',).order_by('-year')
    papers = {}
    for i in query_set:
        if i['year'] not in papers:
            papers[i['year']] = []
        papers[i['year']].append(i)
    return papers.items()
