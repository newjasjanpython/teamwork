from django.db import models

class Catalog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Test(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='tests')
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  # Marks whether this is the correct answer
    
    def __str__(self):
        return f"Answer for {self.question.text}: {self.text}"
