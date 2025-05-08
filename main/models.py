from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



#--------------------------------------------------------------------------#
#                      Models des catégories de taches                     #
#--------------------------------------------------------------------------#
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['name']
    
    def __str__(self):
        return self.name




#--------------------------------------------------------------------------#
#                                Models des taches                         #
#--------------------------------------------------------------------------#
class Task(models.Model):
    """Modèle de tâche"""
    STATUS_CHOICES = [
        ('todo', 'À faire'),
        ('in_progress', 'En cours'),
        ('done', 'Terminée'),
        ('canceled', 'Annulée'),
    ]
    
    PRIORITY_CHOICES = [
        (1, 'Basse'),
        (2, 'Normale'),
        (3, 'Haute'),
        (4, 'Urgente'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")
    due_date = models.DateTimeField(blank=True, null=True, verbose_name="Date d'échéance")
    status = models.CharField( max_length=20, choices=STATUS_CHOICES, default='todo',verbose_name="Statut")
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2,verbose_name="Priorité")
    completed_at = models.DateTimeField(blank=True, null=True, verbose_name="Date de complétion")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks',verbose_name="Propriétaire")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='tasks',blank=True, null=True,verbose_name="Catégorie")
    
    class Meta:
        verbose_name = "Tâche"
        verbose_name_plural = "Tâches"
        ordering = ['-priority', 'due_date', 'created_at']
    
    def __str__(self):
        return self.title
    
    def mark_as_done(self):
        self.status = 'done'
        self.completed_at = timezone.now()
        self.save()
    
    @property
    def is_overdue(self):
        if self.due_date and self.status != 'done' and self.status != 'canceled':
            return timezone.now() > self.due_date
        return False
