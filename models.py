from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    register_no = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    package = models.DecimalField(max_digits=6, decimal_places=2)
    eligibility_cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Placement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_role = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    placement_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.company.company_name}"
