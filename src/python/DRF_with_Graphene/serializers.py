from rest_framework import serializers
from graphene_django.rest_framework.mutation import SerializerMutation
from GeneralApp.models import Airport
from ReservationsManagerApp.serializers import ReservationSerializer
from ReservationsManagerApp.models import ReservationComponent, ReservationHotel, ReservationRoundtrip, ReservationTransfer, ReservationTour, ReservationService, Hotel

class ReservationMutation(SerializerMutation):
    class Meta:
        serializer_class = ReservationSerializer

class ReservationComponentGraphSerializer(serializers.ModelSerializer):
    component = serializers.SerializerMethodField()

    class Meta:
        model = ReservationComponent
        fields = ('id', 'reservation', 'dertour_bk', 'day', 'content_type', 'object_id', 'comment', 'is_invoiced', 'component')

    def get_component(self, instance):
        components_models = {
            'reservationhotel': ReservationHotel,
            'reservationroundtrip': ReservationRoundtrip,
            'reservationtransfer': ReservationTransfer,
            'reservationtour': ReservationTour,
            'reservationservice': ReservationService,
        }

        component = components_models[instance.content_type.model].objects.get(id=instance.object_id)

        return self.get_component_string(instance.content_type.model, component)

    def get_component_string(self, component_model, component):
        components_get_string = {
            'reservationhotel': self.get_hotel_string,
            'reservationroundtrip': self.get_roundtrip_string,
            'reservationtransfer': self.get_transfer_string,
            'reservationtour': self.get_tour_string,
            'reservationservice': self.get_service_string,
        }
        return components_get_string[component_model](component)

    def get_hotel_string(self, component):
        return component.hotel.name

    def get_roundtrip_string(self, component):
        return component.roundtrip.name

    def get_transfer_string(self, component):
        origin_str = self.get_place_str('origin', component)
        destination_str = self.get_place_str('destination', component)

        return "{} => {}".format(origin_str, destination_str)

    def get_place_str(self, case, component):
        places_models = {
            'airport': Airport,
            'hotel': Hotel,
        }

        if case == 'origin':
            return places_models[component.origin_content_type.model].objects.get(id=component.origin_object_id).name
        else:
            return places_models[component.destination_content_type.model].objects.get(id=component.destination_object_id).name

    def get_tour_string(self, component):
        return component.tour.name

    def get_service_string(self, component):
        return component.service.name

class ReservationComponentMutation(SerializerMutation):
    class Meta:
        serializer_class = ReservationComponentGraphSerializer
