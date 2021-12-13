from django.contrib import admin
from django.contrib.admin import register

from expenses.models import Expense


@register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass
