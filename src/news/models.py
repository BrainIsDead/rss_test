from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField(null=True)
    link = models.URLField(max_length = 250, null=True)
    trend =models.CharField(max_length = 250, null=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return str(self.title)
