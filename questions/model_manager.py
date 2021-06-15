from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery, TrigramSimilarity
from django.contrib.postgres.aggregates import StringAgg
from django.db.models import F
from django.db import models


def filePath(instance, filename):
    filename = f"{instance.subject}_{instance.year}_{instance.semester}_{instance.exam}.pdf"
    return f'files/{filename}'


class QuestionPaperManager(models.Manager):
    def search(self, search_text):
        search_query = SearchQuery(search_text)
        search_rank = SearchRank(F("search_vector"), search_query)
        trigram_similarity = TrigramSimilarity(
            "subject__subject_name", search_text)

        query_set = (
            self.get_queryset()
            .filter(search_vector=search_query)
            .annotate(rank=search_rank + trigram_similarity)
            .order_by('-rank')
        )
        return query_set

    def with_documents(self):
        vector = (
            SearchVector("subject__subject_name_short", weight="A")
            + SearchVector(
                StringAgg("subject__subject_name", delimiter=' '),
                weight="A",
                config='english',
            )
            + SearchVector("branch__name", weight="B")
            + SearchVector("exam__name", weight="C")
            + SearchVector("exam__name_1", weight="C")
            + SearchVector("exam__name_2", weight="C")
            + SearchVector("year", weight="C")
            + SearchVector("semester", weight="D")
        )
        return self.get_queryset().annotate(document=vector)
