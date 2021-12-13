from rest_framework import viewsets

from expenses.models import Expense
from expenses.serializers import ExpenseSerializer


class ExpensesView(viewsets.ReadOnlyModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
