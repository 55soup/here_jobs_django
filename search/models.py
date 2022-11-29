from django.db import models

# Create your models here.
class Jobs(models.Model):
    enterprise = models.CharField(max_length=50) #기업명
    enterprise_num = models.CharField(max_length=50) #사업자등록번호
    sector = models.CharField(max_length=50) #업종
    employee = models.CharField(max_length=50) #사원수(명)
    sales = models.CharField(max_length=50) #매출규모(억)
    address = models.CharField(max_length=100) #주소(도로명 주소)
    weblink = models.CharField(max_length=200) #웹사이트 주소
    introduce = models.CharField(max_length=500) #기업소개 및 기업규몬
    work = models.CharField(max_length=50) # 담당업무
    req_apply = models.CharField(max_length=200) #지원요건
    recruitment = models.CharField(max_length=50) #채용인원
    submit = models.CharField(max_length=50) #제출서류
    submit_deadline = models.CharField(max_length=100) #서류제출 마감일
    etc1 = models.CharField(max_length=200) #기타사항들...
    etc2 = models.CharField(max_length=200)
    etc3 = models.CharField(max_length=200)

    def __str__(self):
        return self.sector
