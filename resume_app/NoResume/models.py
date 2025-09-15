from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __repr__(self):
        return self.name


class Skill(models.Model):
    user = models.ManyToManyField(User, related_name="skills")
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=100)
    skill_proficiency = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True)

    def __repr__(self):
        return self.skill_name


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experience")
    experience_id = models.AutoField(primary_key=True)
    experience_name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.experience_name} at {self.location}"


class Volunteer_Experience(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="volunteer_experience"
    )
    volunteer_id = models.AutoField(primary_key=True)
    volunteer_name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __repr__(self):
        return self.volunteer_name


class Certification(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="certifications"
    )
    certificate_id = models.AutoField(primary_key=True)
    certificate_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    provider = models.CharField(max_length=100)

    def __repr__(self):
        return self.certificate_name


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education")
    education_id = models.AutoField(primary_key=True)
    education_name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    grade = models.IntegerField(null=True)

    def __repr__(self):
        return f"{self.education_name} from {self.institution}"
