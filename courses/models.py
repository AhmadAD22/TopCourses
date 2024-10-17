from django.db import models
from accounts.models import User
class Course(models.Model):
    image=models.ImageField(upload_to='media/courses',null=True,blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class StudentsCourse(models.Model):
     student = models.ForeignKey(User, on_delete=models.CASCADE)
     course = models.ForeignKey(Course, on_delete=models.CASCADE)
     

class Session(models.Model):
    number=models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Session on {self.date} for {self.course.name}"

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.fullName} attendance for {self.session}"
    
class EvaluationType(models.TextChoices):
    PRE="قبلي"
    POST='بعدي'

class Evaluation(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    type=models.CharField(max_length=50,choices=EvaluationType.choices)

    def __str__(self):
        return f"Evaluations for {self.student.fullName} in {self.session}"
    
class Question(models.Model):
    evaluation=models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    question=models.CharField(max_length=250)
    answer=models.TextField(null=True,blank=True)

class SessionRating(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    rating = models.IntegerField()
    message=models.TextField()
    

    def __str__(self):
        return f"Rating {self.rating} by {self.student.fullName} for {self.session}"
