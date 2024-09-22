from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date

class UserManager(BaseUserManager):
    def create_user(self, email, nome, whatsapp, password=None):
        if not email:
            raise ValueError("Usuários devem ter um email")
        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            whatsapp=whatsapp,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_ultimo_acesso = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Animal(models.Model):
    ESPECIE_CHOICES = [
        (1, 'Cão'),
        (2, 'Gato')
    ]
    
    animal_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=4, choices=ESPECIE_CHOICES)
    raca = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    condicao_corporal = models.IntegerField()
    gestacao = models.BooleanField(default=False)
    semana_gestacao = models.IntegerField(null=True, blank=True)
    lactacao = models.IntegerField(null=True, blank=True)
    semana_lactacao = models.IntegerField(null=True, blank=True)
    foto = models.CharField(max_length=255, null=True, blank=True)

    def idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year

    def fase_vida(self):
        idade = self.idade()
        if idade < 1:
            return "Filhote"
        elif 1 <= idade < 7:
            return "Adulto"
        else:
            return "Idoso"
