from rest_framework import serializers
from .models import (CommonMachineSetting, UniqueMachineSetting, Machine,
                     Medicine, PatientHistoryPhotos, PatientHistory,Patient,
                     PackageComment, Package,
                     DoseComment, Dose,DoctorViewStorage,MachineHardware)

class CommonMachineSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonMachineSetting
        fields = '__all__'
class UniqueMachineSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueMachineSetting
        fields = '__all__'
class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'
class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
class PatientHistoryPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistoryPhotos
        fields = '__all__'
class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = '__all__'
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
class PackageCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageComment
        fields = '__all__'
class PackageSerializer(serializers.ModelSerializer):
    #package_comment=PackageCommentSerializer(many=True,read_only=True)#added
    class Meta:
        model = Package
        fields = '__all__'
class DoseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoseComment
        fields = '__all__'
class DoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dose
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance

class DoctorViewStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorViewStorage
        fields = '__all__'

class MachineHardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineHardware
        fields = '__all__'






