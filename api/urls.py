from django.urls import path, include
from rest_framework import routers
from .views import (CommonMachineSettingViewSet, UniqueMachineSettingViewSet,MachineViewSet,
                    MedicineViewSet,
                    PatientHistoryPhotosViewSet, PatientHistoryViewSet,PatientViewSet,
                    PackageCommentViewSet, PackageViewSet,
                    DoseCommentViewSet, DoseViewSet,DoctorViewSet,
                    DoctorViewStorageViewSet,MachineHardwareViewSet)
from .views import get_all_cities

router = routers.DefaultRouter()
router.register(r'machine/common/setting', CommonMachineSettingViewSet)
router.register(r'machine/unique/Setting', UniqueMachineSettingViewSet)
router.register(r'machine', MachineViewSet)
router.register(r'medicine', MedicineViewSet)
router.register(r'patient/history/Photos', PatientHistoryPhotosViewSet)
router.register(r'patient/history', PatientHistoryViewSet)
router.register(r'patient', PatientViewSet)
router.register(r'package/comment', PackageCommentViewSet)
router.register(r'package', PackageViewSet)
router.register(r'dose/comment', DoseCommentViewSet)
router.register(r'dose', DoseViewSet)
router.register(r'doctor', DoctorViewSet)
router.register(r'doctorview/storage', DoctorViewStorageViewSet)
router.register(r'hardware', MachineHardwareViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_all_cities/', get_all_cities, name='get_all_cities'),
]