from django.shortcuts import render
from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer




#--------------------------------------------#
#                 CATÉGORIES                 #
#--------------------------------------------#

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    
    def perform_create(self, serializer):
        serializer.save()



#--------------------------------------------#
#                   TÂCHES                   #
#--------------------------------------------#

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority', 'status']
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    @action(detail=True, methods=['post'])
    def terminer(self, request, pk=None):
        task = self.get_object()
        task.status = 'done'
        task.completed_at = timezone.now()
        task.save()
        return Response({'status': 'tâche terminée'})
    
    @action(detail=True, methods=['post'])
    def annuler(self, request, pk=None):
        task = self.get_object()
        task.status = 'canceled'
        task.save()
        return Response({'status': 'tâche annulée'})
    
    @action(detail=False, methods=['get'])
    def en_retard(self, request):
        overdue_tasks = Task.objects.filter(
            owner=request.user,
            due_date__lt=timezone.now(),
            status__in=['todo', 'in_progress']
        )
        serializer = self.get_serializer(overdue_tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def par_statut(self, request):
        status_param = request.query_params.get('status', None)
        if status_param:
            tasks = Task.objects.filter(owner=request.user, status=status_param)
            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data)
        return Response(
            {"error": "Paramètre 'status' requis"}, 
            status=status.HTTP_400_BAD_REQUEST
        )




#--------------------------------------------#
#              UTILISATEURS                  #
#--------------------------------------------#

class UserTasksView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    @action(detail=False, methods=['get'])
    def statistiques(self, request):
        user_tasks = Task.objects.filter(owner=request.user)
        total = user_tasks.count()
        todo = user_tasks.filter(status='todo').count()
        in_progress = user_tasks.filter(status='in_progress').count()
        done = user_tasks.filter(status='done').count()
        canceled = user_tasks.filter(status='canceled').count()
        overdue = user_tasks.filter(
            due_date__lt=timezone.now(),
            status__in=['todo', 'in_progress']
        ).count()
        
        return Response({
            'total': total,
            'a_faire': todo,
            'en_cours': in_progress,
            'terminees': done,
            'annulees': canceled,
            'en_retard': overdue
        })
