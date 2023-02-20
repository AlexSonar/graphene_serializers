import graphene
from graphene_django.types import DjangoObjectType
from ReservationsManagerApp.models import   Reservation, ReservationComponent
from InvoicesManagerApp.models import Invoice, InvoiceEntry, InvoiceEntryComponent
from PaymentsManagerApp.models import Payment, PaymentReservationComponent

class ReservationType(DjangoObjectType):
    class Meta:
        model = Reservation

class ReservationComponentType(DjangoObjectType):
    class Meta:
        model = ReservationComponent

class InvoiceType(DjangoObjectType):
    class Meta:
        model = Invoice

class InvoiceEntryType(DjangoObjectType):
    class Meta:
        model = InvoiceEntry

class InvoiceEntryComponentType(DjangoObjectType):
    class Meta:
        model = InvoiceEntryComponent

class PaymentType(DjangoObjectType):
    class Meta:
        model = Payment

class PaymentReservationComponentType(DjangoObjectType):
    class Meta:
        model = PaymentReservationComponent

class  Query(object):
    all_reservations = graphene.List(ReservationType)
    all_reservation_components = graphene.List(ReservationComponentType)
    all_invoices = graphene.List(InvoiceType)
    all_invoice_components = graphene.List(InvoiceEntryType)
    all_invoice_entries_components = graphene.List(InvoiceEntryComponentType)
    all_payment = graphene.List(PaymentType)
    all_payment_reservation_components = graphene.List(PaymentReservationComponentType)

    def resolve_all_reservations(self, info, **kwargs):
        return Reservation.objects.all()

    def resolve_all_reservation_components(self, info, **kwargs):
        return ReservationComponent.objects.select_related('reservation').all()

    def resolve_all_invoice_entries_components(self, info, **kwargs):
        return InvoiceEntryComponent.objects.select_related('reservation_component').all()

    def resolve_all_payment_reservation_components(self, info, **kwargs):
        return PaymentReservationComponent.objects.select_related('reservation_component').all()
