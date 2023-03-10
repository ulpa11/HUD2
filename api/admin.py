from django.contrib import admin
from .models import (CommonMachineSetting, UniqueMachineSetting, Machine,
                     Medicine, PatientHistoryPhotos, PatientHistory,
                     Patient, PackageComment, Package, DoseComment, Dose,DoctorViewStorage,
                     UserProfile,MachineHardware)

# Register your models here.

admin.site.register(CommonMachineSetting)
admin.site.register(UniqueMachineSetting)
admin.site.register(Machine)
admin.site.register(Medicine)
admin.site.register(PatientHistoryPhotos)
admin.site.register(PatientHistory)
admin.site.register(Patient)
admin.site.register(PackageComment)
admin.site.register(Package)
admin.site.register(DoseComment)
admin.site.register(Dose)
admin.site.register(DoctorViewStorage)
admin.site.register(UserProfile)
admin.site.register(MachineHardware)