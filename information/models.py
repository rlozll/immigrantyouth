from django.db import models

class Institution(models.Model):
    REGION_CHOICES = [
        ('서울', '서울'),
        ('경기', '경기'),
        ('인천', '인천'),
        ('세종', '세종'),
        ('충남', '충남'),
        ('경북', '경북'),
        ('울산', '울산'),
        ('경남', '경남'),
        ('부산', '부산'),
    ]

    name = models.CharField(max_length=100)  # 기관명
    type = models.CharField(max_length=50)   # 기관 구분 (공공기관 등)
    region = models.CharField(max_length=10, choices=REGION_CHOICES)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.region} - {self.name}"
