from rest_framework import serializers
from apps.locations.models import Countries, States, Cities


class CountrySerializers(serializers.ModelSerializer):
    # Se definen los atributos
    class Meta:
        model = Countries 
        fields = '__all__'

    def to_representation(self, instance):
        return {
                'id' : instance.id,
                'name': instance.name,
                'iso3':instance.iso3,
                'numeric_code':instance.numeric_code,
                'iso2':instance.iso2,
                'phonecode':instance.phonecode,
                'capital':instance.capital,
                'currency':instance.currency,
                'currency_name':instance.currency_name,
                'currency_symbol':instance.currency_symbol,
                'tld':instance.tld,
                'native':instance.native,
                'region':instance.region,
                'sub_region':instance.subregion,
                'timezones':instance.timezones,
                'translations':instance.translations,
                'latitude':instance.latitude,
                'longitude':instance.longitude,
                'emoji':instance.emoji,
                'emojiu':instance.emojiu,
                'flag':instance.flag,
                'wikidataid':instance.wikidataid
            }

class CountryStateSerializers(serializers.ModelSerializer):

    class Meta:
        model = States
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
                'id' : instance.id,
                'name' : instance.name,
                'country_code' : instance.country_code,
                'fips_code' : instance.fips_code,
                'iso2' : instance.iso2,
                'type' : instance.type,
                'latitude' : instance.latitude,
                'longitude' : instance.longitude,
                'flag' : instance.flag,
                'wikidataid' : instance.wikidataid,
                'country' : {
                    'id' : instance.country.id,
                    'name' : instance.country.name
                }
        }


class CitySerializers(serializers.ModelSerializer):

    class Meta:
        model = Cities
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'name' : instance.name,
            'state_code' : instance.state_code,
            'country_code' : instance.country_code,
            'latitude' : instance.latitude,
            'longitude' : instance.longitude,
            'flag' : instance.flag,
            'wikidataid' : instance.wikidataid,
            'country' : {
                'id' : instance.country.id,
                'name' : instance.country.name
            },
            'state' : {
                'id' : instance.state.id,
                'name' : instance.state.name
            }
        }

