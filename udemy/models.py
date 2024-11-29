from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=5)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome #Essa função vaz apresentar o nome do objeto quando ele for istanciado.

class cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobre Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    


