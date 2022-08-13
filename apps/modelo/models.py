from django.db import models
class Aereolinea(models.Model):

    aereolinea_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 70, null = False)

    def __str__(self):
        
        return self.nombre
    
class Avion(models.Model):
    avion_id = models.AutoField(primary_key = True)
    numero = models.CharField(max_length = 20, unique = True, null = False)
    capacidad = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    puestos_Disponibles=models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    aereolinea = models.ForeignKey(Aereolinea, on_delete = models.CASCADE,blank=True, null=True)
    estado = models.BooleanField(default = True)
    

    def __str__(self):
        
        return self.numero

class Cliente(models.Model):

    listaGenero = (
        ('femenino','Femenino'),
        ('masculino', 'Masculino')
    )

    cliente_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length = 10, unique = True)
    nombres = models.CharField(max_length = 70, null = False)
    apellidos = models.CharField(max_length = 70, null = False)
    genero = models.CharField(max_length = 30, choices = listaGenero, default = 'masculino')
    correo = models.EmailField(max_length = 105, null = False, unique = True)
    celular = models.CharField(max_length = 15,  null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    

    def __str__ (self):
        return self.cedula

class Asiento(models.Model):

    listaCategoria = (
        ('ventana','Ventana'),
        ('medio', 'Medio'),
        ('pasillo', 'Pasillo'),
    )

    asiento_id = models.AutoField(primary_key = True)
    numero = models.CharField(max_length = 20, null = False)
    categoria = models.CharField(max_length = 30, choices = listaCategoria)
    avion = models.ForeignKey(Avion, on_delete = models.CASCADE) 
    estado = models.BooleanField(default = True)
         
    def __int__(self):
        
        return self.asiento_id

class Pais(models.Model):

    pais_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 70, null = False)

    def __str__(self):
        
        return self.nombre

class Ciudad(models.Model):

    ciudad_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 70, null = False)
    nombreAereopuerto = models.CharField(max_length = 70, null = False)
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE)

    def __str__(self):
        
        return self.nombre

class Viaje(models.Model):

    viaje_id = models.AutoField(primary_key = True)
    numero = models.CharField(max_length = 20, unique = True, null = False)
    fechaViaje = models.DateTimeField()
    fechaLlegada = models.DateTimeField()
    destino = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    avion = models.ForeignKey(Avion, on_delete = models.CASCADE) 
    estado = models.BooleanField(default = True)
    
         
    def __str__(self):
        
        return self.numero

class Boleto(models.Model):

    boleto_id = models.AutoField(primary_key = True)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete = models.CASCADE)
    num_asiento = models.CharField(max_length = 20)
    categoria_asiento = models.CharField(max_length = 20, null= True)
    coste = models.DecimalField(max_digits = 10, decimal_places = 2,default = 150.00)
    estado = models.BooleanField(default = True)
    
         
    def __int__(self):
        
        return self.boleto_id

