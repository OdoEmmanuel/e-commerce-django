from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

# Create your models here.
class Category(MPTTModel):
    """
    Inventory Categoy table implimented with MPTT
    """

    name = models.CharField(
        max_length=100,
        null=False, 
        unique=False, 
        blank=False, 
        verbose_name=_("category name"),
        help_text=_("format: required, max-100")
    )
    slug =  models.SlugField(
       max_length=100,
       null=False,
       unique=False,
       blank=False,
       help_text=_("format: required, letter, numbers, underscore, or hyphens"),        
    )
    is_active = models.BooleanField(default=True,)


    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self):
        return self.name
    