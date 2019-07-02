from django.contrib import admin
from test01 import models

# Register your models here.
#admin.site.register(models.Eos)
@admin.register(models.Form1_1_1)
class Form1_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,21,1) ]#21


@admin.register(models.Form1_1_2)
class FormForm1_1_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,21,1) ]


@admin.register(models.Form2_1_1)
class Form2_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,48,1) ]


@admin.register(models.Form2_1_2)
class Form2_1_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,48,1) ]


@admin.register(models.Form2_1_3)
class Form2_1_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,48,1) ]


@admin.register(models.Form2_2_1)
class Form2_2_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,14,1) ]


@admin.register(models.Form3_1_1)
class Form3_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,5,1) ]


@admin.register(models.Form3_1_2)
class Form3_1_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,33,1) ]#33


@admin.register(models.Form3_1_3)
class Form3_1_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,10,1) ]



@admin.register(models.Form3_2_1)
class Form3_2_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,5,1) ]


@admin.register(models.Form3_2_2)
class Form3_2_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,33,1) ]


@admin.register(models.Form3_2_3)
class Form3_2_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,9,1) ]


@admin.register(models.Form3_3_1)
class Form3_3_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]

@admin.register(models.Form3_3_2)
class Form3_3_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]


@admin.register(models.Form3_3_3)
class Form3_3_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]


@admin.register(models.Form3_3_4)
class Form3_3_4Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,35,1) ]


@admin.register(models.Form3_3_5)
class Form3_3_5Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,11,1) ]


@admin.register(models.Form3_4_1)
class Form3_4_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,15,1) ]


@admin.register(models.Form3_4_2)
class Form3_4_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]



@admin.register(models.Form3_4_3)
class Form3_4_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,13,1) ]


@admin.register(models.Form4_1_1)
class Form4_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,16,1) ]


@admin.register(models.Form5_1_1)
class Form5_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,17,1) ]

@admin.register(models.Form5_1_2)
class Form5_1_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,24,1) ]

@admin.register(models.Form5_1_3)
class Form5_1_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,11,1) ]

