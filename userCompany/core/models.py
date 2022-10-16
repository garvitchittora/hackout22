from django.db import models

class Country(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "Country"
        verbose_name_plural = "Country"
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length = 50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    code = models.CharField(max_length = 50)

    class Meta:
        db_table = "City"
        verbose_name_plural = "City"
    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length = 500)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    summary = models.CharField(max_length = 500)
    avg_rating = models.FloatField()
    count_of_rating = models.IntegerField()
    video_url = models.CharField(max_length = 500, default = "")
    tgid = models.IntegerField(null = True)

    class Meta:
        db_table = "Experience"
        verbose_name_plural = "Experience"

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length = 50)
    url = models.CharField(max_length = 100)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    class Meta:
        db_table = "Image"
        verbose_name_plural = "Image"

    def __str__(self):
        return self.name

class Inventory(models.Model):
    slot = models.IntegerField()
    date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    class Meta:
        db_table = "Inventory"
        verbose_name_plural = "Inventory"

    def __str__(self):
        return self.experience.name + " " + self.city.name + " " + str(self.date)

class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    image = models.CharField(max_length = 500, default = "")
    level = models.IntegerField(default=0)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    class Meta:
        db_table = "User"
        verbose_name_plural = "User"

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

class Interest(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Interest"
        verbose_name_plural = "Interest"

    def __str__(self):
        return self.experience.name + " " + self.user.name

class ViewedInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

    class Meta:
        db_table = "ViewedInterest"
        verbose_name_plural = "ViewedInterest"

    def __str__(self):
        return self.user.name + " " + self.interest.experience.name

class Comments(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_text = models.CharField(max_length = 500)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Comments"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.user.name + " - " + str(self.experience.id)


class Notifications(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    notification_text = models.CharField(max_length = 500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Notifications"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return self.user.name + " " + str(self.timestamp) 
